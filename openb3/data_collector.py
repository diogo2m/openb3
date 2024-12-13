import yfinance as yf
import logging
from time import sleep
from .stock import Stock
import threading
from data_access_objects import StockDAO, Database

class DataCollector:

    def __init__(self, step_time: float = 5, watch_list: list[Stock] = {}, db = None):
        self.db = db
        self.step_time = step_time
        self.watch_list = {}

        for s in watch_list:
            self.add_stock(s)

        # Suppress logging messages
        logging.getLogger("yfinance").setLevel(logging.CRITICAL)

    @staticmethod
    def stock_exists(stock_code: str) -> bool:
        try:
            ticker = DataCollector.request_stock(stock_code)
        except:
            pass
        
        if not ticker.info.get("previousClose"):
            stock_code += ".SA"
            ticker = DataCollector.request_stock(stock_code)
        
        if not ticker.info.get("previousClose"):
            return False
        
        return True

    def add_stock(self, stock_code: str):

        if stock_code in [s for s in self.watch_list]:
            return

        if DataCollector.stock_exists(stock_code):
            stock = Stock(stock_code, 0, 0)
            self.watch_list[stock_code] = stock
            return
        
        raise ValueError

    def set_step_time(self, new_time: float):
        self.step_time = new_time
    
    def daemon(self, stop_event: threading.Event = None):
        while not stop_event.is_set():
            self.refresh_stocks()
            sleep(self.step_time)

    @staticmethod
    def convert_yahoo_finances_to_stock(ticker: yf.Ticker):
        ticker_info = ticker.info
        last_price = ticker_info.get('previousClose', 0)
        stock_code = ticker_info.get('symbol', 'Unknown')
        stock_name = ticker_info.get('shortName', 'Unknown')
        market_cap = ticker_info.get('marketCap', 0)
        pe_ratio = ticker_info.get('trailingPE', None)
        pb_ratio = ticker_info.get('priceToBook', None)

        stock = Stock(
            code=stock_code,
            name=stock_name,
            amount=0,
            total_cost=0.0,
            monitoring={},
        )

        stock.beta_variation = ticker_info.get('beta', None)
        stock.enterprise_value = market_cap
        stock.ev_ebitda = ticker_info.get('enterpriseToEbitda', None)
        stock.pe_ratio = pe_ratio
        stock.pb_ratio = pb_ratio

        stock.add_pricing_history(last_price)

        return stock

    @staticmethod
    def request_stock(stock_code: str) -> yf.Ticker:
        try:
            ticker = yf.Ticker(f'{stock_code}.SA')
        except:
            ticker = None
        return ticker

    @staticmethod
    def get_stock(stock_code: str) -> Stock:
        return DataCollector.convert_yahoo_finances_to_stock(yf.Ticker(stock_code))

    def refresh_stocks(self):
        for s in self.watch_list:
            try:
                ticker = DataCollector.request_stock(self.watch_list[s].code)
                ticker_info = ticker.info

                self.watch_list[s].pricing_history.append(ticker.info["previousClose"])
                StockDAO.add_stock(
                    self.db, 
                    self.watch_list[s].code,  # Assuming ticker["code"] is like 'PETR4.SA' and you want 'PETR4'
                    ticker_info.get("shortName", "Unknown"), 
                    ticker_info.get('previousClose', 0),  # Assuming previousClose is your current price
                    ticker_info.get('beta', None),  # Assuming beta is available in ticker_info
                    ticker_info.get('marketCap', 0),  # Assuming marketCap is the enterprise value
                    ticker_info.get('enterpriseToEbitda', None),  # Assuming this is the EV/EBITDA ratio
                    ticker_info.get('trailingPE', None),  # Assuming this is the PE ratio
                    ticker_info.get('priceToBook', None)  # Assuming this is the PB ratio
                )
                # print(self.watch_list[s].pricing_history)
            except Exception as e:
                # print(e)
                self.watch_list[s].pricing_history.append(0)

