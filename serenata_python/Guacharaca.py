from Instrumento import *
# Guacharaca hereda de instrumento e iplementa sus metodos abstractos


class Guacharaca(Instrumento):

    def __init__(self):
        self.nombre = "Guacharaca"
        super().__init__()

    def prepararInstrumento(self):
        return "static/GuacharacaA.png "

    def tocarInstrumento(self):
        return "static/GuacharacaT.jfif "