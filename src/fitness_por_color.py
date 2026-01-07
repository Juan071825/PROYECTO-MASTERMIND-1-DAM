from src.medir_fitness import medir_fitness
from src.parametros_mastermind import EMOJIS_ALELOS

def fitness_por_color(poblacion, cromosoma_secreto):
    colores = ["verde", "azul", "amarillo", "morado", "negro", "marrón"]

    # Diccionario con el fitness acumulado de cada color
    fitness_colores = {color: 0 for color in colores}

    fitness_poblacion = medir_fitness(poblacion, cromosoma_secreto)

    for individuo, (cromosoma, fitness, _) in fitness_poblacion.items():
        for emoji in cromosoma:
            for nombre_color, emoji_color in EMOJIS_ALELOS.items():
                if emoji == emoji_color:
                    fitness_colores[nombre_color] += fitness

    return fitness_colores

