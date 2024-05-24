from hgt.tarea import Tarea

class Evento(Tarea):
    def __init__(self, id:int, tarea:str, estado:bool, fechaInicio:str, horaInicio:str, fechaFin:str, horaFin:str):
        super().__init__(id, tarea, estado)
        self.fechaInicio = fechaInicio
        self.horaInicio  = horaInicio
        self.fechaFin    = fechaFin
        self.horaFin     = horaFin

    #Métodos CRUD
    def read(self):
        infoTarea = super().read()
        return f'{infoTarea}|&&|{self.fechaInicio}|&&|{self.horaInicio}|&&|{self.fechaFin}|&&|{self.horaFin}'

    def update(self, idNueva:int, tareaNueva:str, estadoNuevo:bool, fechaInicio:str, horaInicio:str, fechaFin:str, horaFin:str):
        super().update(idNueva, tareaNueva, estadoNuevo)
        self.fechaInicio = fechaInicio
        self.horaInicio  = horaInicio
        self.fechaFin    = fechaFin
        self.horaFin     = horaFin

    def delete(self):
        self.fechaInicio = None
        self.horaInicio  = None
        self.fechaFin    = None
        self.horaFin     = None