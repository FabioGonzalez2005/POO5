import pytest
from hgt.evento import Evento

@pytest.fixture
def evento():
    return Evento("28-10-2024", "10:20", "30-10-2024", "12:00")

def test_read(evento):
    assert evento.read() == "28-10-2024|&&|10:20|&&|30-10-2024|&&|12:00"

def test_update(evento):
    evento.update(28, 11, 30, 11)

    assert evento.read() == "28-10-2024|&&|10:20|&&|30-10-2024|&&|12:00"

def test_delete(evento):
    evento.delete()
    assert evento.read() == "None|&&|None|&&|None|&&|None"