import numpy as np
import matplotlib.pyplot as plt

# Vectores del ejemplo práctico
X = np.array([0.2, 0.5, 0.1, 0.0])
Y = np.array([0.3, 0.4, 0.0, 0.2])

# Función para calcular la similitud coseno
def cosine_similarity(vec1, vec2):
    dot_product = np.dot(vec1, vec2)
    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)
    similarity = dot_product / (norm_vec1 * norm_vec2)
    return similarity

# Calcular la similitud coseno
similarity = cosine_similarity(X, Y)

print(f"Similitud coseno entre X y Y: {similarity:.4f}")

# Proyectar los vectores en un espacio 2D para visualización
# (los datos originales están en un espacio n-dimensional, pero para graficar los reducimos a 2D)
X_2D = X[:2]  # Tomamos las primeras dos dimensiones de X
Y_2D = Y[:2]  # Tomamos las primeras dos dimensiones de Y

# Crear una gráfica para visualizar los vectores
plt.figure(figsize=(8, 6))
plt.quiver(0, 0, X_2D[0], X_2D[1], angles='xy', scale_units='xy', scale=1, color='r', label='Vector X')
plt.quiver(0, 0, Y_2D[0], Y_2D[1], angles='xy', scale_units='xy', scale=1, color='b', label='Vector Y')

# Configuración del gráfico
plt.xlim(-0.1, 0.6)
plt.ylim(-0.1, 0.6)
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.title(f"Similitud Coseno: {similarity:.4f}")
plt.xlabel("Dimensión 1")
plt.ylabel("Dimensión 2")

# Mostrar el gráfico
plt.show()
