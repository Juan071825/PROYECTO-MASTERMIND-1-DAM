import random
from src.medir_fitness import medir_fitness
from src.parametros_mastermind import PORCETAJE_DEFUNCION


def selector_padres():

    UNO = 1
    poblacion = medir_fitness()
    numero_padres = int(len(poblacion) * (UNO -PORCETAJE_DEFUNCION))

    keys = list(poblacion.keys())
    lista_fitness = [poblacion[key][1] for key in keys]

    pesos = []
    for fitness in lista_fitness:
        pesos.append(fitness + UNO)



    padres_seleccionados = random.choices(
        population=keys, 
        weights=pesos,
        k=numero_padres
    )

    padres_seleccionados = set(padres_seleccionados)

    while len(padres_seleccionados) < numero_padres:
        padres_seleccionados.add(random.choices(population=keys, weights=pesos, k=1)[0] )
        #[0] para impedir que metas una lista dentro de un set.
        

    return {key: poblacion[key] for key in padres_seleccionados}

