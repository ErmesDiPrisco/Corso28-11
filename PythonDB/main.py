from dataAccess import dataAccess



def unica_lista():
        while True:
            try:
                val=int(input('Scegli:\n1)Lista di tutti i film\n2)Lista dei film di tutti gli attori\n3)Per averle entrambe\nScegli 1 o 2 o 3:\n--->'))
                match val:
                    case 1:
                        conn1.query_lista_film()
                        conn1.stop()
                        return False
                    case 2:
                        conn1.query_lista_attori()
                        conn1.stop()
                        return False
                    case 3:
                        conn1.query_lista_attori()
                        conn1.query_lista_film()
                        conn1.stop()
                        return False
            except ValueError:
                print('Inserisci un numero intero')
                continue

conn1=dataAccess()
unica_lista()

