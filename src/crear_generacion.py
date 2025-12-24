

def crear_generacion(progenitores, hijos):
    nueva_generacion = {}
    nueva_generacion.update(progenitores)
    nueva_generacion.update(hijos)
    return nueva_generacion



if __name__ == "__main__":
    from src.medir_fitness import medir_fitness
    from src.crear_offspring import crear_offspring

    progenitores = medir_fitness
    hijos = crear_offspring(progenitores)

    nueva_generacion = crear_generacion(progenitores, hijos)
    print(nueva_generacion)