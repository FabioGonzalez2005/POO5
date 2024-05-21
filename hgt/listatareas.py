from hgt.tarea import Tarea

class ListaTareas:
    LIMITCHAR = "|&&|"

    def __init__(self, lista=None):
        if lista is None:
            self.tareas = []
        else:
            self.tareas = lista

    def agregar(self, tarea:Tarea):
        self.tareas.append(tarea)

    def read(self):
        result = ""
        for tarea in self.tareas:
            result += tarea
            if tarea != self.tareas[-1]:
                result += self.LIMITCHAR
        return result
    
    def load(self, data:str):
        tareas = data.split(self.LIMITCHAR)
        for tarea in tareas:
            self.tareas.append(tarea)
    
    def update(self, tarea:Tarea, nombre:str):
        for a in self.tareas:
            if a == tarea:
                a.update(nombre)
                break

    def delete(self, tarea:Tarea):
        for a in self.tareas:
            if a == tarea:
                a.delete()
                break

    def __str__(self):
        return self.read()
    
    def __len__(self):
        return len(self.tareas)
    
    def __getitem__(self, index):
        return self.tareas[index]
    
    def __setitem__(self, index, value):
        self.tareas[index] = value

    def __delitem__(self, index):
        del self.tareas[index]

    def __iter__(self):
        return iter(self.tareas)
    
    def __contains__(self, item):
        return item in self.tareas
    
    def __eq__(self, other):
        return self.tareas == other.tareas
    
    def __ne__(self, other):
        return self.tareas != other.tareas
