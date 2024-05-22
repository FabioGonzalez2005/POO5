from tarea import Tarea

class Evento(Tarea):
    def __init__(self, fechaInicio, horaInicio, fechaFin, horaFin):
        self.fechaInicio = fechaInicio
        self.horaInicio = horaInicio
        self.fechaFin = fechaFin
        self.horaFin = horaFin

    #Métodos CRUD
    def read(self):
        return f'{fechaInicio}'

    def update(self):
        pass

    def delete(self):
        pass