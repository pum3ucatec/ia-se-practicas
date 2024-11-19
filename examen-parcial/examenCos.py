import numpy as np
import matplotlib.pyplot as plt

# Definimos los vectores TF-IDF
X = np.array([0.2, 0.5, 0.1, 0.0])
Y = np.array([0.3, 0.4, 0.0, 0.2])

# Calculamos la similitud coseno
def cosine_similarity(x, y):
    dot_product = np.dot(x, y)
    norm_x = np.linalg.norm(x)
    norm_y = np.linalg.norm(y)
    return dot_product / (norm_x * norm_y)

similarity = cosine_similarity(X, Y)

# Imprimimos el resultado de la similitud coseno
print(f"Similitud coseno: {similarity:.4f}")

# Graficamos los vectores
plt.figure(figsize=(8, 6))
plt.quiver(0, 0, X[0], X[1], angles='xy', scale_units='xy', scale=1, color='r', label='Vector X')
plt.quiver(0, 0, Y[0], Y[1], angles='xy', scale_units='xy', scale=1, color='b', label='Vector Y')

# Configuraciones del gráfico
plt.xlim(-0.5, 1)
plt.ylim(-0.5, 1)
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.grid()
plt.title('Vectores TF-IDF y Similitud Coseno')
plt.xlabel('Componente 1')
plt.ylabel('Componente 2')
plt.legend()
plt.show()

