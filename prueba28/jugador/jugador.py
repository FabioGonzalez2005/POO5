from prueba28.jugador.persona import Persona

class Jugador(Persona):
    def __init__(self, nombre, deporte):
        super().__init__(nombre)
        self.deporte = deporte

    def read(self)->str:
        return super().read() + ',' + self.deporte