from EquipoMaterial import *
from Operacion import *


class Personal():

    def __init__(self):
        self.azarInst = 0  # Este "azarInst" nos ayuda a escoger instrumentos al azar de listaEquipo

        # Este "numero" nos ayuda a saber la cantidad de musicos
        self.numero = Operacion()
        self.listaEquipo = EquipoMaterial().alistarEquipo()
        self.equipoEscogido = []
        super().__init__()

    # Como el numero de musicos es aleatorio recorremos un for del tamaño del numero de musicos(0-9)
    # y aleatoriamente asignamos instrumentos con azarInst

    def asignarInstrumentos(self):
        for i in range(self.numero.generarNumeroMusicos()):
            self.azarInst = Operacion().escogerInstrumento()
            self.equipoEscogido.insert(i, self.listaEquipo[self.azarInst])

        return self.equipoEscogido

    # Este metodo imprime la lista obtenida en asignarInstrumentos() imprimiendo los metodos de preparar
    # y tocar
    def numeroMusicos(self):
        self.listaMetodo = self.asignarInstrumentos()
        return (len(self.listaMetodo))
    def compadreAfinemos(self):
        
        
            return self.listaMetodo
    def compadreEmpezemosaTocar(self):  
        return self.listaMetodo
