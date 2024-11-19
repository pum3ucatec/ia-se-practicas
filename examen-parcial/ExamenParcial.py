import numpy as np
import matplotlib.pyplot as plt

# Definir los vectores X e Y
X = np.array([0.2, 0.5, 0.1, 0.0])
Y = np.array([0.3, 0.4, 0.0, 0.2])

# Función para calcular la similitud coseno
def calcular_similitud_coseno(X, Y):
    numerador = np.dot(X, Y)  # Producto punto entre X e Y
    denominador = np.sqrt(np.dot(X, X)) * np.sqrt(np.dot(Y, Y))  # Magnitudes de X e Y
    return numerador / denominador

# Calcular la similitud coseno
similitud = calcular_similitud_coseno(X, Y)
print(f"Similitud coseno entre X e Y: {similitud:.4f}")

# Graficar los vectores en un espacio 2D para representación visual
plt.figure(figsize=(8, 6))

# Representación de los vectores
plt.quiver(0, 0, X[0], X[1], angles='xy', scale_units='xy', scale=1, color='blue', label='Vector X')
plt.quiver(0, 0, Y[0], Y[1], angles='xy', scale_units='xy', scale=1, color='orange', label='Vector Y')

# Ajustar límites del gráfico
plt.xlim(-0.5, 1)
plt.ylim(-0.5, 1)

# Agregar título y etiquetas
plt.title(f"Similitud Coseno: {similitud:.4f}", fontsize=14)
plt.xlabel("Dimensión 1")
plt.ylabel("Dimensión 2")
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)

# Agregar leyenda
plt.legend()

# Mostrar el gráfico
plt.grid()
plt.show()
