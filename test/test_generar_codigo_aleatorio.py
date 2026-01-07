from src.generar_codigo_aleatorio import generar_codigo_aleatorio
from src.parametros_mastermind import EMOJIS_ALELOS


def test_generar_codigo_aleatorio():
    resultado = generar_codigo_aleatorio()          # Genera un código aleatorio de 4 emojis

    assert len(resultado) == 4                      # Comprobamos que el código tiene exactamente 4 posiciones

    for emoji in resultado:
        assert emoji in EMOJIS_ALELOS.values()      # Cada emoji debe ser uno de los permitidos en EMOJIS_ALELOS