from src.introducir_codigo import pedir_codigo_secreto

 




def medir_fitness(poblacion, cromosoma_secreto):


    individuos = list(poblacion.values())
    valores_fitness = []
    
    
    for individuo in individuos:
        cromosoma_secreto_copia = cromosoma_secreto.copy()
        individuo_copia = individuo.copy()
        fitness = 0
        
        for alelo in range(len(individuo)):
           #Coincidencia exacta (color y posición).
            if individuo_copia[alelo] == cromosoma_secreto_copia[alelo]:
                fitness += 2
                cromosoma_secreto_copia[alelo] = None
                individuo_copia[alelo] = None


        for alelo in range(len(individuo)):
            #Coincidencia parcial (color pero no posición).
            if individuo_copia[alelo] is not None and individuo_copia[alelo] in cromosoma_secreto_copia:
                fitness += 1
                cromosoma_secreto_copia[cromosoma_secreto_copia.index(individuo_copia[alelo])] = None
                individuo_copia[alelo] = None

            else:
                fitness += 0
        
        valores_fitness.append(fitness)
    
    valores_diccionario_fitness = list(zip(individuos, valores_fitness))
    return dict(zip(poblacion.keys(), valores_diccionario_fitness))



