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

def pedir_codigo_secreto():
    print('Por favor, introduce un código de 4 colores de entre los siguientes 8, pueden estar repetidos:')
    print(", ".join(COLORES) + '.')
    print('Para que funcione correctamente, introduce el nombre del color tak cual aparece arriba. Y cuidado con los espacios!')
    UNO = 1
    codigo_secreto = []

    while len(codigo_secreto) != 4:
        print('Debes introducir los 4 colores.')
        print('Introduce el color ' + str(len(codigo_secreto)+ UNO) +'.')
        entrada_color = input('Introduce un color: ')
        
        
        if entrada_color in COLORES:
            codigo_secreto.append(entrada_color)
    
        else:
            print("Algún color no es válido, inténtalo de nuevo.")

    emojis_codigo_secreto = []
    for ficha in codigo_secreto:
        emojis_codigo_secreto.append(EMOJIS_COLORES[ficha])
    
    return print(' '.join(emojis_codigo_secreto))
            

pedir_codigo_secreto()


