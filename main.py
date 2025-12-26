import sys
from src.medir_fitness import medir_fitness
from src.crear_offspring import crear_offspring
from src.crear_generacion import crear_generacion
from src.selector_padres import selector_padres
from src.generar_poblacion_aleatoria import generar_poblacion_aleatoria
import src.introducir_codigo as modulos

cromosoma_secreto = modulos.pedir_codigo_secreto()


def mejor_candidato_generacion(poblacion):
    fitness_poblacion = medir_fitness(poblacion, cromosoma_secreto)
    fitness_ordenado = sorted(fitness_poblacion.items(), key=lambda x: x[1], reverse=True)
    mejor_candidato = fitness_ordenado[0]
    return mejor_candidato


def registro_generaciones():
    contador_generaciones = 1

    poblacion = generar_poblacion_aleatoria(100)
    lista_mejores_candidatos = []

    while contador_generaciones < 14:
        
        if contador_generaciones == 1:
            mejor_candidato = mejor_candidato_generacion(poblacion)
            lista_mejores_candidatos.append(mejor_candidato)
            contador_generaciones += 1
        else:
            fitness_poblacion = medir_fitness(poblacion, cromosoma_secreto)
            padres_seleccionados = selector_padres(fitness_poblacion)
            hijos = crear_offspring(padres_seleccionados)
            fitness_hijos = medir_fitness(hijos, cromosoma_secreto)
            poblacion = crear_generacion(padres_seleccionados, fitness_hijos)
            mejor_candidato = mejor_candidato_generacion(poblacion)
            lista_mejores_candidatos.append(mejor_candidato)
            contador_generaciones += 1

    return print(lista_mejores_candidatos)


if __name__ == "__main__":
    registro_generaciones()






















