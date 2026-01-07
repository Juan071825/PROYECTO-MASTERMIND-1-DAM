from src.medir_fitness import medir_fitness
from src.parametros_mastermind import EMOJIS_ALELOS, EMOJIS_PINES


# TEST 1 — Coincidencias exactas color y posición correctos
def test_fitness_coincidencia_exacta():
    poblacion = {
        "ind1": [
            EMOJIS_ALELOS["marrón"],
            EMOJIS_ALELOS["azul"],
            EMOJIS_ALELOS["verde"],
            EMOJIS_ALELOS["amarillo"]
        ]
    }

    secreto = [
        EMOJIS_ALELOS["marrón"],
        EMOJIS_ALELOS["azul"],
        EMOJIS_ALELOS["verde"],
        EMOJIS_ALELOS["amarillo"]
    ]

    resultado = medir_fitness(poblacion, secreto)

    individuo, fitness, pines = resultado["ind1"]

    # 4 coincidencias exactas → 4 × 4 puntos = 16
    assert fitness == 16

    # Deben aparecer 4 pines rojos
    assert pines.count(EMOJIS_PINES["rojo"]) == 4



# TEST 2 — Coincidencias parciales color correcto pero posición incorrecta
def test_fitness_coincidencia_parcial():
    poblacion = {
        "ind1": [
            EMOJIS_ALELOS["marrón"],
            EMOJIS_ALELOS["azul"],
            EMOJIS_ALELOS["verde"],
            EMOJIS_ALELOS["amarillo"]
        ]
    }

    secreto = [
        EMOJIS_ALELOS["azul"],
        EMOJIS_ALELOS["verde"],
        EMOJIS_ALELOS["amarillo"],
        EMOJIS_ALELOS["marrón"]
    ]

    resultado = medir_fitness(poblacion, secreto)

    individuo, fitness, pines = resultado["ind1"]

    # 4 coincidencias parciales → 4 × 1 punto = 4
    assert fitness == 4

    # Deben aparecer 4 pines blancos
    assert pines.count(EMOJIS_PINES["blanco"]) == 4



# TEST 3 — Sin coincidencias
def test_fitness_sin_coincidencias():
    poblacion = {
        "ind1": [
            EMOJIS_ALELOS["marrón"],
            EMOJIS_ALELOS["marrón"],
            EMOJIS_ALELOS["marrón"],
            EMOJIS_ALELOS["marrón"]
        ]
    }

    secreto = [
        EMOJIS_ALELOS["azul"],
        EMOJIS_ALELOS["azul"],
        EMOJIS_ALELOS["azul"],
        EMOJIS_ALELOS["azul"]
    ]

    resultado = medir_fitness(poblacion, secreto)

    individuo, fitness, pines = resultado["ind1"]

    assert fitness == 0
    assert pines == []
