import sqlite3


SQLMDLCREATE = '''
    CREATE TABLE IF NOT EXISTS citas (
    id INTEGER PRIMARY KEY AUTOINCREMENT
    cita TEXT NOT NULL
)
'''

con = sqlite3.connect('citas.db')

con.close()