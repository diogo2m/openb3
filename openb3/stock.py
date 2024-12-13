class Stock:
    def __init__(
        self, 
        code: str, 
        name: str,
        amount: float = 0.0, 
        total_cost: float = 0.0, 
        monitoring: dict = None,
        portfolio_id: int = None, 
        stock_id: int = None,
        quantity: int = 0, 
        purchase_price: float = 0.0
    ):
        # For the Stock table attributes
        self._code = code
        self._name = name
        self._amount = amount
        self._total_cost = total_cost
        self._monitoring = monitoring if monitoring else {}
        self.pricing_history = []

        # For the PortfolioStock table attributes
        self._portfolio_id = portfolio_id
        self._stock_id = stock_id
        self._quantity = quantity
        self._purchase_price = purchase_price

    def __str__(self):
        return f'{self.name} ({self.code}: R${self.purchase_price:.2f})'
    
    def __repr__(self):
        return f'{self.name} ({self.code}: R${self.purchase_price:.2f})'

    # Properties and Setters for Stock Table Attributes
    @property
    def code(self):
        return self._code

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name: name):
        self._name = name

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount: float):
        self._amount = amount

    @property
    def total_cost(self):
        return self._total_cost

    @total_cost.setter
    def total_cost(self, total_cost: float):
        self._total_cost = total_cost

    @property
    def monitoring(self):
        return self._monitoring

    @monitoring.setter
    def monitoring(self, monitoring: dict):
        self._monitoring = monitoring

    # Properties and Setters for PortfolioStock Table Attributes
    @property
    def portfolio_id(self):
        return self._portfolio_id

    @portfolio_id.setter
    def portfolio_id(self, portfolio_id: int):
        self._portfolio_id = portfolio_id

    @property
    def stock_id(self):
        return self._stock_id

    @stock_id.setter
    def stock_id(self, stock_id: int):
        self._stock_id = stock_id

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity: int):
        self._quantity = quantity

    @property
    def purchase_price(self):
        return self._purchase_price

    @purchase_price.setter
    def purchase_price(self, purchase_price: float):
        self._purchase_price = purchase_price

    # Method to calculate the total cost for PortfolioStock
    def calculate_total_cost(self):
        return self._quantity * self._purchase_price

    # Method to update the stock attributes based on the PortfolioStock values
    def update_stock_from_portfolio(self, quantity: int, purchase_price: float):
        self._quantity = quantity
        self._purchase_price = purchase_price
        self._total_cost = self.calculate_total_cost()

    def add_pricing_history(self, price: float):
        self.pricing_history.append(price)
