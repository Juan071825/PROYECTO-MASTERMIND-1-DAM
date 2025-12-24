import sys
import src.introducir_codigo as modulos
import src.generar_poblacion_aleatoria as modulos
import src.medir_fitness as modulos
import src.selector_padres as modulos
import src.crear_offspring as modulos
import src.crear_generacion as modulos

cromosoma_secreto = modulos.pedir_codigo_secreto()

def mejor_poblacion_inicial():

    contador_generaciones = 0

   
    poblacion_inicial = modulos.generar_poblacion_aleatoria(100)
    diccionario_fitness_inicial = modulos.medir_fitness(poblacion_inicial)

    diccionario_valores_fitness_inicial = diccionario_fitness_inicial.values()
    diccionario_fitness_inicial_ordenado = diccionario_valores_fitness_inicial.sort(reverse=True, key=lambda x: x[1])

    return diccionario_fitness_inicial_ordenado[0]
         
            

def mejor_resto_generaciones(diccionario_fitness_inicial):
    while contador_generaciones < 14:    
        diccionario_padres_seleccionados = modulos.selector_padres(diccionario_fitness_inicial)
        diccionario_hijos = modulos.crear_offspring(diccionario_padres_seleccionados)
        diccionario_hijos_fitness = modulos.medir_fitness(diccionario_hijos)
        crear_generacion = modulos.crear_generacion(diccionario_padres_seleccionados, diccionario_hijos_fitness)

        contador_generaciones += 1














