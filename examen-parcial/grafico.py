import matplotlib.pyplot as plt
import numpy as np
from cosine_similarity import cosine_similarity

def plot_vectors(x, y, similarity, output_file="grafico.png"):
    """Grafica dos vectores y muestra su información, además de guardar el resultado como una imagen PNG."""
    origin = [0, 0]  # Origen para ambos vectores

    # Convertir los vectores para graficar
    x_coords = np.array(x)
    y_coords = np.array(y)

    # Graficar los vectores
    plt.quiver(*origin, x_coords[0], x_coords[1], angles='xy', scale_units='xy', scale=1, color='r', label=f'Vector X {x}')
    plt.quiver(*origin, y_coords[0], y_coords[1], angles='xy', scale_units='xy', scale=1, color='b', label=f'Vector Y {y}')

    # Configurar límites
    plt.xlim(-0.5, 0.5)
    plt.ylim(-0.5, 0.5)
    plt.axhline(0, color='gray', linewidth=0.5)
    plt.axvline(0, color='gray', linewidth=0.5)
    plt.grid()

    # Título y leyenda
    plt.title(f'Similitud Coseno: {similarity:.2f}')
    plt.legend()

    # Agregar texto con información adicional
    plt.text(0.1, -0.4, f"Vector X: {x}", fontsize=10, color='red')
    plt.text(0.1, -0.45, f"Vector Y: {y}", fontsize=10, color='blue')
    plt.text(0.1, -0.5, f"Similitud Coseno: {similarity:.2f}", fontsize=10, color='green')

    # Guardar la imagen como PNG
    plt.savefig(output_file)
    print(f"Gráfico guardado como {output_file}")
    plt.close()

if __name__ == "__main__":
    # Vectores del ejemplo práctico
    x = [0.2, 0.5]
    y = [0.3, 0.4]

    # Calcular similitud coseno
    similarity = cosine_similarity(x, y)
    print(f"Similitud Coseno: {similarity:.2f}")

    # Generar y guardar el gráfico
    plot_vectors(x, y, similarity)

