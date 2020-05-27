from Acordeon import *
from Guacharaca import *
from Guitarra import *
from Tambores import *
from Trompeta import *


class EquipoMaterial():

    # Se crean objetos de todos los tipos de instrumento
    def __init__(self):
        self.tambor = Tambores()
        self.guacharaca = Guacharaca()
        self.guitarra = Guitarra()
        self.trompeta = Trompeta()
        self.acordeon = Acordeon()
        super().__init__()
    # En este metodo, se añaden todos los objetos a una lista, usamos la palabra reservada
    # para hacer referencia a los objetos creados

    def alistarEquipo(self):
        equipoInst = [self.acordeon, self.guacharaca,
                      self.guitarra, self.tambor, self.trompeta]
        return equipoInst
