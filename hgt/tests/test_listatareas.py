import pytest
from hgt.listatareas import ListaTareas

@pytest.fixture
def lista():
    return ListaTareas()

# Test de la clase ListaTareas
def test_listaTareas0(lista):
    assert len(lista) == 0

def test_listaTareas1(lista):
    lista.agregar('Mates')
    assert len(lista) == 1

def test_listaTarea2(lista):
    lista.agregar('Mates')
    lista.agregar('Lengua')

    assert len(lista) == 2

    assert lista[0] == 'Mates'
    assert lista[1] == 'Lengua'

def test_listaTareaDelete(lista):
    lista.agregar('Informática')
    assert lista[0] == 'Informática'

    del lista[0]
    assert len(lista) == 0

    assert 'Informática' not in lista

def test_listaRead(lista):
    lista.agregar('Mates')
    lista.agregar('Lengua')

    assert lista.read() == 'Mates' + lista.LIMITCHAR + 'Lengua'

def test_listaLoad(lista):
    lista.load('Mates' + lista.LIMITCHAR + 'Lengua')
    assert len(lista) == 2

    assert lista[0] == 'Mates'
    assert lista[1] == 'Lengua'