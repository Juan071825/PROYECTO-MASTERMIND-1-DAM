from src.generar_poblacion_aleatoria import generar_poblacion_aleatoria
from src.introducir_codigo import pedir_codigo_secreto
 
censo = generar_poblacion_aleatoria()
codigo_secreto = pedir_codigo_secreto()
censo_individuos = list(censo.values())

def medir_fitness():

   
    valores_fitness = []
    
    for individuo in censo_individuos:
        fitness = 0
        for color in individuo:
            if color in codigo_secreto:
                fitness += 1
            else:
                fitness += 0
        valores_fitness.append(fitness)
        return valores_fitness






def registrar_fitness():
    
    valores_fitness = medir_fitness()
    dict_fitness = {}
    
    for key in censo.keys():
        for valores in list(zip(censo_individuos, valores_fitness)):
            dict_fitness[key] = valores

    return print(dict_fitness)


registrar_fitness()