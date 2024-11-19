import numpy as np
import matplotlib.pyplot as plt

X = np.array([0.2, 0.5, 0.1, 0.0])
Y = np.array([0.3, 0.4, 0.0, 0.2])

def cosine_similarity(x, y):
    dot_product = np.dot(x, y)
    magnitude_x = np.linalg.norm(x)
    magnitude_y = np.linalg.norm(y)
    return dot_product / (magnitude_x * magnitude_y)

similarity = cosine_similarity(X, Y)
print(f"Similitud Coseno: {similarity:.4f}")
X_2D = X[:2]
Y_2D = Y[:2]
plt.figure(figsize=(8, 8))
origin = [0, 0]
plt.quiver(*origin, X_2D[0], X_2D[1], angles='xy', scale_units='xy', scale=1, color='r', label='Vector X')
plt.quiver(*origin, Y_2D[0], Y_2D[1], angles='xy', scale_units='xy', scale=1, color='b', label='Vector Y')
plt.xlim(-0.1, 0.6)
plt.ylim(-0.1, 0.6)
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.title(f"Similitud Coseno: {similarity:.4f}")
plt.xlabel("Componente 1")
plt.ylabel("Componente 2")
plt.show()
