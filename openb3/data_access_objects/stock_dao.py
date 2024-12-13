from openb3 import Stock 

class StockDAO:
    @classmethod
    def add_stock(cls, db, code, name, current_price, beta_variation, enterprise_value, ev_ebitda, pe_ratio, pb_ratio):
        query = """
        INSERT INTO Stock (code, name, current_price, beta_variation, enterprise_value, ev_ebitda, pe_ratio, pb_ratio)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        params = (code, name, current_price, beta_variation, enterprise_value, ev_ebitda, pe_ratio, pb_ratio)
        return db.execute_query(query, params)

    @classmethod
    def _convert_to_stock(cls, data):
        """
        Converts a dictionary fetched from the database into a Stock object.
        """
        if not data:
            return None
        return Stock(
            code=data['code'],
            name=data['name'],
            amount=data.get('amount', 0),  # Assuming a default of 0 if 'amount' is not in the data
            total_cost=data.get('total_cost', 0.0),  # Assuming a default of 0.0
            monitoring=data.get('monitoring', {})  # Default to an empty dict if not present
        )

    @classmethod
    def get_all_stocks(cls, db):
        query = "SELECT * FROM Stock"
        result = db.fetch_all(query)
        return [cls._convert_to_stock(row) for row in result]

    @classmethod
    def get_stock_by_id(cls, db, stock_id):
        query = "SELECT * FROM Stock WHERE id = %s"
        result = db.fetch_one(query, (stock_id,))
        return cls._convert_to_stock(result)

    @classmethod
    def get_stock_by_code(cls, db, stock_code):
        query = "SELECT * FROM Stock WHERE code = %s"
        result = db.fetch_one(query, (stock_code,))
        return cls._convert_to_stock(result)

    @classmethod
    def get_id_by_stock_code(cls, db, stock_code):
        query = "SELECT id FROM Stock WHERE code = %s"
        result = db.fetch_one(query, (stock_code,))
        if result:
            return result['id']
        return None

    @classmethod
    def update_stock_price(cls, db, stock_id, new_price):
        query = "UPDATE Stock SET current_price = %s WHERE id = %s"
        return db.execute_query(query, (new_price, stock_id))

    @classmethod
    def delete_stock(cls, db, stock_id):
        query = "DELETE FROM Stock WHERE id = %s"
        return db.execute_query(query, (stock_id,))
