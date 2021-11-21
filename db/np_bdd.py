#esta clase conecta a la bdd y crea un cursor
#las demas clases usa el cursos para realizar las querys

import psycopg2

class np_bdd:
    def __init__(self) -> None:
        try:
            self.conn = psycopg2.connect(dbname='Test',user='postgres',password='postgres',host='::1',port=5432)
        except psycopg2.DatabaseError as e:
            print('Ocurrio un error: %', e)
        self.cur = self.conn.cursor()

    def __del__(self) -> None:
        self.cur.close()
        self.conn.close()