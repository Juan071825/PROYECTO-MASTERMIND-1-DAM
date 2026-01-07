import random

def crear_generacion(progenitores, hijos, tamaño_poblacion):

    nueva_generacion = {}
    contador_entradas = 0

    # """
    # Preservaremos al mejor progenitor (elitismo).
    # """

    mejor_progenitor = max(
        progenitores.items(), 
        key=lambda x: x[1][1]
        )[0] #[1]lista, [1] valores diccionario, [1] (cromosoma, fitness, pines), [0] clave cromosoma
    nueva_generacion['individuo0'] = progenitores[mejor_progenitor][0]
    contador_entradas += 1

    # """Introducimos a los progenitores, procurando no repetir al mejor progenitor"""
    for clave, (cromosoma, _, _) in progenitores.items():
        if clave == mejor_progenitor:
            continue
        nueva_generacion['individuo' + str(contador_entradas)] = cromosoma
        contador_entradas += 1
        
# """Añadimos a los hijos"""
    for cromosoma in hijos.values():
        nueva_generacion['individuo' + str(contador_entradas)] = cromosoma
        contador_entradas += 1 

    while len(nueva_generacion) < tamaño_poblacion:

        candidatos = [list(t) for t in set(tuple(c) for c in nueva_generacion.values())]
        if not candidatos:
            break

        cromosoma = random.choice(candidatos)
        nueva_generacion['individuo' + str(len(nueva_generacion))] = cromosoma
        
    return nueva_generacion








if __name__ == "__main__":
    from src.medir_fitness import medir_fitness
    from src.crear_offspring import crear_offspring

    progenitores = medir_fitness()
    hijos = crear_offspring(progenitores)

    nueva_generacion = crear_generacion(progenitores, hijos)
    print(nueva_generacion)