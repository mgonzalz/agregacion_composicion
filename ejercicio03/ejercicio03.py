'''
En el último ejercicio de la sección sobre la herencia, se mostraron los límites de la herencia múltiple: 
acoplamientos de clases cuyo vínculo no es tan obvio, atajos tomados en el código que tienen mucho riesgo 
de error. Este ejercicio utiliza otro enfoque del problema: la asociación (ya sea composición o 
agregación).
Enunciado: comenzando con el mismo código que el ejercicio sobre herencia múltiple, cree una clase que agrupe el comportamiento común entre las clases Ventana y ParedCortina.
Enunciado: modifique las clases Ventana y ParedCortina para que usen esta nueva clase-interfaz Cristal.
Enunciado: modifique el código para que el programa funcione de nuevo.
'''
from enum import Enum
class Orientacion(Enum):
    NORTE = 'NORTE'
    SUR = 'SUR'
    ESTE = 'ESTE'
    OESTE = 'OESTE'

class Proteccion(Enum):
    PERSIANA = 'PERSIANA'
    ESTOR = 'ESTOR'
    CORTINA = 'CORTINA'


class Pared:
    def __init__(self, orientacion):
        orientacion = orientacion.upper()
        if orientacion == Orientacion(orientacion).name:
            self.orientacion = orientacion
        else:
            raise ValueError('Orientacion no valida')
        self.ventanas = []
    def agregar_ventana(self, ventana):
        self.ventanas.append(ventana)
    def __str__(self):
        return 'Pared: ' + self.orientacion

class Cristal: #CLASE CRISTAL: Agrupa el comportamiento común entre las clases Ventana y ParedCortina
    def __init__(self, superficie, proteccion):
        if isinstance(proteccion, str):
            if proteccion.upper() == Proteccion(proteccion.upper()).name and proteccion != None:
                self.proteccion = proteccion
            else:
                raise Exception('Protección no valida')
        else:
            raise Exception('Protección obligatoria')
        self.superficie = superficie


class Ventana:
    def __init__(self, pared, superficie, proteccion):
        if isinstance(pared, Pared):
            self.pared = pared
            self.pared.agregar_ventana(self)
        else:
            raise ValueError('La ventana debe estar en una pared')
        Cristal.__init__(self, superficie, proteccion) #(self, superficie, proteccion)

class ParedCortina(Pared, Cristal):
    def __init__(self, orientacion, superficie):
        Pared.__init__(self, orientacion) #(self, orientacion)
        Cristal.__init__(self, self, superficie) #(self, pared, superficie) la pared es la misma que la de la clase padre

    def __str__(self):
        return 'Pared cortina: ' + self.orientacion

class Casa:
    def __init__(self, paredes):
        if isinstance(paredes, list):
            self.paredes = paredes
        else:
            raise Exception('Protección obligatoria')

    def superficie_acristalada(self):
        superficie = 0
        for pared in self.paredes:
            for ventana in pared.ventanas:
                superficie += ventana.superficie
        return superficie


# Instanciación de las paredes
pared_norte = Pared("NORTE") 
pared_oeste = Pared("OESTE") 
pared_sur = Pared("SUR")
pared_este = Pared("ESTE")

# Instanciación de las ventanas
ventana_norte = Ventana(pared_norte, 0.5, "Persiana") 
ventana_oeste = Ventana(pared_oeste, 1, "Estor")
ventana_sur = Ventana(pared_sur, 2, "Cortina") 
ventana_este = Ventana(pared_este, 1, "Persiana")
casa = Casa([pared_norte, pared_oeste, pared_sur, pared_este]) 
print(casa.superficie_acristalada()) #4,5

