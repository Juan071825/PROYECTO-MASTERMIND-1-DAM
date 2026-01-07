from src.selector_padres import selector_padres
from src.parametros_mastermind import PORCETAJE_DEFUNCION



# TEST 1 — Número correcto de padres seleccionados


def test_selector_padres_numero_correcto():
    poblacion = {
        "ind1": (["A"], 10),
        "ind2": (["B"], 20),
        "ind3": (["C"], 30),
        "ind4": (["D"], 40),
    }

    resultado = selector_padres(poblacion)

    numero_esperado = int(len(poblacion) * (1 - PORCETAJE_DEFUNCION))

    # El número de padres debe ser exactamente el esperado
    assert len(resultado) == numero_esperado


# TEST 2 — Las claves devueltas existen en la población original


def test_selector_padres_claves_validas():
    poblacion = {
        "ind1": (["A"], 10),
        "ind2": (["B"], 20),
        "ind3": (["C"], 30),
        "ind4": (["D"], 40),
    }

    resultado = selector_padres(poblacion)

    for key in resultado.keys():
        assert key in poblacion


# TEST 3 — Los valores devueltos son exactamente los originales


def test_selector_padres_valores_correctos():
    poblacion = {
        "ind1": (["A"], 10),
        "ind2": (["B"], 20),
        "ind3": (["C"], 30),
        "ind4": (["D"], 40),
    }

    resultado = selector_padres(poblacion)

    for key, value in resultado.items():
        assert value == poblacion[key]



# TEST 4 — Nunca devuelve duplicados porque usa un set


def test_selector_padres_sin_duplicados():
    poblacion = {
        "ind1": (["A"], 10),
        "ind2": (["B"], 20),
        "ind3": (["C"], 30),
        "ind4": (["D"], 40),
    }

    resultado = selector_padres(poblacion)

    # Las claves deben ser únicas
    assert len(resultado.keys()) == len(set(resultado.keys()))
