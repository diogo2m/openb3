class UserDAO:
    @classmethod
    def add_user(cls, db, name, email, password, phone=None):
        query = "INSERT INTO User (name, email, password, phone) VALUES (%s, %s,%s, %s)"
        params = (name, email, password, phone)
        return db.execute_query(query, params)

    @classmethod
    def get_all_users(cls, db):
        query = "SELECT * FROM User"
        return db.fetch_all(query)

    @classmethod
    def get_user_by_id(cls, db, user_id):
        query = "SELECT * FROM User WHERE id = %s"
        return db.fetch_one(query, (user_id,))
    
    @classmethod
    def get_user_by_email(cls, db, email):
        query = "SELECT * FROM User WHERE email = %s"
        return db.fetch_one(query, (email,))
    
    @classmethod
    def get_user_by_phone(cls, db, phone):
        query = "SELECT * FROM User WHERE phone = %s"
        return db.fetch_one(query, (phone,))

    @classmethod
    def delete_user(cls, db, user_id):
        query = "DELETE FROM User WHERE id = %s"
        return db.execute_query(query, (user_id,))
