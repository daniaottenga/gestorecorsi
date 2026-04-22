from dataclasses import dataclass

# 7. CREO IL MODELLO CORSO E I SUOI EQ, HASH, E STR
@dataclass
class Corso: # prendo i campi in base a quelli che ci sono nel database
    codins: str # vedo le proprietà dal db
    crediti: int
    nome: str
    pd: int


    def __eq__(self, other):
        return self.codins == other.codins # compara le chiavi primarie


    def __hash__(self):
        return hash(self.codins) # return della chiave primaria


    def __str__(self):
        return f"{self.nome} ({self.codins}) - {self.crediti} CFU"