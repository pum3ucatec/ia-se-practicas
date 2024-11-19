import numpy as np
import matplotlib.pyplot as plt

# Vectores dados
X = np.array([0.2, 0.5, 0.1, 0.0])
Y = np.array([0.3, 0.4, 0.0, 0.2])

# Cálculo de la similitud coseno
def cosine_similarity(vec1, vec2):
    dot_product = np.dot(vec1, vec2)
    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)
    return dot_product / (norm_vec1 * norm_vec2)

similarity = cosine_similarity(X, Y)
print(f"Similitud coseno: {similarity:.4f}")

# Proyección de los vectores en 2D para visualización
# Normalizamos los vectores para graficarlos
X_norm = X / np.linalg.norm(X)
Y_norm = Y / np.linalg.norm(Y)

# Crear la gráfica
plt.figure(figsize=(8, 8))
plt.quiver(0, 0, X_norm[0], X_norm[1], angles='xy', scale_units='xy', scale=1, color='r', label="Vector X (Normalizado)")
plt.quiver(0, 0, Y_norm[0], Y_norm[1], angles='xy', scale_units='xy', scale=1, color='b', label="Vector Y (Normalizado)")

# Configuración del gráfico
plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.axhline(0, color='gray', linestyle='--')
plt.axvline(0, color='gray', linestyle='--')
plt.grid(color='lightgray', linestyle='--', linewidth=0.5)
plt.title(f"Similitud Coseno: {similarity:.4f}")
plt.xlabel("Componente 1")
plt.ylabel("Componente 2")
plt.legend()
plt.gca().set_aspect('equal', adjustable='box')

# Mostrar la gráfica
plt.show()
