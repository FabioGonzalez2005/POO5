import pytest
from tarea import Tarea

@pytest.fixture
def tarea():
    return Tarea(1, 'Mates', False)

def test_tarea(tarea):
    assert tarea.read() == '1, Mates, False'

def test_read(tarea):
    assert tarea.read() == '1, Mates, False'

def test_update(idNueva, tareaNueva, estadoNuevo):
    idNueva.update('2')
    tareaNueva.update('Lengua')
    estadoNuevo.update('True')

    assert tarea.read() == '2, Lengua, True'

def test_delete(tarea):
    tarea.delete()
    assert tarea.read() == None