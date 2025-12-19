import mysql.connector as mysql


class DatabaseConnector:
    connection = None

    @classmethod
    def connect(cls):
        db_connection = mysql.connect(
            host="localhost",
            port=3306,
            user="root",
            passwd="123",
            database="pipeline_db",
        )

        cls.connection = db_connection
