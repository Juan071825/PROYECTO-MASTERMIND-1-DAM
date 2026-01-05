from src.generar_codigo_aleatorio import generar_codigo_aleatorio, EMOJIS_ALELOS

def test_generar_codigo_aleatorio():
    resultado = generar_codigo_aleatorio()

    assert len(resultado) == 4

    for emoji in resultado:
        assert emoji in EMOJIS_ALELOS.values()
