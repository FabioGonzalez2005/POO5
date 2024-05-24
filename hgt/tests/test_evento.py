import pytest
from hgt.evento import Evento

@pytest.fixture
def evento():
    return Evento(1, "Mates", False, "28-10-2024", "10:20", "30-10-2024", "12:00")

def test_read(evento):
    assert evento.read() == "1|&&|Mates|&&|False|&&|28-10-2024|&&|10:20|&&|30-10-2024|&&|12:00"

def test_update(evento):
    evento.update(1, "Mates II", False, "29-10-2024", "11:20", "31-10-2024", "13:00")

    assert evento.read() == "1|&&|Mates II|&&|False|&&|29-10-2024|&&|11:20|&&|31-10-2024|&&|13:00"

def test_delete(evento):
    evento.delete()
    assert evento.read() == "None|&&|None|&&|None|&&|None|&&|None|&&|None|&&|None"