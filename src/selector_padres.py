import random
from src.parametros_mastermind import PORCETAJE_DEFUNCION


def selector_padres(poblacion):
    UNO = 1
    numero_padres = int(len(poblacion) * (UNO -PORCETAJE_DEFUNCION))

    poblacion_restante = poblacion.copy()
    padres_seleccionados = {}

    while len(padres_seleccionados) < numero_padres:
        keys = list(poblacion_restante.keys())
        lista_fitness = [poblacion_restante[key][1] for key in keys]

        pesos = []
        for fitness in lista_fitness:
            pesos.append(fitness + UNO)

        seleccionado = random.choices(keys, weights=pesos, k=1)[0]

        padres_seleccionados[seleccionado] = poblacion_restante[seleccionado]
        del poblacion_restante[seleccionado]

    return padres_seleccionados

