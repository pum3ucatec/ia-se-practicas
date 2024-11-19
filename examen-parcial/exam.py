import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import norm

# Vectores TF-IDF del ejemplo
X = np.array([0.2, 0.5, 0.1, 0.0])
Y = np.array([0.3, 0.4, 0.0, 0.2])

# Calcular la similitud coseno
cosine_similarity = np.dot(X, Y) / (norm(X) * norm(Y))
print(f"Similitud Coseno: {cosine_similarity:.4f}")

# Normalizar los vectores para visualización
X_normalized = X / norm(X)
Y_normalized = Y / norm(Y)

# Gráfica en 2D (usando los dos primeros componentes)
plt.figure(figsize=(8, 6))
plt.quiver(0, 0, X_normalized[0], X_normalized[1], angles='xy', scale_units='xy', scale=1, color='r', label='X')
plt.quiver(0, 0, Y_normalized[0], Y_normalized[1], angles='xy', scale_units='xy', scale=1, color='b', label='Y')

# Configuración del gráfico
plt.xlim(-0.6, 0.6)
plt.ylim(-0.6, 0.6)
plt.grid()
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.title(f"Visualización de Vectores\nSimilitud Coseno: {cosine_similarity:.4f}")
plt.xlabel("Componente 1")
plt.ylabel("Componente 2")
plt.legend()
plt.show()
