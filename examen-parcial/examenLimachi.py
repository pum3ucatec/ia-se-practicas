import numpy as np
import matplotlib.pyplot as plt

# Vectores del ejemplo práctico
X = np.array([0.2, 0.5, 0.1, 0.0])
Y = np.array([0.3, 0.4, 0.0, 0.2])

# Función para calcular la similitud coseno
def cosine_similarity(vec1, vec2):
    dot_product = np.dot(vec1, vec2)
    magnitude = np.linalg.norm(vec1) * np.linalg.norm(vec2)
    return dot_product / magnitude

# Calcular la similitud coseno
similarity = cosine_similarity(X, Y)
print(f"Similitud coseno: {similarity:.4f}")

# Gráfica de los vectores (usaremos solo los dos primeros componentes para visualizar en 2D)
x_coords = [0, X[0]]
y_coords = [0, X[1]]

x_coords_y = [0, Y[0]]
y_coords_y = [0, Y[1]]

plt.figure(figsize=(8, 6))
plt.quiver(0, 0, X[0], X[1], angles='xy', scale_units='xy', scale=1, color='r', label='Vector X')
plt.quiver(0, 0, Y[0], Y[1], angles='xy', scale_units='xy', scale=1, color='b', label='Vector Y')

# Configuración de la gráfica
plt.xlim(-0.1, 0.4)
plt.ylim(-0.1, 0.6)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.title("Representación de los vectores")
plt.xlabel("Componente X")
plt.ylabel("Componente Y")
plt.legend()
plt.show()
