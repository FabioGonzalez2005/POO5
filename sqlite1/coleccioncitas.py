from db import Db
from cita import Cita

SQLMDLCREATE = '''
    CREATE TABLE IF NOT EXISTS citas (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
   	cita TEXT NOT NULL
)
'''

SQLDDLSELECT = '''
    SELECT * FROM citas
'''

SQLDDLINSERT = '''INSERT INTO citas (cita) VALUES '''
                #Hay que concatenar  ('cita')

SQLDDLUPDATEPART1 = '''UPDATE citas SET cita = "'''
SQLDDLUPDATEPART2 = '''" WHERE id = '''

SQLDDLDELETE = '''DELETE FROM citas WHERE id = '''

SQLDDLSELECT1 = '''SELECT id FROM citas WHERE cita LIKE '''
                #Hay que concatenar



class ColeccionCitas:
    DBNAME = 'citas.db'

    def __init__(self):
        self.con = Db.conectar(self.DBNAME)

        self.con.execute(SQLMDLCREATE)

    def leer(self)->str:
        return self.con.execute(SQLDDLSELECT).fetchall()
    
    def insertar(self, cita):
        if self.buscar(cita) == 0:
            elstr = "('" + str(cita) + "')"
            self.con.execute(SQLDDLINSERT + elstr)

    def actualizar(self, oldCita:str, newCita:str):
        id = self.buscar(oldCita)
        if id != 0 and self.buscar(newCita) == 0:
            elstr = SQLDDLUPDATEPART1 + newCita 
            elstr += SQLDDLUPDATEPART2 + str(id)
            self.con.execute(elstr)

    def borrar(self, cita):
        id = self.buscar(cita) 
        if id != 0:
            self.con.execute(SQLDDLDELETE + str(id))

    def buscar(self, cita:Cita) -> int:
        resultado = 0
        elstr = '"' + str(cita) + '"'
        res = self.con.execute(SQLDDLSELECT1 + elstr)
        reg = res.fetchone()
        if reg != None:
            resultado = reg[0]

        return resultado