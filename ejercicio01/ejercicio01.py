'''
Enunciado: modelar lo siguiente. Una empresa es propietaria de varios edificios y emplea a varios empleados. Un edificio está necesariamente ubicado en una ciudad y una ciudad está formada por varios edificios. Empresa, empleado, ciudad y edificio tienen cada uno un nombre. Estas ciudades incluyen New York, donde se encuentran los edificios A y B, y Los Ángeles, donde está el edificio C. Estos tres edificios son propiedad de YooHoo! que emplea a los Sres. Martin, Salim y la Sra. Xing.

Una vez definidas estas entidades, imagine que su programa es una película estadounidense de catástrofes, en la que se destruye New York. Implemente este evento para que todas las entidades del juego tengan en cuenta las consecuencias de este cataclismo.
'''
#CLASES

class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.edificios = []
        self.empleados = []

    def agregarEdificio(self, edificio):
        self.edificios.append(edificio)

    def agregarEmpleado(self, empleado):
        self.empleados.append(empleado)

    def __str__(self):
        return self.nombre


class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre


class Ciudad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.edificios = []

    def agregarEdificio(self, edificio):
        self.edificios.append(edificio)
    
    def catastrofe(self):
        print("Catastrofe en", self.nombre)
        for edificio in self.edificios:
            print("Edificio", edificio.nombre, "destruido")
            for empleado in edificio.empleados_edificios:
                print("Empleado", empleado.nombre, "muerto")
    def __str__(self):
        return self.nombre

class Edificio(Ciudad):
    def __init__(self, nombre, ciudad):
        self.nombre = nombre
        self.empleados_edificios = []
        ciudad.agregarEdificio(self) #Agrega el edificio a la ciudad

    def empleados_edificio(self, empleado):
        self.empleados_edificios.append(empleado)

    def __str__(self):
        return self.nombre

#OBJETOS
    #Ciudades
ciudad1 = Ciudad("New York")
ciudad2 = Ciudad("Los Ángeles")

    #Edificios
edificio1 = Edificio("A", ciudad1)
edificio2 = Edificio("B", ciudad1)
edificio3 = Edificio("C", ciudad2)

    #Empleados
empleado1 = Empleado("Martin")
empleado2 = Empleado("Salim")
empleado3 = Empleado("Xing")

    #Agrega los empleados a los edificios correspondientes
edificio1.empleados_edificio(empleado1)
edificio2.empleados_edificio(empleado2)
edificio3.empleados_edificio(empleado3)

    #Empresa
empresa = Empresa("YooHoo!")


ciudad1.catastrofe()
