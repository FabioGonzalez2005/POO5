class Cita:
    def __init__(self, cita:str) -> None:
        self.cita = cita

    def __str__(self) -> str:
        return self.cita
    
    def leer(self) -> str:
        return self.cita