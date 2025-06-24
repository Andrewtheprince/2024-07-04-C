import flet as ft
from UI.view import View
from model.modello import Model


class Controller:
    def __init__(self, view: View, model: Model):
        self._formaScelta = None
        self._view = view
        self._model = model
        self._annoScelto = None

    def fillYear(self):
        anni = self._model.getAnni()
        for anno in anni:
            self._view.ddyear.options.append(ft.dropdown.Option(key = anno, data = anno, on_click=self._sceltaAnno))
        self._view.update_page()

    def fillShape(self, e):
        shape = self._model.getShape(self._annoScelto)
        for forma in shape:
            self._view.ddshape.options.append(ft.dropdown.Option(key=forma, data = forma, on_click=self._sceltaForma))
        self._view.update_page()

    def handle_graph(self, e):
        pass

    def handle_path(self, e):
        pass

    def _sceltaAnno(self, e):
        self._annoScelto = e.control.data
        print(f"selezionato {self._annoScelto}")

    def _sceltaForma(self, e):
        self._formaScelta = e.control.data
        print(f"selezionata {self._formaScelta}")