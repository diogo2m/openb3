class TransactionDAO:
    @classmethod
    def add_transaction(cls, db, user_id, portfolio_stock_id, quantity, purchase_price):
        query = """
        INSERT INTO Transaction (user_id, portfolio_stock_id, quantity, purchase_price)
        VALUES (%s, %s, %s, %s)
        """
        params = (user_id, portfolio_stock_id, quantity, purchase_price)
        return db.execute_query(query, params)

    @classmethod
    def get_all_transactions(cls, db):
        query = "SELECT * FROM Transaction"
        return db.fetch_all(query)

    @classmethod
    def get_transaction_by_id(cls, db, transaction_id):
        query = "SELECT * FROM Transaction WHERE id = %s"
        return db.fetch_one(query, (transaction_id,))

    @classmethod
    def get_transactions_by_user(cls, db, user_id):
        query = "SELECT * FROM Transaction WHERE user_id = %s"
        return db.fetch_all(query, (user_id,))

    @classmethod
    def get_transactions_by_portfolio_stock(cls, db, portfolio_stock_id):
        query = "SELECT * FROM Transaction WHERE portfolio_stock_id = %s"
        return db.fetch_all(query, (portfolio_stock_id,))

    @classmethod
    def update_transaction(cls, db, transaction_id, quantity=None, purchase_price=None):
        query = """
        UPDATE Transaction
        SET quantity = COALESCE(%s, quantity),
            purchase_price = COALESCE(%s, purchase_price)
        WHERE id = %s
        """
        params = (quantity, purchase_price, transaction_id)
        return db.execute_query(query, params)

    @classmethod
    def delete_transaction(cls, db, transaction_id):
        query = "DELETE FROM Transaction WHERE id = %s"
        return db.execute_query(query, (transaction_id,))
