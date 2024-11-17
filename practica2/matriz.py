import numpy as np
from scipy.spatial import distance_matrix
import pandas as pd
import matplotlib.pyplot as plt

# Definir los puntos con sus coordenadas en el plano 2D
puntos = {
    "A": (2, 3),
    "B": (5, 1),
    "C": (8, 3),
    "D": (1, 7),
    "E": (6, 5),
    "F": (4, 1),
    "G": (7, 2),
    "H": (2, 8),
    "I": (8, 1),
    "J": (5, 5),
    "K": (6, 7),
    "L": (5, 1),
    "M": (9, 3),
    "N": (9, 7),
    "Ñ": (10, 5),
    "O": (-5, 3),
    "P": (-5, 1),
    "Q": (-8, 3),
    "R": (1, -7),
    "S": (6, -5),
    "T": (2, -3),
    "U": (5, -1),
    "V": (-10, -3),
    "W": (-2, -2),
    "X": (-8, -5),
    "Y": (-10, -3),
    "Z": (-5, 10),
    "1": (6, -6),
    "2": (-3, -8)
}

# Extraer nombres y coordenadas de los puntos
nombres = list(puntos.keys())
coordenadas = np.array(list(puntos.values()))

# Calcular la matriz de distancias
distancias = distance_matrix(coordenadas, coordenadas)
df_distancias = pd.DataFrame(distancias, index=nombres, columns=nombres)

# Mostrar la matriz de distancias
print("Matriz de distancias entre puntos:")
print(df_distancias)

# Definir un umbral de distancia para formar clusters
umbral = 4.5
clusters = []
visitados = set()

# Crear clusters en base al umbral de distancia
for i, nombre_fila in enumerate(nombres):
    if nombre_fila in visitados:
        continue
    nuevo_cluster = [nombre_fila]
    visitados.add(nombre_fila)
    for j, nombre_col in enumerate(nombres):
        if i != j and distancias[i, j] <= umbral:
            if nombre_col not in visitados:
                nuevo_cluster.append(nombre_col)
                visitados.add(nombre_col)
    clusters.append(nuevo_cluster)

# Mostrar los clusters formados
print("\nClusters formados con umbral de distancia 4.5:")
for i, cluster in enumerate(clusters, 1):
    print(f"Cluster {i}: {', '.join(cluster)}")

# Visualizar los puntos y los clusters en un gráfico
plt.figure(figsize=(8, 6))
for i, nombre in enumerate(nombres):
    x, y = coordenadas[i]
    plt.scatter(x, y, label=f'{nombre} ({x}, {y})')
    plt.text(x + 0.2, y + 0.2, nombre, fontsize=12)
plt.xlabel("Coordenada X")
plt.ylabel("Coordenada Y")
plt.title("Distribución de Puntos en Coordenadas")
plt.legend()
plt.grid(True)
#plt.show()
plt.savefig("Grafica_Matriz.png")
