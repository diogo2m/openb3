class PortfolioDAO:
    @classmethod
    def add_portfolio(cls, db, user_id, name):
        query = """
        INSERT INTO Portfolio (user_id, name)
        VALUES (%s, %s)
        """
        params = (user_id, name)
        return db.execute_query(query, params)

    @classmethod
    def get_all_portfolios(cls, db):
        query = "SELECT * FROM Portfolio"
        return db.fetch_all(query)

    @classmethod
    def get_portfolio_by_id(cls, db, portfolio_id):
        query = "SELECT * FROM Portfolio WHERE id = %s"
        return db.fetch_one(query, (portfolio_id,))

    @staticmethod
    def get_portfolios_by_user_id(db, user_id):
        query = """
        SELECT * FROM Portfolio WHERE user_id = %s ORDER BY created_at DESC
        """
        result = db.fetch_all(query, (user_id,))
        return result

    @staticmethod
    def get_last_created_portfolio(db, user_id):
        portfolios = PortfolioDAO.get_portfolios_by_user_id(db, user_id)
        if portfolios:
            return portfolios[0]  # Return the most recently created portfolio
        return None

    @classmethod
    def delete_portfolio(cls, db, portfolio_id):
        query = "DELETE FROM Portfolio WHERE id = %s"
        return db.execute_query(query, (portfolio_id,))
