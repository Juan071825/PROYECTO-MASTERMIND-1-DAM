from src.generar_codigo_aleatorio import generar_codigo_aleatorio

def generar_poblacion_aleatoria(numero_individuos):
    poblacion ={}
    contador_individuos = 0

    while contador_individuos < numero_individuos:
        individuo = generar_codigo_aleatorio()
        poblacion['individuo' + str(contador_individuos + 1)] = individuo
        contador_individuos += 1

    return poblacion

