import pytest
from calculadora import sumar, restar, multiplicar, dividir


def test_sumar_dos_numeros():
    assert sumar(2, 3) == 5


def test_restar_dos_numeros():
    assert restar(10, 4) == 6


def test_multiplicar_dos_numeros():
    assert multiplicar(3, 5) == 15


def test_dividir_dos_numeros():
    assert dividir(10, 2) == 5


def test_dividir_por_cero_lanza_error():
    with pytest.raises(ValueError):
        dividir(10, 0)