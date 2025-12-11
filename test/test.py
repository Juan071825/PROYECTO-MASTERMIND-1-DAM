import pytest

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


#from src.introducir_codigo import pedir_codigo_secreto
from src.generar_codigo_aleatorio import generar_codigo_aleatorio

#@pytest.mark.pedir_codigo_secreto
#def test_pedir_codigo_secreto():
    
#    resultado = pedir_codigo_secreto()
    
#   assert resultado is not None
#    assert len(resultado) == 4
#    for color in resultado: assert color in ['verde', 'azul', 'amarillo', 'morado', 'negro', 'marrón']


@pytest.mark.generar_codigo_aleatorio
def test_generar_codigo_aleatorio():
    resultado = generar_codigo_aleatorio()
    assert resultado is not None
    assert len(resultado) == 4
    for color in resultado: assert color in ["\U0001F7E2", "\U0001F535", "\U0001F7E1", "\U0001F7E3", "\u26AB", "\U0001F7E4"]