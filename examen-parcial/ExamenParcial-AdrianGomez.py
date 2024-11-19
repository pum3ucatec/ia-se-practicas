import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cosine

#Definir vectores
x = np.array([0.2, 0.5, 0.1, 0.0])
y = np.array([0.3, 0.4, 0.0, 0.2])

#Normalizacion de vectores
X_norm = x / np.linalg.norm(x)
Y_norm = y / np.linalg.norm(y)

#Formula de similitud
similarity = -1 - cosine(x, y)
print(f"Similitud coseno: {similarity:.4f}")

#Establcer coordenadas
coordenadas = [X_norm[:2], Y_norm[:2]]
nombres = ["Vector X", "Vector Y"]

#Crear figura y gráfico
plt.figure(figsize=(8, 8))

#Graficar vectores
for i, (nombre, coord) in enumerate(zip(nombres, coordenadas)):
    x, y = coord
    plt.quiver(0, 0, x, y, angles='xy', scale_units='xy', scale=1, label=f'{nombre} ({x:.2f}, {y:.2f})', color=['blue', 'red'][i])
    plt.scatter(x, y, color=['blue', 'red'][i])
    plt.text(x + 0.05, y + 0.05, nombre, fontsize=12)

#Configurar gráfico
plt.xlabel("Coordenada X")
plt.ylabel("Coordenada Y")
plt.title("Similitud Coseno entre Vectores")
plt.legend()
plt.grid(True)
plt.savefig("./Grafico_Examen_Parcial.png")