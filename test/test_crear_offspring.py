import random
from src.crear_offspring import ( seleccionar_padres, cruzar, generar_mutacion, crear_hijo, crear_offspring)
from src.parametros_mastermind import EMOJIS_ALELOS


# Tests de seleccionar_padres

def test_seleccionar_padres_devuelve_listas():
    progenitores = {
        "p1": [[1,1,1,1], 10],
        "p2": [[2,2,2,2], 20]
    }

    padre, madre = seleccionar_padres(progenitores)           # Seleccionamos dos padres

    assert len(padre) == 4                                    # Padre tiene 4 colores
    assert len(madre) == 4                                    # Madre tiene 4 colores



# Tests de cruzar


def test_cruzar():
    padre = [1,1,1,1]
    madre = [2,2,2,2]

    hijo = cruzar(padre, madre, 2)                            # Cruce en punto 2

    assert hijo == [1,1,2,2]                                  # Resultado esperado del cruce




# Tests de crear_hijo


def test_crear_hijo_longitud_correcta():
    padre = [1,1,1,1]
    madre = [2,2,2,2]

    hijo = crear_hijo(padre, madre)                           # Crear hijo completo

    assert len(hijo) == 4                                     # Siempre debe tener 4 alelos



# Tests de crear_offspring


def test_crear_offspring_basico():
    progenitores = {
        "p1": [[1,1,1,1], 10],
        "p2": [[2,2,2,2], 20]
    }

    hijos = crear_offspring(progenitores)                     # Generamos 25 hijos

    assert len(hijos) == 25                                   # Deben ser 25
    assert list(hijos.keys())[0] == "hijo1"                   # Primera clave correcta
    assert list(hijos.keys())[-1] == "hijo25"                 # Última clave correcta

    for hijo in hijos.values():
        assert len(hijo) == 4                                 # Cada hijo tiene 4 colores
        for alelo in hijo:
            assert alelo in EMOJIS_ALELOS.values()            
