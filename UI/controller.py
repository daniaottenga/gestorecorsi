import flet as ft

from model.model import Model


class Controller:
    def __init__(self, view):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = Model()

    def handlePrintCorsiPD(self, e):
        pass

    def handlePrintIscrittiCorsiPD(self, e):
        pass

    def handlePrintIscrittiCodins(self, e):
        pass

    def handlePrintCDSCodins(self, e):
        pass

    def fillddCodins(self):
        # for cod in self._model.getCodins():
        #     self._view.ddCodins.options.append(
        #         ft.dropdown.Option(cod)
        #     )

        for c in self._model.getAllCorsi():
            self._view.ddCodins.options.append(ft.dropdown.Option(
                key = c.codins,
                data = c,
                on_click = self._choiceDDCodins
            ))
            pass

    def _choiceDDCodins(self, e):
        self._ddCodinsValue = e.control.data
        print(self._ddCodinsValue)