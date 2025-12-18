import random
from src.medir_fitness import registrar_fitness
from src.parametros_mastermind import PORCETAJE_DEFUNCION


def selector_padres():
    poblacion = registrar_fitness()
    numero_padres = int(len(poblacion)*(1-PORCETAJE_DEFUNCION))

    keys = list(poblacion.keys())
    lista_fitness = [poblacion[key][1] for key in keys]

    pesos = []
    for fitness in lista_fitness:
        pesos.append(fitness + 1)



    padres_seleccionados = random.choices(
        population=keys, 
        weights=pesos,
        k=numero_padres
    )

    return print(len({key: poblacion[key] for key in padres_seleccionados})), print({key: poblacion[key] for key in padres_seleccionados})

selector_padres()

