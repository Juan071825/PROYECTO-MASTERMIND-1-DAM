import random

from src.parametros_mastermind import ALELOS_ELEGIBLES, EMOJIS_ALELOS

def generar_codigo_aleatorio():
    
    cromosoma_aleatorio = []

    while len(cromosoma_aleatorio) < 4:
        cromosoma_aleatorio.append(random.choice(ALELOS_ELEGIBLES))

    
    emojis_cromosoma_aleatorio = []
    for alelo in cromosoma_aleatorio:
        emojis_cromosoma_aleatorio.append(EMOJIS_ALELOS[alelo])
    return list(emojis_cromosoma_aleatorio)

