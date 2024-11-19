import numpy as np
import matplotlib.pyplot as plt

# Definir los vectores
X = np.array([0.2, 0.5, 0.1, 0.0])
Y = np.array([0.3, 0.4, 0.0, 0.2])

# Calcular la similitud coseno
similaridad = np.dot(X, Y) / (np.linalg.norm(X) * np.linalg.norm(Y))
print(f"Similitud coseno: {similaridad:.4f}")

# Reducir a un espacio 2D para graficar (usamos las dos primeras dimensiones para visualizar)
X_2D = X[:2]
Y_2D = Y[:2]

# Crear una figura
plt.figure(figsize=(8, 6))

# Graficar los vectores en el plano 2D
plt.quiver(0, 0, X_2D[0], X_2D[1], angles='xy', scale_units='xy', scale=1, color='blue', label=f'Vector X: {X_2D}')
plt.quiver(0, 0, Y_2D[0], Y_2D[1], angles='xy', scale_units='xy', scale=1, color='red', label=f'Vector Y: {Y_2D}')

# Configurar el gráfico
plt.xlim(-0.1, 0.6)
plt.ylim(-0.1, 0.6)
plt.xlabel("Dimensión X")
plt.ylabel("Dimensión Y")
plt.title(f"Similitud Coseno: {similaridad:.4f}")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()

# Guardar el gráfico en un archivo
plt.savefig("Grafico_coseno.png")
print("Gráfico guardado como 'Grafico.png'")
