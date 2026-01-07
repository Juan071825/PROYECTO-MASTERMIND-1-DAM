from src.generar_codigo_aleatorio import generar_codigo_aleatorio

def generar_poblacion_aleatoria(numero_individuos):
    poblacion ={}
    contador_individuos = 0
    UNO = 1

    while contador_individuos < numero_individuos:
        individuo = generar_codigo_aleatorio()
        poblacion['individuo' + str(contador_individuos + UNO)] = individuo
        contador_individuos += UNO

    return poblacion

