from src.generar_poblacion_aleatoria import generar_poblacion_aleatoria
from src.introducir_codigo import pedir_codigo_secreto


def medir_fitness():
    censo = generar_poblacion_aleatoria(5)
    codigo_secreto = pedir_codigo_secreto()
    censo_individuos = list(censo.values())
    registro_fitness = []
    
    for individuo in censo_individuos:
        fitness = 0
        for color in individuo:
            if color in codigo_secreto:
                fitness += 1
            else:
                fitness += 0
        registro_fitness.append(fitness)
    return registro_fitness
