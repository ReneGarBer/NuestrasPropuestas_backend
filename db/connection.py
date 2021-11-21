import mysql.connector
import hashlib

class Database:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                user='root',
                password='',
                database='nuestras_propuestas'
            )
            self.cursor = self.connection.cursor()
        except:
            print('No se pudo establecer la conexión a la base de datos')

    def iniciar_sesion(self, username, password):
        h = hashlib.new('sha256', bytes(password ,'utf-8'))
        h = h.hexdigest()

        print(username, h)

        query = 'SELECT id FROM administradores WHERE username = %s AND password = %s'
        self.cursor.execute(query, (username, h))

        id = self.cursor.fetchone()

        if id:
            return id[0], True
        else:
            return None, False


    def crear_usuario(self, username, password):
        if self.existe_usuario(username):
            return False
        else:
            h = hashlib.new('sha256', bytes(password, 'utf-8'))
            h = h.hexdigest()

            print(username, h)
            query = "INSERT INTO administradores(username, password) VALUES (%s, %s)"
            self.cursor.execute(query, (username, h))
            self.connection.commit()

            return True

    def existe_usuario(self, username):
        query = "SELECT COUNT(*) FROM administradores WHERE username = %s"
        self.cursor.execute(query, (username,))

        return self.cursor.fetchone()[0] == 1