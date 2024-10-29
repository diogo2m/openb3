
class Stock:

    _code = ""
    _amount = 0
    _total_cost = 0
    _monitoring = None

    def __init__(self, code : str, amount : float, total_cost : float, monitoring : dict = None):
        self._code = code
        self._amount = amount
        self._total_cost = total_cost
        self._monitoring = monitoring
    
    @property
    def code(self):
        return self._code
    
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount : float):
        self._amount = amount

    @property
    def total_cost(self):
        return self._total_cost

    @total_cost.setter
    def total_cost(self, total_cost : float):
        self._total_cost = total_cost

    @property
    def monitoring(self):
        return self._monitoring

    @monitoring.setter
    def monitoring(self, monitoring : bool):
        self._monitoring = monitoring
