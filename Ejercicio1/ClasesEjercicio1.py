#Atención a los pacientes de un consultorio médico.

class Paciente:
    def __init__(self, cod, nom, ape):
        self.codigo = cod
        self.nombre = nom
        self.apellido = ape

    def __str__(self):
        return f""" Codigo Paciente: {self.codigo} 
Nombres: {self.nombre}
Apellidos: {self.apellido}"""

class Cola:
    def __init__(self):
        self.elementos = []

    def agregar(self, elem):
        self.elementos.append(elem)
    
    def atender(self):
        try:
            return self.elementos.pop(0)
        except Exception as ex:
            print("Cola vacia, no hay elementos por eliminar", str(ex))
        
    def verificarVacio(self):
        return self.elementos == []