
import flet as ft

from UI.controller import Controller
from UI.view import View


def main(page: ft.Page):
    v = View(page)
    c = Controller(v)
    v.set_controller(c)
    v.load_interface()


ft.app(target = main)
