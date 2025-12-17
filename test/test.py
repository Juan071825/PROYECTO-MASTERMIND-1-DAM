import pytest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.generar_codigo_aleatorio import generar_codigo_aleatorio, EMOJIS_COLORES
from src.generar_poblacion_aleatoria import generar_poblacion_aleatoria
from src.introducir_codigo import pedir_codigo_secreto



# TEST 1
@pytest.mark.generar_codigo_aleatorio
def test_generar_codigo_aleatorio():
    resultado = generar_codigo_aleatorio()

    assert isinstance(resultado, str)
    assert len(resultado) > 0  
    assert len(resultado) == 4  

    for emo in resultado:
        assert emo in EMOJIS_COLORES.values()



# TEST 2
@pytest.mark.generar_poblacion_aleatoria
def test_generar_poblacion_aleatoria():
    poblacion = generar_poblacion_aleatoria(5)

    assert isinstance(poblacion, dict)
    assert len(poblacion) == 5

    for key, value in poblacion.items():
        assert key.startswith("individuo")
        assert isinstance(value, str)
        assert len(value) == 4
        for emo in value:
            assert emo in EMOJIS_COLORES.values()


# TEST 3
@pytest.mark.pedir_codigo_secreto
def test_pedir_codigo_secreto():
    colores_simulados = ["rojo", "azul", "morado", "negro"]

    colores, emojis = pedir_codigo_secreto(simulado=colores_simulados)

    assert colores == ["rojo", "azul", "morado", "negro"]
    assert len(emojis) == 4
    for i, color in enumerate(colores):
        assert emojis[i] == EMOJIS_COLORES[color]