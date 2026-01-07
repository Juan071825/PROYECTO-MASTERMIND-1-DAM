from src.introducir_codigo import pedir_codigo_secreto
from src.parametros_mastermind import EMOJIS_ALELOS, EMOJIS_PINES

 




def medir_fitness(poblacion, cromosoma_secreto):


    individuos = list(poblacion.values())
    valores_fitness = []
    lista_pines = []
    individuos_lista = []
    
    
    for individuo in individuos:

        individuos_lista.append(individuo)
        cromosoma_secreto_copia = cromosoma_secreto.copy()
        individuo_copia = individuo.copy() 
        fitness = 0
        pines_individuo = []

        for alelo in range(len(individuo)):
           #Coincidencia exacta (color y posición).
            if individuo_copia[alelo] == cromosoma_secreto_copia[alelo]:
                fitness += 4
                cromosoma_secreto_copia[alelo] = None
                individuo_copia[alelo] = None
                pines_individuo.append(EMOJIS_PINES['rojo'])


        for alelo in range(len(individuo)):
            #Coincidencia parcial (color pero no posición).
            if individuo_copia[alelo] is not None and individuo_copia[alelo] in cromosoma_secreto_copia:
                fitness += 1
                cromosoma_secreto_copia[cromosoma_secreto_copia.index(individuo_copia[alelo])] = None
                individuo_copia[alelo] = None
                pines_individuo.append(EMOJIS_PINES['blanco'])

            else:
                fitness += 0
        

        valores_fitness.append(fitness)
        lista_pines.append(pines_individuo)
    
    valores_diccionario_fitness = list(zip(individuos_lista, valores_fitness, lista_pines))
    return dict(zip(poblacion.keys(), valores_diccionario_fitness))


if __name__ == "__main__":
    codigo_secreto = pedir_codigo_secreto()
    print(medir_fitness({'ind1': [EMOJIS_ALELOS['azul'], EMOJIS_ALELOS['azul'], EMOJIS_ALELOS['verde'], EMOJIS_ALELOS['morado']],
                         'ind2': [EMOJIS_ALELOS['morado'], EMOJIS_ALELOS['negro'], EMOJIS_ALELOS['blanco'], EMOJIS_ALELOS['marrón']]},codigo_secreto))