#Atención a los pacientes de un consultorio médico.
import ClasesEjercicio1 as c
cola = c.Cola()
cod = 1

def menu():
        print("1. Agregar Paciente")
        print("2. Atender Paciente")
        print("3. Mostrar Pacientes")
        print("4. Salir")
        op = int(input("Digite su opcion...  "))
        return op

def agregarPaciente():
    global cod
    nom = input("Nombres: ")
    ape = input("Apellidos: ")
    paciente = c.Paciente(cod, nom, ape)
    cod += 1
    try:
        cola.agregar(paciente)
    except Exception as ex:
        print(str(ex))

def atenderPaciente():
    print(cola.atender())

def mostrarPaciente():
    for paciente in cola.elementos:
        print(paciente)

def main():
    op = 0
    while(op != 4):
        op = menu()
        if(op==1): agregarPaciente()
        elif(op==2): atenderPaciente()
        elif(op==3): mostrarPaciente()
        elif(op==4): print("Ciao, ciao...")
        else: print("Opcion invalida...")

main()

