from abc import ABC, abstractmethod

#Creamos la Clase Instrumento que es abstracta con sus metodos respectivos
class Instrumento (ABC):

    def __init__(self):
        pass

    @abstractmethod
    def prepararInstrumento(self):
        pass

    @abstractmethod
    def tocarInstrumento(self):
        pass




