import random
from src.parametros_mastermind import ALELOS_ELEGIBLES, EMOJIS_ALELOS, PROBABILIDAD_MUTACION


def crear_offspring(progenitores):

    UNO = 1

    lista_hijos = []
    diccionario_hijos = {}

    while len(lista_hijos) < 25:

        pareja_seleccionada = random.choices(
            population=list(progenitores.keys()),
            k=2
        )

        padre = progenitores[pareja_seleccionada[0]][0]
        madre = progenitores[pareja_seleccionada[1]][0]

        punto_cruce = random.randint(1, 3)

        hijo = padre[:punto_cruce] + madre[punto_cruce:]
        hijo = generar_mutacion(hijo, PROBABILIDAD_MUTACION)
        lista_hijos.append(hijo)

        diccionario_hijos[f"hijo{len(lista_hijos)}"] = hijo   # ← FIX IMPORTANTE

    return diccionario_hijos


def generar_mutacion(hijo, probabilidad_mutacion):

    if random.random() < probabilidad_mutacion:
        index_alelo_mutado = random.randint(0, 3)
        nuevo_alelo = random.choice(ALELOS_ELEGIBLES)
        hijo[index_alelo_mutado] = EMOJIS_ALELOS[nuevo_alelo]
    return hijo
