import numpy as np
import matplotlib.pyplot as plt

def cosine_similarity(x, y):
    """
    Calcula la similitud coseno entre dos vectores x e y.
    """
    dot_product = np.dot(x, y)
    norm_x = np.linalg.norm(x)
    norm_y = np.linalg.norm(y)
    return dot_product / (norm_x * norm_y)

# Ejemplo práctico
X = np.array([0.2, 0.5, 0.1, 0.0])
Y = np.array([0.3, 0.4, 0.0, 0.2])

# Calcular similitud coseno
similarity = cosine_similarity(X, Y)
print(f"Similitud coseno: {similarity:.4f}")

# Visualización de vectores
fig, ax = plt.subplots(figsize=(8, 8))
ax.quiver(0, 0, X[0], X[1], angles='xy', scale_units='xy', scale=1, color='blue', label='Vector X')
ax.quiver(0, 0, Y[0], Y[1], angles='xy', scale_units='xy', scale=1, color='red', label='Vector Y')

# Configuración del gráfico
ax.set_xlim(-0.5, 0.6)
ax.set_ylim(-0.5, 0.6)
ax.axhline(0, color='black',linewidth=0.5)
ax.axvline(0, color='black',linewidth=0.5)
ax.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
ax.set_title(f"Similitud Coseno: {similarity:.4f}", fontsize=14)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.legend()
plt.savefig("Graficoexam1p.png")
