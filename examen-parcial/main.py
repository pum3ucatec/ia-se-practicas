import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity

# Vectores de ejemplo
X = np.array([0.2, 0.5, 0.1, 0.0])  # Primer vector
Y = np.array([0.3, 0.4, 0.0, 0.2])  # Segundo vector

# Calcular la similitud coseno entre los dos vectores
similarity = cosine_similarity([X], [Y])[0][0]
print(f"Similitud Coseno: {similarity:.3f}")

# Graficar los vectores X y Y
plt.figure(figsize=(6, 6))
plt.quiver(0, 0, X[0], X[1], angles='xy', scale_units='xy', scale=1, color='r', label='Vector X')
plt.quiver(0, 0, Y[0], Y[1], angles='xy', scale_units='xy', scale=1, color='b', label='Vector Y')

# Ajustar límites del gráfico
plt.xlim(-0.5, 0.5)
plt.ylim(-0.5, 0.5)

# Etiquetas y título
plt.text(X[0] * 1.1, X[1] * 1.1, 'X', color='r')
plt.text(Y[0] * 1.1, Y[1] * 1.1, 'Y', color='b')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.title(f"Similitud Coseno: {similarity:.3f}")

# Mostrar la leyenda
plt.legend()

# Mostrar gráfico
plt.show()
