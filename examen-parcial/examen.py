import numpy as np
from scipy.spatial.distance import cosine
import matplotlib.pyplot as plt

# Vectores de ejemplo (TF-IDF de dos documentos)
X = np.array([0.2, 0.5, 0.1, 0.0])
Y = np.array([0.3, 0.4, 0.0, 0.2])

# Calcular la similitud coseno
cos_sim = 1 - cosine(X, Y) 

# Mostrar el resultado de la similitud coseno
print(f"Similitud coseno entre X y Y: {cos_sim:.4f}")

# Graficar los vectores X y Y
plt.figure(figsize=(8, 6))

# Graficamos los vectores X y Y en un espacio 2D (debido a la baja dimensionalidad de nuestros vectores)
plt.quiver(0, 0, X[0], X[1], angles='xy', scale_units='xy', scale=1, color='r', label='Vector X')
plt.quiver(0, 0, Y[0], Y[1], angles='xy', scale_units='xy', scale=1, color='b', label='Vector Y')

# Configuraciones del gráfico
plt.xlim(-0.1, 0.5)
plt.ylim(-0.1, 0.5)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(True)
plt.xlabel("Componente 1")
plt.ylabel("Componente 2")
plt.title(f"Similitud Coseno: {cos_sim:.4f}")
plt.legend()

# Guardar la imagen
plt.savefig("grafico-examen.png")  

# Mostrar el gráfico
plt.show()
