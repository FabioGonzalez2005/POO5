class Tarea:
    def __init__(self, id:int, tarea:str, estado:bool) -> None:
        self.id     = id
        self.tarea  = tarea
        self.estado = estado

    #Métodos CRUD
    def read(self)->str:
        return f'{self.id}|&&|{self.tarea}|&&|{self.estado}'

    def update(self, idNueva:int, tareaNueva:str, estadoNuevo:bool)->None:
        self.id     = idNueva
        self.tarea  = tareaNueva
        self.estado = estadoNuevo
        
    def delete(self):
        self.id     = None
        self.tarea  = None
        self.estado = None