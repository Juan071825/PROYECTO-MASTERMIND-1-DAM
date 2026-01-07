from src.parametros_mastermind import ALELOS_ELEGIBLES, EMOJIS_ALELOS

def pedir_codigo_secreto():
    print('Por favor, introduce un código de 4 colores de entre los siguientes 8, pueden estar repetidos:')
    print(", ".join(ALELOS_ELEGIBLES) + '.')
    print('Para que funcione correctamente, introduce el nombre del color tal cual aparece arriba. Y cuidado con los espacios!')
    print("Si deseas salir del juego, teclea 'e' en cualquier momento.")
    UNO = 1
    cromosoma_secreto = []

    while len(cromosoma_secreto) != 4:
        print('Debes introducir los 4 colores.')
        print('Introduce el color ' + str(len(cromosoma_secreto)+ UNO) +'.')
        entrada_alelo = input('Introduce un color: ')
        
        
        if entrada_alelo in ALELOS_ELEGIBLES:
            cromosoma_secreto.append(entrada_alelo)

        elif entrada_alelo == 'e':
            return print("Has salido del juego.")
    
        else:
            print("Algún color no es válido, inténtalo de nuevo.")

    emojis_cromosoma_secreto = []
    for alelo in cromosoma_secreto:
        emojis_cromosoma_secreto.append(EMOJIS_ALELOS[alelo])
    
    return list(emojis_cromosoma_secreto)


if __name__ == '__main__':

    pedir_codigo_secreto()




