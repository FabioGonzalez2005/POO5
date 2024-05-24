from hgt.tarea import Tarea

class Evento(Tarea):
    def __init__(self, fechaInicio:str, horaInicio:str, fechaFin:str, horaFin:str):
        self.fechaInicio = fechaInicio
        self.horaInicio  = horaInicio
        self.fechaFin    = fechaFin
        self.horaFin     = horaFin

    #Métodos CRUD
    def read(self):
        return f'{self.fechaInicio}|&&|{self.horaInicio}|&&|{self.fechaFin}|&&|{self.horaFin}'

    def update(self, fechaInicio:str, horaInicio:str, fechaFin:str, horaFin:str):
        self.fechaInicio = fechaInicio
        self.horaInicio  = horaInicio
        self.fechaFin    = fechaFin
        self.horaFin     = horaFin

    def delete(self):
        self.fechaInicio = None
        self.horaInicio  = None
        self.fechaFin    = None
        self.horaFin     = None