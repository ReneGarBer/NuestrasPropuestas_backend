from psycopg2 import sql
import psycopg2
import psycopg2.errorcodes
from clases import prueba
from np_bdd import np_bdd

class np_base(np_bdd):
    ##definir funciones base para todos los objetos que interactuan con la base de datos
    pass

class DaoPrueba(np_bdd):

    def add(self,prueba):
        try:
            query = sql.SQL("INSERT INTO prueba (asunto) VALUES ({value})".format(value=sql.Identifier('asunto de prueba')))
            self.cur.execute(query)
            self.conn.commit()
        except Exception as e:
            print(psycopg2.errorcodes.lookup(e.pgcode))


    def delete(self,prueba):
        try:
            query = sql.SQL("DELETE FROM prueba WHERE Id = {id}".format(id=sql.Identifier(prueba.getsetid)))
            self.cur.execute(query)
            self.conn.commit()
        except Exception as e:
            print(psycopg2.errorcodes.lookup(e.pgcode))

    def show(self,id):
        try:
            query = sql.SQL("SELECT * FROM prueba WHERE Id = {id}".format(id=id))
            self.cur.execute(query)
            self.conn.commit()
        except Exception as e:
            print(psycopg2.errorcodes.lookup(e.pgcode))
        return self.createobject(self.cur.fetchone())

    def showall(self):
        try:
            query = sql.SQL("SELECT * FROM prueba")
            self.cur.execute(query)
            self.conn.commit()
        except Exception as e:
            print(psycopg2.errorcodes.lookup(e.pgcode))
        
        return self.cur.fetchall()

    def advancedquery(self,query):
        try:
            self.cur.execute(query)
            self.conn.commit()
        except Exception as e:
            print(psycopg2.errorcodes.lookup(e.pgcode))

    def creatobject(self,resp):
        Prueba = prueba()
        Prueba.getsetid = resp[0]
        Prueba.getsetasunto = resp[1]
        return Prueba