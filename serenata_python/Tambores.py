from Instrumento import *
# Tambores hereda de instrumento e iplementa sus metodos abstractos


class Tambores (Instrumento):

    def __init__(self):
        self.nombre = "Tambores"
        super().__init__()

    def prepararInstrumento(self):
        return "static/tamborA.jpg "

    def tocarInstrumento(self):
        return "static/TamborT.jpg"
