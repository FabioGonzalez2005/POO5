import sqlite3

SQLMDLCREATE = '''
    CREATE TABLE IF NOT EXISTS citas (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
   	cita TEXT NOT NULL
)
'''

#con = sqlite3.connect('citas.db', isolation_level = None)
con = sqlite3.connect('citas.db', autocommit=True)

con.execute(SQLMDLCREATE)

SQLDDLINSERT = '''
    INSERT INTO citas (cita) VALUES ('La vida es bella')
'''

con.execute(SQLDDLINSERT)
#con.commit()

SQLDDLSELECT = '''
    SELECT * FROM citas
'''

res = con.execute(SQLDDLSELECT)
print(res.fetchall())

con.close()