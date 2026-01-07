from src.fitness_por_color import fitness_por_color

def test_fitness_por_color_basico():
    poblacion = {
        "individuo0": ["🟩", "🟦", "🟩", "🟪"]
    }

    cromosoma_secreto = ["🟩", "🟦", "🟪", "⬛"]

    resultado = fitness_por_color(poblacion, cromosoma_secreto)

    # Comprobamos que devuelve todas las claves esperadas
    assert "verde" in resultado
    assert "azul" in resultado
    assert "amarillo" in resultado
    assert "morado" in resultado
    assert "negro" in resultado
    assert "marrón" in resultado

    for valor in resultado.values():
        assert isinstance(valor, int)
