

def crear_generacion(progenitores, hijos):
    diccionario_padres_hijos = {}
    diccionario_padres_hijos.update(progenitores)
    diccionario_padres_hijos.update(hijos)

    nueva_generacion = {}
    contador_entradas = 0
    for entrada in list(diccionario_padres_hijos.values()):
        nueva_generacion['individuo' + str(contador_entradas)] = entrada
        contador_entradas += 1 
        
    return nueva_generacion








if __name__ == "__main__":
    from src.medir_fitness import medir_fitness
    from src.crear_offspring import crear_offspring

    progenitores = medir_fitness()
    hijos = crear_offspring(progenitores)

    nueva_generacion = crear_generacion(progenitores, hijos)
    print(nueva_generacion)