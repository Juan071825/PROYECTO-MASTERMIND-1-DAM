from src.generar_poblacion_aleatoria import generar_poblacion_aleatoria
from src.parametros_mastermind import EMOJIS_ALELOS


def test_generar_poblacion_aleatoria():
    poblacion = generar_poblacion_aleatoria(5)

    assert len(poblacion) == 5

    for clave, codigo in poblacion.items():
        assert clave.startswith("individuo")
        assert len(codigo) == 4
        for emoji in codigo:
            assert emoji in EMOJIS_ALELOS.values()


# Test 2 

def test_generar_poblacion_claves_unicas():
    poblacion = generar_poblacion_aleatoria(10)
    assert len(poblacion.keys()) == len(set(poblacion.keys()))