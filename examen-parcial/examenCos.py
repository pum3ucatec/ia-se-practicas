import numpy as np
import matplotlib.pyplot as plt

# Definimos dos vectores de características TF-IDF
vector1 = np.array([0.2, 0.5, 0.1, 0.0])
vector2 = np.array([0.3, 0.4, 0.0, 0.2])

# Función para calcular la similitud del coseno
def similitud_coseno(vector_a, vector_b):
    """Calcula la similitud del coseno entre dos vectores.

    Args:
        vector_a: El primer vector.
        vector_b: El segundo vector.

    Returns:
        La similitud del coseno entre los dos vectores.
    """

    producto_punto = np.dot(vector_a, vector_b)
    norma_a = np.linalg.norm(vector_a)
    norma_b = np.linalg.norm(vector_b)
    return producto_punto / (norma_a * norma_b)

# Calculamos la similitud del coseno entre los dos vectores
similitud = similitud_coseno(vector1, vector2)
print(f"Similitud del coseno: {similitud:.4f}")

# Creamos una figura para la gráfica
plt.figure(figsize=(8, 6))

# Graficamos los vectores como flechas
plt.quiver(0, 0, vector1[0], vector1[1], angles='xy', scale_units='xy', scale=1, color='r', label='Vector 1')
plt.quiver(0, 0, vector2[0], vector2[1], angles='xy', scale_units='xy', scale=1, color='b', label='Vector 2')

# Configuramos la gráfica
plt.xlim(-0.5, 1)
plt.ylim(-0.5, 1)
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.grid(True)
plt.title('Vectores TF-IDF y Similitud del Coseno')
plt.xlabel('Componente 1')
plt.ylabel('Componente 2')
plt.legend()

# Guardamos la gráfica como un archivo PNG
plt.savefig("grafico_similitud_coseno.png")
plt.show()