from database.DAO import DAO


class Model:
    def __init__(self):
        pass

    # 5. CHIEDO AL DAO QUELLO CHE MI SERVE
    def getCodins(self):
        return DAO.getCodins()


    def getAllCorsi(self):
        return DAO.getAllCorsi()


    def getCorsiPD(self, pd):
        return DAO.getCorsiPD(pd)


    def getCorsiPDwIscritti(self, pd):
        result = DAO.getCorsiPDwIscritti(pd)
        result.sort(key= lambda s: s[1], reverse=True) # ordinato per numero di iscritti
        return result


    def getStudentiCorso(self, codins):
        studenti = DAO.getStudentiCorso(codins)
        studenti.sort(key=lambda s:s.cognome)
        return studenti


    def getCDSofCorso(self, codins):
        cds = DAO.getCDSofCorso(codins)
        cds.sort(key = lambda c: c[1], reverse=True)
        return cds
