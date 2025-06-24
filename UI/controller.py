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
        self._model.buildGraph(self._annoScelto, self._formaScelta)
        n,a = self._model.getGraphDetails()
        self._view.txt_result1.clean()
        self._view.txt_result1.controls.append(ft.Text(f"Numero di vertici: {n}"))
        self._view.txt_result1.controls.append(ft.Text(f"Numero di archi: {a}"))
        self._view.txt_result1.controls.append(ft.Text("I 5 archi di peso maggiore sono:"))
        archiPesoMax = self._model.archiPesoMaggiore()
        for arcoMax in archiPesoMax:
            self._view.txt_result1.controls.append(ft.Text(arcoMax))
        self._view.update_page()

    def handle_path(self, e):
        pass

    def _sceltaAnno(self, e):
        self._annoScelto = e.control.data
        print(f"selezionato {self._annoScelto}")

    def _sceltaForma(self, e):
        self._formaScelta = e.control.data
        print(f"selezionata {self._formaScelta}")