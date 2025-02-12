class Persona:
    def __init__(self, nombre, apellido) -> None:
        self.nombre = nombre
        self.apellido = apellido

    def saludar(self):
        return f"Hola, soy {self.nombre} {self.apellido}"
    

class Estudiante(Persona):
    def __init__(self, nombre, apellido, grado):
        super().__init__(nombre, apellido)
        self.grado = grado

    def saludar(self):
        return f"Hola, soy el estudiante {self.nombre} {self.apellido} y estoy en {self.grado}"

persona = Persona("Luis", "Rodriguez")

print(persona.saludar())


estudiante = Estudiante("John", "Doe", "3ro")

print(estudiante.saludar())