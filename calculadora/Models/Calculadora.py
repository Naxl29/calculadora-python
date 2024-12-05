import mysql.connector

class ModeloCalculadora:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="Calculadora"
            )
        self.cursor = self.conn.cursor()
        
        