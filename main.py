from src.medir_fitness import medir_fitness
from src.crear_offspring import crear_offspring
from src.crear_generacion import crear_generacion
from src.selector_padres import selector_padres
from src.generar_poblacion_aleatoria import generar_poblacion_aleatoria
from src.introducir_codigo import pedir_codigo_secreto
from src.parametros_mastermind import TAMAÑO_POBLACION

# NUEVOS IMPORTS
from src.fitness_por_color import fitness_por_color
from src.grafico import graficar_barras_fitness_por_generacion_y_color


def introducir_cromosoma_secreto():
    cromosoma_secreto = pedir_codigo_secreto()
    return cromosoma_secreto


def registro_generaciones(cromosoma_secreto):

    contador_generaciones = 0
    poblacion = generar_poblacion_aleatoria(100)
    lista_mejores_candidatos = []

    # NUEVAS ESTRUCTURAS PARA LA GRÁFICA
    generaciones = []
    fitness_colores = {
        "verde": [], "azul": [], "amarillo": [],
        "morado": [], "negro": [], "marrón": []
    }

    # CICLO PRINCIPAL
    while contador_generaciones < 14:

        mejor_candidato = mejor_candidato_generacion(poblacion, cromosoma_secreto)
        lista_mejores_candidatos.append(mejor_candidato)

        if mejor_candidato[1][1] == 16:  # fitness máximo 4*4 = 16
            break

        fitness_poblacion = medir_fitness(poblacion, cromosoma_secreto)

        # REGISTRO PARA LA GRÁFICA
        generaciones.append(contador_generaciones)

        fitness_gen = fitness_por_color(poblacion, cromosoma_secreto)
        for color in fitness_colores:
            fitness_colores[color].append(fitness_gen[color])

        # EVOLUCIÓN GENÉTICA
        padres_seleccionados = selector_padres(fitness_poblacion)
        hijos = crear_offspring(padres_seleccionados)
        poblacion = crear_generacion(padres_seleccionados, hijos, TAMAÑO_POBLACION)

        contador_generaciones += 1

    # MOSTRAR GRÁFICA AL FINAL
    graficar_barras_fitness_por_generacion_y_color(generaciones, fitness_colores)

    return print(lista_mejores_candidatos)


def mejor_candidato_generacion(poblacion, cromosoma_secreto):
    fitness_poblacion = medir_fitness(poblacion, cromosoma_secreto)
    fitness_ordenado = sorted(fitness_poblacion.items(), key=lambda x: x[1][1], reverse=True)
    mejor_candidato = fitness_ordenado[0]
    return mejor_candidato


if __name__ == "__main__":
    registro_generaciones(cromosoma_secreto=introducir_cromosoma_secreto())
