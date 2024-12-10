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
        
    def agregar_operacion(self, n1, signo, n2):
        consulta = "INSERT INTO operaciones (n1, signo, n2) VALUES (%s, %s, %s)"
        self.cursor.execute(consulta,(n1, signo, n2))
        self.conn.commit()


    def agregar_resultado(self, resultado):
        consulta = "INSERT INTO resultados (resultado) VALUES (%s)"
        self.cursor.execute(consulta,(resultado,))
        self.conn.commit()
    
    def ver_historial(self):
        self.cursor.execute("""SELECT o.id, o.n1, o.signo, o.n2, r.resultado
                FROM operaciones_resultados AS op
                JOIN operaciones AS o ON op.id_operacion = o.id
                JOIN resultados AS r ON op.id_resultado = r.id""")
        return self.cursor.fetchall()
    
    def ver_h(self):
        self.cursor.execute("""SELECT CONCAT(o.n1, o.signo, o.n2, ' = ', r.resultado) AS operacion
                FROM operaciones_resultados AS op
                JOIN operaciones AS o ON op.id_operacion = o.id
                JOIN resultados AS r ON op.id_resultado = r.id """)
        return self.cursor.fetchall
    
    def ver_h(self):
        self.cursor.execute("""SELECT CONCAT(o.n1, o.signo, o.n2, ' = ', r.resultado) AS operacion
                FROM operaciones_resultados AS op
                JOIN operaciones AS o ON op.id_operacion = o.id
                JOIN resultados AS r ON op.id_resultado = r.id """)
        return self.cursor.fetchall()
    
    def op_re(self, id_operacion, id_resultado):
        consulta = "INSERT INTO operaciones_resultados (id_operacion, id_resultado) VALUES (%s, %s)"
        self.cursor.execute(consulta,(id_operacion, id_resultado))
        self.conn.commit()

    def ultimo_id(self):
        consulta = "SELECT LAST_INSERT_ID()"
        self.cursor.execute(consulta)
        return self.cursor.fetchone()[0]
    

    def borrar_historial(self):
        consulta_relaciones = "DELETE FROM operaciones_resultados"
        self.cursor.execute(consulta_relaciones, ())
        consulta1 = "DELETE FROM operaciones"
        self.cursor.execute (consulta1, ())
        consulta2 = "DELETE FROM resultados"
        self.cursor.execute (consulta2, ())
        self.conn.commit()