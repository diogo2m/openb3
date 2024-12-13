class PortfolioStockDAO:
    @classmethod
    def add_portfolio_stock(cls, db, portfolio_id, stock_id, quantity, purchase_price):
        query = """
        INSERT INTO PortfolioStock (portfolio_id, stock_id, quantity, purchase_price)
        VALUES (%s, %s, %s, %s)
        """
        params = (portfolio_id, stock_id, quantity, purchase_price)
        return db.execute_query(query, params)

    @classmethod
    def get_all_portfolio_stocks(cls, db):
        query = "SELECT * FROM PortfolioStock"
        return db.fetch_all(query)

    @classmethod
    def get_portfolio_stock_by_id(cls, db, portfolio_stock_id):
        query = "SELECT * FROM PortfolioStock WHERE id = %s"
        return db.fetch_one(query, (portfolio_stock_id,))

    @classmethod
    def get_portfolio_stocks_by_portfolio(cls, db, portfolio_id):
        query = "SELECT * FROM PortfolioStock WHERE portfolio_id = %s"
        return db.fetch_all(query, (portfolio_id,))

    @classmethod
    def get_portfolio_stocks_by_stock(cls, db, stock_id):
        query = "SELECT * FROM PortfolioStock WHERE stock_id = %s"
        return db.fetch_all(query, (stock_id,))

    @classmethod
    def update_portfolio_stock(cls, db, portfolio_stock_id, quantity=None, purchase_price=None):
        query = """
        UPDATE PortfolioStock
        SET quantity = COALESCE(%s, quantity),
            purchase_price = COALESCE(%s, purchase_price)
        WHERE id = %s
        """
        params = (quantity, purchase_price, portfolio_stock_id)
        return db.execute_query(query, params)

    @classmethod
    def remove_stock_from_portfolio(cls, db, portfolio_id, stock_id):
        query = "DELETE FROM PortfolioStock WHERE portfolio_id = %s AND stock_id = %s"
        return db.execute_query(query, (portfolio_id, stock_id))

    @classmethod
    def remove_all_stocks_from_portfolio(cls, db, portfolio_id):
        query = "DELETE FROM PortfolioStock WHERE portfolio_id = %s"
        return db.execute_query(query, (portfolio_id,))
