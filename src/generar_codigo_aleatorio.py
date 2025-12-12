import random

from src.parametros_mastermind import COLORES_ELEGIBLES, EMOJIS_COLORES

def generar_codigo_aleatorio():
    
    codigo_aleatorio = []

    while len(codigo_aleatorio) < 4:
        codigo_aleatorio.append(random.choice(COLORES_ELEGIBLES))

    
    emojis_codigo_aleatorio = []
    for ficha in codigo_aleatorio:
        emojis_codigo_aleatorio.append(EMOJIS_COLORES[ficha])
    return ''.join(emojis_codigo_aleatorio)

