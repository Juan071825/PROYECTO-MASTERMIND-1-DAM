from src.crear_offspring import generar_mutacion, crear_offspring
from src.parametros_mastermind import EMOJIS_ALELOS


# Tests de generar_mutacion


def test_generar_mutacion_no_ocurre():
    hijo = [EMOJIS_ALELOS["verde"]] * 4                       # Hijo inicial con 4 colores iguales

    resultado = generar_mutacion(hijo.copy(), 0.0)           # Probabilidad 0 de no mutar

    assert resultado == hijo                                 # No debe cambiar nada


def test_generar_mutacion_si_ocurre():
    hijo = [EMOJIS_ALELOS["verde"]] * 4                       # Hijo inicial con 4 colores iguales

    resultado = generar_mutacion(hijo.copy(), 1.0)           # Probabilidad 1 de mutar

    assert resultado != hijo                                 # Debe cambiar al menos un color



# Tests de crear_offspring


def test_crear_offspring():
    progenitores = {
        "p1": [[EMOJIS_ALELOS["verde"]] * 4, 10],             # Progenitor 1 
        "p2": [[EMOJIS_ALELOS["azul"]] * 4, 20]              # Progenitor 2
    }

    hijos = crear_offspring(progenitores)                    # Generamos 25 hijos

    assert len(hijos) == 25                                  # Deben ser 25 hijos
    assert list(hijos.keys())[0] == "hijo0"                  # Primera clave correcta
    assert list(hijos.keys())[-1] == "hijo24"                # Última clave correcta

    for hijo in hijos.values():
        assert len(hijo) == 4                                # Cada hijo tiene 4 alelos
        for alelo in hijo:
            assert alelo in EMOJIS_ALELOS.values()           # Alelos válidos (emojis)
