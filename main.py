from src.medir_fitness import medir_fitness
from src.crear_offspring import crear_offspring
from src.crear_generacion import crear_generacion
from src.selector_padres import selector_padres
from src.generar_poblacion_aleatoria import generar_poblacion_aleatoria
from src.introducir_codigo import pedir_codigo_secreto
from src.parametros_mastermind import TAMAÑO_POBLACION


def introducir_cromosoma_secreto():
    # """
# Pedimos el código secreto al usuario.
# """
    cromosoma_secreto = pedir_codigo_secreto()
    return cromosoma_secreto




def registro_generaciones(cromosoma_secreto):
# """
# Generamos la población inicial y dos variables que necesitaremos más adelante.
# """
    contador_generaciones = 0
    poblacion = generar_poblacion_aleatoria(100)
    lista_mejores_candidatos = []

# """
# Comenzamos el ciclo de generaciones.
# """
    while contador_generaciones < 14:

        mejor_candidato = mejor_candidato_generacion(poblacion, cromosoma_secreto)
        lista_mejores_candidatos.append(mejor_candidato)

        if mejor_candidato[1][1] == 16: # fitness máximo 4*4 = 16
            break

        fitness_poblacion = medir_fitness(poblacion, cromosoma_secreto)
        padres_seleccionados = selector_padres(fitness_poblacion)
        hijos = crear_offspring(padres_seleccionados)
        poblacion = crear_generacion(padres_seleccionados, hijos, TAMAÑO_POBLACION)

        contador_generaciones += 1


    return print(lista_mejores_candidatos)




def mejor_candidato_generacion(poblacion, cromosoma_secreto):
    fitness_poblacion = medir_fitness(poblacion, cromosoma_secreto)
    fitness_ordenado = sorted(fitness_poblacion.items(), key=lambda x: x[1][1], reverse=True) # ordena la pobalción en base a su fitness.
    mejor_candidato = fitness_ordenado[0]
    return mejor_candidato




if __name__ == "__main__":
    registro_generaciones(cromosoma_secreto=introducir_cromosoma_secreto())