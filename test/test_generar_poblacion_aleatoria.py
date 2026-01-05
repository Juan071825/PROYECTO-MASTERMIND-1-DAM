from src.generar_poblacion_aleatoria import generar_poblacion_aleatoria
from src.parametros_mastermind import EMOJIS_ALELOS


def test_generar_poblacion_aleatoria():
    poblacion = generar_poblacion_aleatoria(5)      # Generamos una población de 5 individuos

    assert len(poblacion) == 5                      # Comprobamos que hay exactamente 5 individuos

    for clave, codigo in poblacion.items():         
        assert clave.startswith("individuo")        # La clave debe empezar por "individuo"
        assert len(codigo) == 4                     # Cada código debe tener 4 emojis

        for emoji in codigo:
            assert emoji in EMOJIS_ALELOS.values()  # Cada emoji debe ser válido según EMOJIS_ALELOS


def test_generar_poblacion_claves_unicas():
    poblacion = generar_poblacion_aleatoria(10)     # Generamos una población de 10 individuos

    # Comprobar que todas las claves son únicas
    assert len(poblacion.keys()) == len(set(poblacion.keys()))
