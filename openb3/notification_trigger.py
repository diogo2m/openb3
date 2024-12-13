from .stock import Stock
from datetime import datetime

class NotificationTrigger:

    available_methods = ["sms", "email", "push"]
    delay_time = 30*60

    def __init__(self, stock_code: str, user_id: int, upper_limit: float, lower_limit: float, method: str):
        self.stock_code = stock_code
        self.user_id = user_id
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit
        self.method = method if method in NotificationTrigger.available_methods else "push"
        self.last_notification = 0

    def check(self, stock: Stock) -> bool:
        if datetime.timestamp(datetime.now()) - self.last_notification < NotificationTrigger.delay_time:
            return False
        
        if stock.purchase_price > self.upper_limit:
            return True
        
        if stock.purchase_price < self.lower_limit:
            return True
        
        return False

    def notify_email():
        pass

    def notify_sms():
        pass

    def notify_push():
        pass

    def notify(self):
        print(f"Bah fudeu, tua ação {self.stock_code} tá acima do limite")
