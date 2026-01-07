from src.crear_generacion import crear_generacion

def test_tamano():
    progenitores = {
        "p1": ([1, 1, 1, 1], 10, (4, 0)),
        "p2": ([2, 2, 2, 2], 5, (2, 1)),
    }
    hijos = {
        "h1": [3, 3, 3, 3],
    }

    nueva = crear_generacion(progenitores, hijos, tamaño_poblacion=4)

    assert len(nueva) == 4


def test_mejor_primero():
    progenitores = {
        "p1": ([1, 1, 1, 1], 3, (1, 1)),
        "p2": ([9, 9, 9, 9], 10, (4, 0)),  
    }
    hijos = {}

    nueva = crear_generacion(progenitores, hijos, tamaño_poblacion=2)

    assert nueva["individuo0"] == [9, 9, 9, 9]


def test_hijos_incluidos():
    progenitores = {
        "p1": ([1, 1, 1, 1], 10, (4, 0)),
    }
    hijos = {
        "h1": [5, 5, 5, 5],
        "h2": [6, 6, 6, 6],
    }

    nueva = crear_generacion(progenitores, hijos, tamaño_poblacion=3)

    assert [5, 5, 5, 5] in nueva.values()
    assert [6, 6, 6, 6] in nueva.values()
