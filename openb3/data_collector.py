
class DataCollector:

    step_time = 5;

    def set_step_time():
        return NotImplementedError

    def refresh_data_base():
        return NotImplementedError

    def get_stock(stock_code : str) -> dict:
        return NotImplementedError
    
    @classmethod
    def stock_exists() -> bool:
        return True