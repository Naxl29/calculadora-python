import mysql.connector

class Database:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host='localhost',
            password="",
            user="root",
            database="Calculadora"
        )
        self.cursor = self.connection.cursor(dictionary=True)
        self.create_database(database)
        self.connection.database = database  

    def create_database(self, database):
        self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database};")
        self.cursor.execute(f"USE {database};")
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS operaciones (
                id INT AUTO_INCREMENT PRIMARY KEY,
                n1 INT NOT NULL,
                signo CHAR (1) NOT NULL,
                n2 INT INT NOT NULL
            );
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS resultados (
                id INT AUTO_INCREMENT PRIMARY KEY,
                resultado INT NOT NULL,
            );
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS transacciones (
                id INT AUTO_INCREMENT PRIMARY KEY,
                id_operacion INT NOT NULL,
                id_resultado INT NOT NULL,
                FOREIGN KEY (id_operacion) REFERENCES operaciones(id),
                FOREIGN KEY (id_resultado) REFERENCES resultados(id)
            );
        """)
        self.connection.commit()

    def execute_query(self, query, params=None):
        self.cursor.execute(query, params or ())
        self.connection.commit()

    def fetch_all(self, query, params=None):
        self.cursor.execute(query, params or ())
        return self.cursor.fetchall()

    def fetch_one(self, query, params=None):
        self.cursor.execute(query, params or ())
        return self.cursor.fetchone()
