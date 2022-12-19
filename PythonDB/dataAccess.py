from dbconn import Connessione

class dataAccess:
    def __init__(self):
        self.query='query'
        self.conn1=Connessione()
        self.conn1.get_richiesta_connessione()

    
    def query_lista_film(self):
        self.query='select title from film'
        self.conn1.lista_film(self.query)
        
    def query_lista_attori(self):
        self.query='select first_name, last_name from actor'
        self.conn1.lista_film(self.query)
        
    
    def stop(self):
            self.conn1.close_conn()