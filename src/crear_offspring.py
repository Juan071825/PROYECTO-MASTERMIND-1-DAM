import random
from src.parametros_mastermind import ALELOS_ELEGIBLES, EMOJIS_ALELOS, PROBABILIDAD_MUTACION, NUMERO_HIJOS

def crear_offspring(progenitores):

    UNO = 1

    lista_hijos = []
    diccionario_hijos = {}
    progenitores_lista = list(valores[0] for valores in progenitores.values())

    while len(lista_hijos) < NUMERO_HIJOS:

        
        padre, madre = random.sample(progenitores_lista, 2)
        hijo = []

        if random.random() < 0.7:
            punto_corte = random.randint(1,3)
            hijo = padre[:punto_corte] + madre[punto_corte:]
        else:
            hijo = [random.choice([padre[alelo], madre[alelo]]) for alelo in range(4)]

        hijo_mutado = generar_mutacion(hijo, PROBABILIDAD_MUTACION)
        lista_hijos.append(hijo_mutado)


    for index, hijo in enumerate(lista_hijos, start=0):
        diccionario_hijos['hijo' + str(index)] = hijo

    return diccionario_hijos


def generar_mutacion(hijo, probabilidad_mutacion):

    for alelo in range(len(hijo)):
        if random.random() < probabilidad_mutacion:
            hijo[alelo] = random.choice(list(EMOJIS_ALELOS.values()))
    return hijo
