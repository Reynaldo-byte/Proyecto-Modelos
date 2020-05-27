from random import randint, uniform, random


class Operacion():
    def __init__(self):
        self.numero = 0
        super().__init__()

    # Con este metodo se genera un numero al azar de musicos
    def generarNumeroMusicos(self):
        self.numero = randint(4, 9)
        return self.numero

    # Con este metodo se genera un numero al azar para escoger el instrumento al azar
    def escogerInstrumento(self):
        self.numero = randint(0, 4)
        return self.numero
