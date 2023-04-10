'''
Enunciado: modelar lo siguiente. Una empresa es propietaria de varios edificios y emplea a varios empleados. Un edificio está necesariamente ubicado en una ciudad y una ciudad está formada por varios edificios. Empresa, empleado, ciudad y edificio tienen cada uno un nombre. Estas ciudades incluyen New York, donde se encuentran los edificios A y B, y Los Ángeles, donde está el edificio C. Estos tres edificios son propiedad de YooHoo! que emplea a los Sres. Martin, Salim y la Sra. Xing.

Una vez definidas estas entidades, imagine que su programa es una película estadounidense de catástrofes, en la que se destruye New York. Implemente este evento para que todas las entidades del juego tengan en cuenta las consecuencias de este cataclismo.
'''
#CLASES
class Empleado:
    def __init__(self, nombre, empresa):
        if isinstance(empresa, Empresa):
            self.empresa = empresa
            empresa.empleados.append(self)
        self.nombre = nombre
    def __str__(self):
        return self.nombre

class Edificio:
    def __init__(self, nombre, ciudad, empresa):
        if isinstance(ciudad, Ciudad):
            self.ciudad = ciudad
            ciudad.edificios.append(self)
        if isinstance(empresa, Empresa):
            self.empresa = empresa
            empresa.edificios.append(self)
        self.nombre = nombre
    def __str__(self):
        return self.nombre

class Ciudad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.edificios = []
    def __str__(self):
        return self.nombre
    def __del__(self):
        print("Se destruye la ciudad de " + self.nombre)
        for edificio in self.edificios:
            print("Se destruye el edificio " + edificio.nombre)

class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []
        self.edificios = []
    def __str__(self):
        return self.nombre


#Ciudad
ciudad1 = Ciudad("New York")
ciudad2 = Ciudad("Los Ángeles")

#Empresa
empresa = Empresa("YooHoo!")

#Edificios
edificio1 = Edificio("A", ciudad1, empresa)
edificio2 = Edificio("B", ciudad1, empresa)
edificio3 = Edificio("C", ciudad2, empresa)

#Empleados
empleado1 = Empleado("Martin", empresa)
empleado2 = Empleado("Salim", empresa)
empleado3 = Empleado("Xing", empresa)

