import pytest
from hgt.evento import Evento

@pytest.fixture
def evento():
    return Evento(28, 10, 30, 12)

def test_read(tarea):
    assert tarea.read() == "28|&&|10|&&|30|&&|12"

def test_update(tarea):
    tarea.update(28, 11, 30, 11)

    assert tarea.read() == "28|&&|11|&&|30|&&|11"

def test_delete(tarea):
    tarea.delete()
    assert tarea.read() == "None|&&|None|&&|None|&&|None"