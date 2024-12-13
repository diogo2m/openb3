class NotificationTriggerDAO:
    @classmethod
    def add_notification_trigger(cls, db, user_id, stock_id, upper_limit=None, lower_limit=None, method="email"):
        query = """
        INSERT INTO NotificationTrigger (user_id, stock_id, upper_limit, lower_limit, method)
        VALUES (%s, %s, %s, %s, %s)
        """
        params = (user_id, stock_id, upper_limit, lower_limit, method)
        return db.execute_query(query, params)
    
    @classmethod
    def get_all_notification_triggers(cls, db):
        query = "SELECT * FROM NotificationTrigger"
        return db.fetch_all(query)

    @classmethod
    def get_notification_trigger_by_id(cls, db, trigger_id):
        query = "SELECT * FROM NotificationTrigger WHERE id = %s"
        return db.fetch_one(query, (trigger_id,))

    @classmethod
    def get_notification_triggers_by_user(cls, db, user_id):
        query = "SELECT * FROM NotificationTrigger WHERE user_id = %s"
        return db.fetch_all(query, (user_id,))

    @classmethod
    def get_notification_triggers_by_stock(cls, db, stock_id):
        query = "SELECT * FROM NotificationTrigger WHERE stock_id = %s"
        return db.fetch_all(query, (stock_id,))

    @classmethod
    def update_notification_trigger(cls, db, trigger_id, upper_limit=None, lower_limit=None, method=None):
        query = """
        UPDATE NotificationTrigger
        SET upper_limit = COALESCE(%s, upper_limit),
            lower_limit = COALESCE(%s, lower_limit),
            method = COALESCE(%s, method)
        WHERE id = %s
        """
        params = (upper_limit, lower_limit, method, trigger_id)
        return db.execute_query(query, params)

    @classmethod
    def delete_notification_trigger(cls, db, trigger_id):
        query = "DELETE FROM NotificationTrigger WHERE id = %s"
        return db.execute_query(query, (trigger_id,))

    @classmethod
    def delete_trigger_by_stock(cls, db, user_id, stock_id):
        query = "DELETE FROM NotificationTrigger WHERE user_id = %s AND stock_id = %s"
        return db.execute_query(query, (user_id, stock_id))
    
