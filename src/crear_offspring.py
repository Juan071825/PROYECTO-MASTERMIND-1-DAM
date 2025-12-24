import random
from src.parametros_mastermind import ALELOS_ELEGIBLES, EMOJIS_ALELOS
from src.selector_padres import selector_padres

def crear_offspring(progenitores):

    UNO = 1

    
    lista_hijos = []
    
    while len(lista_hijos) < 25:

        pareja_seleccionada = random.choices(
            population= list(progenitores.keys()),
            k= 2
        )

        padre = progenitores[pareja_seleccionada[0]][0]
        madre = progenitores[pareja_seleccionada[1]][0]

        punto_cruce = random.randint(1, 3)

        hijo = padre[:punto_cruce] + madre[punto_cruce:]
        lista_hijos.append(hijo)

        diccionario_hijos = {}
        for hijo in lista_hijos:
            diccionario_hijos['hijo' + str(lista_hijos.index(hijo) + UNO)] = hijo

    return diccionario_hijos