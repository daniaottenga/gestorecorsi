import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Gestore Corsi - Edizione 2026" # nel titolo della finestra del sistema operativo
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None

        # 1. DEFINISCO GLI ATTRIBUTI NEL COSTRUTTORE
        self.ddPD = None # drop down periodo didattico, menu a tendina
        self.ddCodins = None # drop down codice insegnamento
        self.btnPrintCorsiPD = None # print corsi periodo didattico
        self.btnPrintIscrittiCorsiPD = None # print numero iscritti dei corsi del periodo didattico
        self.btnPrintIscrittiCodins = None # print iscritti corsi del codice inserito
        self.btnPrintCDSCodins = None # print corsi di laurea del codice inserito
        self.txt_result = None


    def load_interface(self):
        # 2. CAMBIO TITOLO
        self._title = ft.Text("Gestore Corsi - Edizione 2026", color="blue", size=24) # titolo visibile
        # nella pagina
        self._page.controls.append(self._title)

        # 3. CREO LE RIGHE
        self.ddPD = ft.Dropdown(label="Periodo Didattico",
                                options = [ft.dropdown.Option("I"), ft.dropdown.Option("II")], # lista di opzioni
                                width=200) # crea un menu a tendina
        # con .value ho il valore di cosa ho scelto
        self.btnPrintCorsiPD = ft.ElevatedButton(text="Stampa Corsi",
                                                 on_click=self._controller.handlePrintCorsiPD,
                                                 width=300)
        self.btnPrintIscrittiCorsiPD = ft.ElevatedButton(text="Stampa numero iscritti",
                                                 on_click=self._controller.handlePrintIscrittiCorsiPD,
                                                 width=300)
        row1 = ft.Row([self.ddPD, self.btnPrintCorsiPD, self.btnPrintIscrittiCorsiPD],
                      alignment=ft.MainAxisAlignment.CENTER)

        self.ddCodins = ft.Dropdown(label = "Corso", width=200) # le opzioni dei corsi non le so in questa fase,
        # le devo leggere dal database, il controller farà una query dove chiede al database e riempe il dropdown
        self._controller.fillddCodins() # aggiunge le opzioni
        self.btnPrintIscrittiCodins = ft.ElevatedButton(text = "Stampa iscritti al corso",
                                                        on_click = self._controller.handlePrintIscrittiCodins,
                                                        width=300)
        self.btnPrintCDSCodins = ft.ElevatedButton(text = "Stampa CDS afferenti", # tutti i corsi iscritti al
                                                   # codice insegnamento
                                                   on_click = self._controller.handlePrintCDSCodins,
                                                   width=300)
        row2 = ft.Row([self.ddCodins, self.btnPrintIscrittiCodins, self.btnPrintCDSCodins],
                      alignment=ft.MainAxisAlignment.CENTER)

        self._page.add(row1, row2)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
