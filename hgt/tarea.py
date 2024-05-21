class Tarea:
    def __init__(self, id:int, tarea:str, estado:bool) -> None:
        self.id     = id
        self.tarea  = tarea
        self.estado = estado

    #Métodos CRUD
    def read(self)->str:
        return self.tarea

    def update(self, tarea)->None:
        self.tarea = tarea
        
    def delete(self):
        self.tarea = None