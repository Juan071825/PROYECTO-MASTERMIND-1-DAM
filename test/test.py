import pytest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.generar_codigo_aleatorio import generar_codigo_aleatorio, EMOJIS_COLORES
from src.generar_poblacion_aleatoria import generar_poblacion_aleatoria
from src.introducir_codigo import pedir_codigo_secreto


# Test 1 generar_codigo_aleatorio

@pytest.mark.generar_codigo_aleatorio
def test_generar_codigo_aleatorio():
    resultado = generar_codigo_aleatorio()

    assert len(resultado) == 4

    for emoji in resultado:
        assert emoji in EMOJIS_COLORES.values()


# Test 2 generar_codigo_aleatorio

@pytest.mark.generar_codigo_aleatorio
def test_generar_codigo_aleatorio_no_vacio():
    resultado = generar_codigo_aleatorio()
    assert resultado != ""



# Test 1 generar_poblacion_aleatoria

@pytest.mark.generar_poblacion_aleatoria
def test_generar_poblacion_aleatoria():
    poblacion = generar_poblacion_aleatoria(5)

    assert len(poblacion) == 5

    for clave, codigo in poblacion.items():
        assert clave.startswith("individuo")
        assert len(codigo) == 4
        for emoji in codigo:
            assert emoji in EMOJIS_COLORES.values()


# Test 2 generar_poblacion_aleatoria

@pytest.mark.generar_poblacion_aleatoria
def test_generar_poblacion_claves_unicas():
    poblacion = generar_poblacion_aleatoria(10)
    assert len(poblacion.keys()) == len(set(poblacion.keys()))


# Test 1 pedir_codigo_secreto

@pytest.mark.pedir_codigo_secreto
def test_pedir_codigo_secreto():
    colores_simulados = ["rojo", "azul", "morado", "negro"]

    colores, emojis = pedir_codigo_secreto(simulado=colores_simulados)

    assert colores == colores_simulados
    assert len(emojis) == 4

    for posicion in range(4):
        assert emojis[posicion] == EMOJIS_COLORES[colores[posicion]]


# Test 2 pedir_codigo_secreto

@pytest.mark.pedir_codigo_secreto
def test_pedir_codigo_secreto_longitud():
    colores_simulados = ["verde", "azul", "amarillo", "negro"]

    colores, emojis = pedir_codigo_secreto(simulado=colores_simulados)

    assert len(colores) == 4
    assert len(emojis) == 4
