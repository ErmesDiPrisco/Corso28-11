import mysql.connector as mysql
from getpass import getpass

class Connessione():
    def __init__(self, connessione=None):
        self._connessione=connessione
    
    
    def get_richiesta_connessione(self):
        try:
            self._connessione=mysql.connect(host = "localhost" , user = "root" , passwd = getpass() ,port="3306",database="sakila" )
        except mysql.Error:
            print('Oops, qualcosa è andato storto')
            return mysql.Error
        

    def lista_film(self, query):
        lista=self._connessione.cursor()
        lista.execute(query)
        risultato=lista.fetchall()
        for res in risultato:
            print(res)

    def close_conn(self):
        self._connessione.close()
        print('Connessione chiusa con successo')