import matplotlib.pyplot as plt

def graficar_barras_fitness_por_generacion_y_color(generaciones, fitness_colores):
    plt.figure(figsize=(12, 6))

    # Colores reales para cada línea
    colores_plot = {
        "verde": "green",
        "azul": "blue",
        "amarillo": "yellow",
        "morado": "purple",
        "negro": "black",
        "marrón": "brown"
    }

    for color, valores in fitness_colores.items():
        plt.plot(
            generaciones,
            valores,
            marker='o',
            label=color,
            color=colores_plot[color]
        )

    plt.xlabel("Generación")
    plt.ylabel("Uso total del color")
    plt.title("Evolución del uso de colores por generación")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
