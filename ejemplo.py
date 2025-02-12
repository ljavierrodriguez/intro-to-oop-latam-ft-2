# definiendo la clase Libro
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def mostrar_info(self):
        return f"Titulo: {self.titulo}, Autor: {self.autor}"

# definiendo la clase Biblioteca 
class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        return f"Libro {libro.titulo} agregado..."
    
    def mostrar_libros(self):
        print(f"Libros en la Biblioteca {self.nombre}:")
        print("________")
        for libro in self.libros:
            print(libro.mostrar_info())

b = Biblioteca("4Geeks")

# capturar el numero de libros a ingresar
# cantidad = int(input("Ingrese el numero de libros a ingresar:\n"))
'''
for x in range(cantidad):
    titulo = input("Ingrese titulo:\n")
    autor = input("Ingrese autor:\n")
    l = Libro(titulo, autor)
    b.agregar_libro(l)
'''
seguir = True
while seguir:
    titulo = input("Ingrese titulo:\n")
    autor = input("Ingrese autor:\n")
    l = Libro(titulo, autor)
    b.agregar_libro(l)
    opcion = input("Desea Agregar otro Libro y/n:")
    if  opcion.lower() == 'y':
        seguir = True
    else:
        seguir = False 

b.mostrar_libros()

