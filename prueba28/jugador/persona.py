class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def read(self) ->str:
        return self.nombre
    
    def update(self, nombre):
        self.nombre = nombre

    def delete(self):
        self.nombre = None