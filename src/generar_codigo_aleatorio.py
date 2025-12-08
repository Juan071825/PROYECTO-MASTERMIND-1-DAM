import random

COLORES = ['rojo', 'verde', 'azul', 'amarillo', 'morado', 'negro', 'blanco', 'marrón']

EMOJIS_COLORES = {
'rojo': "\U0001F534",
'verde': "\U0001F7E2",
'azul': "\U0001F535",
'amarillo': "\U0001F7E1",
'morado': "\U0001F7E3",
'negro': "\u26AB",
'blanco': "\u26AA",
'marrón': "\U0001F7E4"
}

def generar_codigo_aleatorio():
    
    codigo_aleatorio = []

    while len(codigo_aleatorio) < 4:
        codigo_aleatorio.append(random.choice(COLORES))

    
    emojis_codigo_aleatorio = []
    for ficha in codigo_aleatorio:
        emojis_codigo_aleatorio.append(EMOJIS_COLORES[ficha])
    return print(' '.join(emojis_codigo_aleatorio))



generar_codigo_aleatorio()