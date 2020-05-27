from Instrumento import *
# Trompeta hereda de instrumento e iplementa sus metodos abstractos


class Trompeta (Instrumento):
    def __init__(self):
        super().__init__()
        self.nombre = "Trompeta"

    def prepararInstrumento(self):
        return "/static/trompetaA.jpg "

    def tocarInstrumento(self):
        return "static/trompetaT.jfif "
