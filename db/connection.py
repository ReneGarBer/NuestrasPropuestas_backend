import mysql.connector
import hashlib
from pdftotext import PDFToText

class Database:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                user='root',
                password='',
                database='nuestras_propuestas'
            )
            self.cursor = self.connection.cursor()
            self.utils = PDFToText()
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

    def nueva_propuesta(self, data):
        try:
            titulo = data['titulo']
            extracto = data['extracto']
            contenido = self.utils.read_content(data['pdf'] + '.txt')
            archivo = data['pdf']
            estado = data['estado']
            partido = data['partido']
            fecha = data['fecha']
            autor = data['autor']
            subido = data['subido']


            query = """INSERT INTO 
                propuestas(titulo, extracto, contenido, archivo, estado, partido, fecha, autor, subido)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""


            self.cursor.execute(query, (titulo, extracto, contenido, archivo, estado, partido, fecha, autor, subido))
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False
    
    def get_propuestas(self, keywords = ''):
        query = """SELECT 
        id, titulo, extracto, archivo, estado, partido, fecha, autor
        FROM propuestas WHERE contenido LIKE %s """
        
        self.cursor.execute(query, ("%" + keywords + "%",))
        propuestas = []

        for row in self.cursor.fetchall():
            propuesta = {
                'id': row[0],
                'titulo': row[1],
                'extracto': row[2],
                'archivo': row[3],
                'estado': row[4],
                'partido': row[5],
                'fecha': row[6],
                'autor': row[7]
            }

            propuestas.append(propuesta)

        return propuestas

    def eliminar_propuesta(self, id):
        query = "DELETE FROM propuestas WHERE id = %s"
        self.cursor.execute(query, (id,))
        self.connection.commit()

        return self.cursor.rowcount

    def get_propuesta(self, id):
        query = """SELECT 
        id, titulo, extracto, archivo, estado, partido, fecha, autor, archivo
        FROM propuestas WHERE id = %s """

        self.cursor.execute(query, (id,))

        row = self.cursor.fetchone()
        propuesta = {}

        if row:
            propuesta = {
                'id': row[0],
                'titulo': row[1],
                'extracto': row[2],
                'archivo': row[3],
                'estado': row[4],
                'partido': row[5],
                'fecha': row[6],
                'autor': row[7],
                'archivo': row[8]
            }
        
        return propuesta

    def modificar_propuesta(self, data, id):
        try:
            titulo = data['titulo']
            extracto = data['extracto']
            contenido = self.utils.read_content(data['pdf'] + '.txt')
            archivo = data['pdf']
            estado = data['estado']
            partido = data['partido']
            fecha = data['fecha']
            autor = data['autor']

            query = """UPDATE propuestas SET 
                titulo = %s, extracto = %s, contenido =%s, archivo = %s, estado = %s, partido = %s, fecha = %s, autor = %s
                WHERE id = %s"""


            self.cursor.execute(query, (titulo, extracto, contenido, archivo, estado, partido, fecha, autor, id))
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False