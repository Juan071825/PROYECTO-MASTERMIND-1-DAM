from src.generar_codigo_aleatorio import generar_codigo_aleatorio

def generar_poblacion_aleatoria(numero_soluciones=100):
    censo ={}
    cont = 0
    UNO = 1

    while cont < numero_soluciones:
        individuo = generar_codigo_aleatorio()
        censo['individuo' + str(cont)] = individuo
        cont += UNO

    return censo

