from src.medir_fitness import medir_fitness
from src.parametros_mastermind import EMOJIS_ALELOS



# TEST 1 — Coincidencias exactas color y posición correctos


def test_fitness_coincidencia_exacta():
    # Población con un único individuo que coincide EXACTAMENTE con el secreto
    poblacion = {
        "ind1": [
            EMOJIS_ALELOS["rojo"],
            EMOJIS_ALELOS["azul"],
            EMOJIS_ALELOS["verde"],
            EMOJIS_ALELOS["amarillo"]
        ]
    }

    # Código secreto idéntico al individuo
    secreto = [
        EMOJIS_ALELOS["rojo"],
        EMOJIS_ALELOS["azul"],
        EMOJIS_ALELOS["verde"],
        EMOJIS_ALELOS["amarillo"]
    ]

    resultado = medir_fitness(poblacion, secreto)

    individuo, fitness, pines = resultado["ind1"]

    # 4 coincidencias exactas → 4 × 2 puntos = 8
    assert fitness == 8

    # Deben aparecer 4 pines rojos 
    assert pines.count(EMOJIS_ALELOS["rojo"]) == 4




# TEST 2 — Coincidencias parciales color correcto pero posición incorrecta


def test_fitness_coincidencia_parcial():
    # Individuo con los mismos colores que el secreto pero todos los colores estan en orden incorrecta
    poblacion = {
        "ind1": [
            EMOJIS_ALELOS["rojo"],
            EMOJIS_ALELOS["azul"],
            EMOJIS_ALELOS["verde"],
            EMOJIS_ALELOS["amarillo"]
        ]
    }

    # Mismos colores, pero desplazados → todo es coincidencia parcial
    secreto = [
        EMOJIS_ALELOS["azul"],
        EMOJIS_ALELOS["verde"],
        EMOJIS_ALELOS["amarillo"],
        EMOJIS_ALELOS["rojo"]
    ]

    resultado = medir_fitness(poblacion, secreto)

    individuo, fitness, pines = resultado["ind1"]

    # 4 coincidencias parciales → 4 × 1 punto = 4
    assert fitness == 4

    # Deben aparecer 4 pines blancos
    assert pines.count(EMOJIS_ALELOS["blanco"]) == 4




# TEST 3 — Sin coincidencias

def test_fitness_sin_coincidencias():
    poblacion = {
        "ind1": [
            EMOJIS_ALELOS["rojo"],
            EMOJIS_ALELOS["rojo"],
            EMOJIS_ALELOS["rojo"],
            EMOJIS_ALELOS["rojo"]
        ]
    }

    # Secreto con 4 azules ningún color coincide
    secreto = [
        EMOJIS_ALELOS["azul"],
        EMOJIS_ALELOS["azul"],
        EMOJIS_ALELOS["azul"],
        EMOJIS_ALELOS["azul"]
    ]

    resultado = medir_fitness(poblacion, secreto)

    individuo, fitness, pines = resultado["ind1"]

    assert fitness == 0

    # No debe haber pines
    assert pines == []
