import pytest
from prueba28.jugador.persona import Persona

@pytest.fixture
def persona():
    return Persona('William')

def test_read(persona):
    assert persona.read() == 'William'
