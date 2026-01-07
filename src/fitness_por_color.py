from src.medir_fitness import medir_fitness
from src.parametros_mastermind import EMOJIS_ALELOS

def fitness_por_color(poblacion, cromosoma_secreto):
    colores = ["verde", "azul", "amarillo", "morado", "negro", "marrón"]

    # Diccionario con el conteo de usos de cada color
    fitness_colores = {color: 0 for color in colores}

    # Ya no necesitas fitness, pero mantenerlo no molesta
    fitness_poblacion = medir_fitness(poblacion, cromosoma_secreto)

    for individuo, (cromosoma, _, _) in fitness_poblacion.items():
        for emoji in cromosoma:
            for nombre_color, emoji_color in EMOJIS_ALELOS.items():
                if emoji == emoji_color:
                    fitness_colores[nombre_color] += 1

    return fitness_colores
