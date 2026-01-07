from src.crear_generacion import crear_generacion


# Test 1: Comprobar que se combinan correctamente progenitores + hijos
def test_crear_generacion_combinacion_correcta():
    progenitores = {"p1": [1, 2, 3, 4], "p2": [5, 6, 7, 8]}  
    hijos = {"h1": [9, 9, 9, 9]}                              

    nueva = crear_generacion(progenitores, hijos)             

    assert len(nueva) == 3                                    # Debe haber 3 individuos en total


# Test 2: Comprobar que las claves nuevas son correctas
def test_crear_generacion_claves_correctas():
    progenitores = {"p1": [1, 2, 3, 4]}                       
    hijos = {"h1": [5, 6, 7, 8]}                              

    nueva = crear_generacion(progenitores, hijos)

    assert list(nueva.keys()) == ["individuo0", "individuo1"] # Las claves deben ser consecutivas


# Test 3: Comprobar que el orden de los valores se mantiene
def test_crear_generacion_orden_valores():
    progenitores = {"p1": [1, 1, 1, 1]}                       
    hijos = {"h1": [2, 2, 2, 2]}                              

    nueva = crear_generacion(progenitores, hijos)

    assert nueva["individuo0"] == [1, 1, 1, 1]                # El primer valor debe ser el progenitor
    assert nueva["individuo1"] == [2, 2, 2, 2]                # El segundo debe ser el hijo
