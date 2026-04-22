# 1. Prendo dalla cartella file del pc il file iscritticorsi.sql e lo trascino in dbeaver
# 2. Schiaccio execute sql script e faccio il refresh del local host
# 3. Schiaccio open sql script
# 4. In alto seleziono il db
# 5. Scrivo la query e la copio in DAO
import flet as ft

from UI.controller import Controller
from UI.view import View


def main(page: ft.Page):
    v = View(page)
    c = Controller(v)
    v.set_controller(c)
    v.load_interface()


ft.app(target = main)
