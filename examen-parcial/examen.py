import numpy as np
import matplotlib.pyplot as plt

# Vectores dados
X = np.array([0.2, 0.5, 0.1, 0.0])
Y = np.array([0.3, 0.4, 0.2, 0.2])

# Cálculo de la similitud coseno
cosine_similarity = np.dot(X, Y) / (np.linalg.norm(X) * np.linalg.norm(Y))
print(f"Similitud coseno: {cosine_similarity:.4f}")

# Graficar los vectores en 2D para visualización
plt.figure(figsize=(8, 6))

# Ejes
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')

# Representar los vectores
plt.quiver(0, 0, X[0], X[1], angles='xy', scale_units='xy', scale=1, color='blue', label='Vector X')
plt.quiver(0, 0, Y[0], Y[1], angles='xy', scale_units='xy', scale=1, color='red', label='Vector Y')

# Límites del gráfico
plt.xlim(-0.1, 0.6)
plt.ylim(-0.1, 0.6)

# Etiquetas
plt.title("Similitud Coseno entre X y Y")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid()
plt.show()
