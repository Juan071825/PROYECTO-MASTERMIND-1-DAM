import matplotlib.pyplot as plt

def graficar_barras_fitness_por_generacion_y_color(generaciones, fitness_colores):
    plt.figure(figsize=(12, 6))

    for color, valores in fitness_colores.items():
        plt.plot(generaciones, valores, marker='o', label=color)

    plt.xlabel("Generación")
    plt.ylabel("Fitness total por color")
    plt.title("Evolución del fitness por color")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
