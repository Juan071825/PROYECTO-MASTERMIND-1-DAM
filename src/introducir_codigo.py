from parametros_mastermind import COLORES_ELEGIBLES, EMOJIS_COLORES

def pedir_codigo_secreto():
    print('Por favor, introduce un código de 4 colores de entre los siguientes 8, pueden estar repetidos:')
    print(", ".join(COLORES_ELEGIBLES) + '.')
    print('Para que funcione correctamente, introduce el nombre del color tak cual aparece arriba. Y cuidado con los espacios!')
    UNO = 1
    codigo_secreto = []

    while len(codigo_secreto) != 4:
        print('Debes introducir los 4 colores.')
        print('Introduce el color ' + str(len(codigo_secreto)+ UNO) +'.')
        entrada_color = input('Introduce un color: ')
        
        
        if entrada_color in COLORES_ELEGIBLES:
            codigo_secreto.append(entrada_color)
    
        else:
            print("Algún color no es válido, inténtalo de nuevo.")

    emojis_codigo_secreto = []
    for ficha in codigo_secreto:
        emojis_codigo_secreto.append(EMOJIS_COLORES[ficha])
    
    return print(' '.join(emojis_codigo_secreto))
            




