class Libro:
    def __init__(self, tit, aut, edi):
        self.titulo = tit
        self.autor = aut
        self.edicion = edi

    def __str__(self):
        return f"""Titulo: {self.titulo}
Autor: {self.autor}
Edicion: {self.edicion}"""

pila = []

def menu():
    print("PIla de Libros")
    print("1. Agregar Libro")
    print("2. Remover Libro")
    print("3. Mostrar Libro")
    print("4. Salir")
    op = int(input("Digite su opcion...  "))
    return op

def agregarLibro():
    tit = input("Titulo: ")
    aut = input("Autor: ")
    edi = int(input("Edicion: "))
    pila.append(Libro(tit, aut, edi))
    print("Libro agregado")

def removerLibro():
    libro = pila.pop()
    print(libro)
    print("Libro removido")

def mostrarLibro():
    for elem in pila:
        print(elem)

def main():
    op = 0
    while(op != 4):
        op = menu()
        if(op==1): agregarLibro()
        elif(op==2): removerLibro()
        elif(op==3): mostrarLibro()
        elif(op==4): print("Ciao, ciao...")
        else: print("Opcion invalida...")

main()
