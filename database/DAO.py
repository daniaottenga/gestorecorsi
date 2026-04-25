from database.DB_connect import DBConnect
from model.corso import Corso
from model.studente import Studente


class DAO():

    # 6. PRENDO I CODICI INSEGNAMENTO AL DB FACENDO UNA QUERY, SARA' SEMPRE UGUALE, CAMBIA SOLO LA QUERY
    @staticmethod
    def getCodins():
        cnx = DBConnect.get_connection() # chiede una connessione
        cursor = cnx.cursor(dictionary=True) # crea un cursore
        query = """select codins 
                    FROM corso""" # fa la query
        cursor.execute(query) # la eseguo

        res = []
        for row in cursor: # ciclo sul cursore per leggere i dati
            res.append(row["codins"]) # metto i dati in una lista, prendo la colonna codins delle righe

        cursor.close() # chiudo il cursore
        cnx.close() # restituiamo la connessione
        return res # restituisce una lista di stringhe con gli insegnamenti che aggiungerà nelle opzioni


    @staticmethod
    def getAllCorsi(): # fa una copia di quello prima e lo modifica
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select * FROM corso""" # leggo tutto il corso
        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(Corso( # appendo l'oggetto corso da creare in model
                codins = row["codins"], # row è un dizionario
                crediti = row["crediti"],
                nome = row["nome"],
                pd = row["pd"]
            ))

        cursor.close()
        cnx.close()
        return res # restituisco una lista di oggetti di tipo corso

    @staticmethod
    def getCorsiPD(pd):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """SELECT *
                    FROM corso c
                    WHERE c.pd = %s""" # %s è per dire che è un parametro

        cursor.execute(query, (pd,))

        res = []
        for row in cursor:
            res.append(Corso(**row)) # lo faccio quando la chiave del dizionario ha lo stesso nome della
            # proprietà dell'oggetto, fa l'unpack del dizionario

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getCorsiPDwIscritti(pd):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """SELECT c.codins, c.crediti, c.nome, c.pd, count(*) as n
                    FROM corso c, iscrizione i 
                    WHERE c.codins = i.codins 
                    and c.pd = %s
                    group by c.codins, c.crediti, c.nome, c.pd"""

        cursor.execute(query, (pd,))

        res = []
        for row in cursor:
            res.append((Corso(codins = row["codins"],
                              crediti = row["crediti"],
                              nome = row["nome"],
                              pd = row["pd"]),
                        row["n"] ))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getStudentiCorso(codins):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """SELECT s.*
                    FROM studente s, iscrizione i 
                    WHERE s.matricola = i.matricola 
                    and i.codins = %s"""

        cursor.execute(query, (codins,))

        res = []
        for row in cursor:
            res.append(Studente(**row))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getCDSofCorso(codins):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """SELECT s.CDS, count(*) as n
                    FROM studente s, iscrizione i 
                    WHERE s.matricola = i.matricola 
                    and i.codins = %s
                    and s.CDS != ""
                    group by s.CDS """

        cursor.execute(query, (codins,))

        res = []
        for row in cursor:
            res.append((row["CDS"], row["n"]))

        cursor.close()
        cnx.close()
        return res
