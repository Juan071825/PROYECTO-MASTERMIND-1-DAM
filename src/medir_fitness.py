from src.generar_poblacion_aleatoria import generar_poblacion_aleatoria
from src.introducir_codigo import pedir_codigo_secreto
 
censo = generar_poblacion_aleatoria()
codigo_secreto = pedir_codigo_secreto()
censo_individuos = list(censo.values())

def medir_fitness():

    valores_fitness = []
    
    
    for individuo in censo_individuos:
        codigo_secreto_copy = codigo_secreto.copy()
        individuo_copy = individuo.copy()
        fitness = 0
        
        for index in range(len(individuo)):
           #Coincidencia exacta (color y posición).
            if individuo_copy[index] == codigo_secreto_copy[index]:
                fitness += 2
                codigo_secreto_copy[index] = None
                individuo_copy[index] = None


        for index in range(len(individuo)):
            #Coincidencia parcial (color pero no posición).
            if individuo_copy[index] is not None and individuo_copy[index] in codigo_secreto_copy:
                fitness += 1
                codigo_secreto_copy[codigo_secreto_copy.index(individuo_copy[index])] = None
                individuo_copy[index] = None

            else:
                fitness += 0
        
        valores_fitness.append(fitness)
    return valores_fitness






def registrar_fitness():
    
    valores_fitness = medir_fitness()
    
    values_dict = list(zip(censo_individuos, valores_fitness))
    return dict(zip(censo.keys(), values_dict))


