import flet as ft
from model.model import Model


class Controller:
    def __init__(self, view):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = Model()

        self._ddCodinsValue = None

    # 4. SCRIVO I METODI CHE CHIAMO NELLA VIEW
    def handlePrintCorsiPD(self, e): # inserisco sempre l'evento, è lo schiacciare del pulsante
        self._view.txt_result.controls.clear()

        pd = self._view.ddPD.value

        if pd is None:
            self._view.create_alert("Attenzione, selezionare un periodo didattico.") # crea complessità,
            # valutare se usarlo
            self._view.update_page()
            return

        if pd == "I":
            pdInt = 1
        else:
            pdInt = 2

        corsiPD = self._model.getCorsiPD(pdInt)

        if not len(corsiPD):
            self._view.txt_result.controls.append(
                ft.Text(f"Nessun corso trovato per il {pd} periodo didattico."))
            self._view.update_page()
            return

        self._view.txt_result.controls.append(
            ft.Text(f"Di seguito i corsi del {pd} periodo didattico:"))
        for c in corsiPD:
            self._view.txt_result.controls.append(
                ft.Text(c)
            )
        self._view.update_page()


    def handlePrintIscrittiCorsiPD(self, e):
        self._view.txt_result.controls.clear()

        pd = self._view.ddPD.value

        if pd is None:
            (self._view.create_alert
             ("Attenzione, selezionare un periodo didattico."))
            self._view.update_page()
            return

        if pd == "I":
            pdInt = 1
        else:
            pdInt = 2

        corsi = self._model.getCorsiPDwIscritti(pdInt)

        if not len(corsi):
            self._view.txt_result.controls.append(
                ft.Text(f"Nessun corso trovato per il {pd} periodo didattico."))
            self._view.update_page()
            return

        self._view.txt_result.controls.append(
            ft.Text(f"Di seguito i corsi del {pd} periodo didattico con dettaglio iscritti:"))
        for c in corsi:
            self._view.txt_result.controls.append(
                ft.Text(f"{c[0]} -- N Iscritti: {c[1]}")
            )
        self._view.update_page()


    def handlePrintIscrittiCodins(self, e):
        self._view.txt_result.controls.clear()

        if self._ddCodinsValue is None:
            self._view.create_alert("Per favore selezionare un insegnamento.")
            self._view.update_page()
            return

        #se arriviamo qui, posso recuperare gli studenti
        studenti = self._model.getStudentiCorso(self._ddCodinsValue.codins)

        if not len(studenti):
            self._view.txt_result.controls.append(
                ft.Text("Nessuno studente iscritto a questo corso."))
            self._view.update_page()
            return

        self._view.txt_result.controls.append(
            ft.Text(f"Di seguito gli studenti iscritti al corso {self._ddCodinsValue}")
        )
        for s in studenti:
            self._view.txt_result.controls.append(
                ft.Text(s)
            )
        self._view.update_page()


    def handlePrintCDSCodins(self, e):
        self._view.txt_result.controls.clear()
        if self._ddCodinsValue is None:
            self._view.create_alert("Per favore selezionare un insegnamento.")
            self._view.update_page()
            return

        cds = self._model.getCDSofCorso(self._ddCodinsValue.codins)

        if not len(cds):
            self._view.txt_result.controls.append(
                ft.Text(f"Nessun CDS afferente al corso {self._ddCodinsValue}"))
            self._view.update_page()
            return

        self._view.txt_result.controls.append(
            ft.Text(f"Di seguito i CDS che frequentano il corso {self._ddCodinsValue}"))

        for c in cds:
            self._view.txt_result.controls.append(ft.Text(f"{c[0]} - N Iscritti: {c[1]}"))
        self._view.update_page()


    def fillddCodins(self): # riempe il drop down di cui devo prendere i dati dal db
        for c in self._model.getAllCorsi():
            self._view.ddCodins.options.append(ft.dropdown.Option( # aggiunge al drop down
                key = c.codins, # stringa visualizzata nel menu
                data = c, # a cui associo l'oggetto corso
                on_click = self._choiceDDCodins # attivato quando seleziono l'oggetto, per salvare nel controller
                # la voce selezionata
            ))


    def _choiceDDCodins(self, e): # metodo del controller che associo alla selezione della voce
        self._ddCodinsValue = e.control.data # legge la selezione dell'utente e la salva in una variabile locale,
        # prende l'oggetto di tipo corso selezionato
        print(self._ddCodinsValue)