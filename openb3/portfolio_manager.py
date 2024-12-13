from .stock import Stock
import yfinance as yf
from .data_collector import DataCollector
from .notification_trigger import NotificationTrigger
from data_access_objects import PortfolioStockDAO, PortfolioDAO, TransactionDAO, NotificationTriggerDAO, StockDAO, Database
from datetime import datetime
import threading
from time import sleep

class PortfolioManager:

    def __init__(self, user_id: int, name: str = None, stock_codes: list[str] = [], portfolio_id: int = None, db = None):
        self.db = db
        self.user_id = user_id
        self.name = name
        self.stocks = []
        self.triggers = {}
        self.id = None
        self.step_time = 1

        if portfolio_id:
            portfolio = PortfolioDAO.get_portfolio_by_id(self.db, portfolio_id)
            if portfolio:
                self.name = portfolio["name"]
                self.user_id = portfolio["user_id"]
                portfolio_stocks = PortfolioStockDAO.get_portfolio_stocks_by_portfolio(self.db, portfolio_id)
                stock_codes = []
                for ps in portfolio_stocks:
                    stock = StockDAO.get_stock_by_id(self.db, ps["stock_id"])
                    stock_codes.append(stock.code)
            else:
                raise ValueError
            self.id = portfolio_id
        else:
            PortfolioDAO.add_portfolio(self.db, self.user_id, self.name)
            self.id = PortfolioDAO.get_last_created_portfolio(self.db, self.user_id)["id"]

        for stock_code in stock_codes:
            self.add_stock(stock_code)
        
    def __str__(self):
        return f'[{self.id}] {self.name}: {self.stocks}'

    def add_stock(self, stock_code: str):
        if not DataCollector.stock_exists(stock_code):
                print(
                    f'Error while saving stock markets: stock "{stock_code} does not exist"'
                )
                raise ValueError


        ticker = DataCollector.request_stock(stock_code)
        ticker_info = ticker.info
        stock = Stock(stock_code, ticker_info.get("shortName", "Unknown"), 0, 0)
        
        stocks = list(map(lambda s: s["stock_id"], PortfolioStockDAO.get_portfolio_stocks_by_portfolio(self.db, self.id)))            
        id = StockDAO.get_id_by_stock_code(self.db, stock_code)

        if id in stocks:
            self.stocks.append(stock)
            self.triggers[stock_code] = []
            return 

        # TODO: Convert Ticker to Stock via get_stock
        if not StockDAO.get_id_by_stock_code(self.db, stock_code):
            StockDAO.add_stock(
                    self.db, 
                    stock_code,
                    ticker_info.get("shortName", "Unknown"), 
                    ticker_info.get('previousClose', 0),
                    ticker_info.get('beta', None),
                    ticker_info.get('marketCap', 0),
                    ticker_info.get('enterpriseToEbitda', None),
                    ticker_info.get('trailingPE', None),
                    ticker_info.get('priceToBook', None)
                )
        
        PortfolioStockDAO.add_portfolio_stock(self.db, self.id, StockDAO.get_id_by_stock_code(self.db, stock_code), 0, 0)
        self.stocks.append(stock)
        self.triggers[stock_code] = []
        
    def remove_stock(self, stock_code: str):
        """
        Remove a stock from the portfolio.
        """
        stock_id = StockDAO.get_id_by_stock_code(self.db, stock_code)
        
        # Check if the stock exists in the portfolio
        if stock_id is None:
            print(f"Stock with code {stock_code} does not exist in the portfolio.")
            return

        # Remove stock from PortfolioStockDAO
        PortfolioStockDAO.remove_stock_from_portfolio(self.db, self.id, stock_id)

        # Remove stock from the portfolio list
        self.stocks = [stock for stock in self.stocks if stock.code != stock_code]
        print(f"Stock {stock_code} has been removed from the portfolio.")

    def delete_portfolio(self):
        """
        Delete the entire portfolio and all associated records.
        """
        PortfolioStockDAO.remove_all_stocks_from_portfolio(self.db, self.id)
        TransactionDAO.remove_all_transactions_by_portfolio(self.db, self.id)
        NotificationTriggerDAO.remove_all_triggers_by_portfolio(self.db, self.id)
        PortfolioDAO.delete_portfolio(self.db, self.id)
        
        print(f"Portfolio {self.name} has been deleted successfully.")

    def create_notification_trigger(self, stock_code: str = None, upper_limit: float = None, lower_limit: float = None, method: str = None, notification_trigger_id: int = None):
        """
        Create a notification trigger for a stock in the portfolio.
        """

        if notification_trigger_id:
            trigger = NotificationTriggerDAO.get_notification_trigger_by_id(self.db, notification_trigger_id)
            stock = StockDAO.get_stock_by_id(self.db, trigger["stock_id"])
            if not self.triggers.get(stock.code, None):
                self.triggers[stock.code] = [] 

            self.triggers[stock.code].append(NotificationTrigger(stock.code, self.user_id, trigger["upper_limit"], trigger["lower_limit"], trigger["method"]))
            print(f"Notification trigger for stock {stock.code} created successfully.")
            return 

        if not (stock_code and upper_limit and lower_limit and method):
            print("Invalid number of parameters")
            raise ValueError

        if method not in ['email', 'sms', 'push']:
            print(f"Invalid notification method: {method}. It must be 'email', 'sms', or 'push'.")
            return
        
        stock_id = StockDAO.get_id_by_stock_code(self.db, stock_code)
        if not stock_id:
            print(f"Stock with code {stock_code} does not exist.")
            return
        
        NotificationTriggerDAO.add_notification_trigger(self.db, self.user_id, stock_id, upper_limit, lower_limit, method)
        self.triggers[stock_code].append(NotificationTrigger(stock_code, self.user_id, upper_limit, lower_limit, method))
        print(f"Notification trigger for stock {stock_code} created successfully.")

    def delete_notification_trigger(self, trigger_id: int = None, stock_code: str = None):
        """
        Delete a notification trigger by trigger ID or stock code.
        """
        if trigger_id is not None:
            NotificationTriggerDAO.delete_trigger_by_id(self.db, trigger_id)
            print(f"Notification trigger with ID {trigger_id} has been deleted.")
        
        elif stock_code is not None:
            stock_id = StockDAO.get_id_by_stock_code(self.db, stock_code)
            if stock_id:
                NotificationTriggerDAO.delete_notification_trigger(self.db, self.user_id, stock_id)
                self.triggers[stock_code] = []
                print(f"Notification trigger for stock {stock_code} has been deleted.")
            else:
                print(f"Stock with code {stock_code} does not exist.")
        else:
            print("Either trigger_id or stock_code must be provided.")

    def add_transaction(self, portfolio_stock_id: int, quantity: float, purchase_price: float):
        """
        Add a transaction for a stock in the portfolio.
        """
        # Add the transaction to the database
        TransactionDAO.add_transaction(self.db, self.user_id, portfolio_stock_id, quantity, purchase_price)        
        PortfolioStockDAO.update_portfolio_stock(self.db, portfolio_stock_id, quantity, purchase_price)
        
        print(f"Transaction for stock with portfolio_stock_id {portfolio_stock_id} added successfully.")

    def should_notify(self, stock: Stock):
        for trigger in self.triggers.get(stock.code, []):
            if trigger.check(stock):
                trigger.notify()
                trigger.last_notification = datetime.timestamp(datetime.now())

    def refresh_stocks(self):
        for s in self.stocks:
            stock = StockDAO.get_stock_by_code(self.db, s.code)
            self.should_notify(s)

    def daemon(self, stop_event: threading.Event = None):
        while not stop_event.is_set():
            self.refresh_stocks()
            sleep(self.step_time)
