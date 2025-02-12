class Persona:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Telefono: {self.telefono}"
    

class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, persona):
        self.contactos.append(persona)

    def mostrar_contacts(self):
        for p in self.contactos:
            print(p.mostrar_informacion())


agenda = Agenda()

persona1 = Persona("John Doe", "555-55-55")
persona2 = Persona("Jane Doe", "555-55-55")

agenda.agregar_contacto(persona1)
agenda.agregar_contacto(persona2)

agenda.mostrar_contacts()

