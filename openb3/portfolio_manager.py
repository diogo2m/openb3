from .stock import Stock
from .data_collector import DataCollector

class PortfolioManager:

    stocks = []

    def __init__(self, stock_codes : list[Stock]):
        for stock in stock_codes:
            if not DataCollector.stock_exists(stock):
                print(f'Error while saving stock markets: stock "{stock} does not exist"')
                return ValueError
            self.stocks = stock

