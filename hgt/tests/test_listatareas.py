import pytest
from hgt.listatareas import ListaTareas

@pytest.fixture
def lista():
    return ListaTareas()

# Test de la clase ListaTareas
def test_listaTareas0(lista):
    assert len(lista) == 0

def test_listaTareas1(lista):
    lista.agregar('Juan')
    assert len(lista) == 1

def test_listaAlumno2(lista):
    lista.agregar('Juan')
    lista.agregar('Pedro')

    assert len(lista) == 2

    assert lista[0] == 'Juan'
    assert lista[1] == 'Pedro'

def test_listaAlumnoDelete(lista):
    lista.agregar('Luis')
    assert lista[0] == 'Luis'

    del lista[0]
    assert len(lista) == 0

    assert 'Luis' not in lista

def test_listaRead(lista):
    lista.agregar('Juan')
    lista.agregar('Pedro')

    assert lista.read() == 'Juan' + lista.LIMITCHAR + 'Pedro'

def test_listaLoad(lista):
    lista.load('Juan' + lista.LIMITCHAR + 'Pedro')
    assert len(lista) == 2

    assert lista[0] == 'Juan'
    assert lista[1] == 'Pedro'