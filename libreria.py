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


    

# Creamos una instancia de la clase Libro
libro1 = Libro("El Gran Gatsby", "Fitzgerald")
libro2 = Libro("Cien años de soledad", "Gabriel Garcia Marquez")

#print(libro1.titulo)
#print(libro1.mostrar_info())
#print(libro2.autor)

biblioteca = Biblioteca("Biblioteca Andres Bello")
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

print("------------------------------------------")
print("Mostrando el contenido de la biblioteca")

biblioteca.mostrar_libros()