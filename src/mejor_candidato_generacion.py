from src.medir_fitness import medir_fitness

def mejor_candidato_generacion(poblacion, cromosoma_secreto):
    fitness_poblacion = medir_fitness(poblacion, cromosoma_secreto)
    fitness_ordenado = sorted(fitness_poblacion.items(), key=lambda x: x[1][1], reverse=True)
    mejor_candidato = fitness_ordenado[0]
    return mejor_candidato