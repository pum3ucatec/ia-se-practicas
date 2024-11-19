import numpy as np
from scipy.spatial import distance_matrix
import pandas as pd
import matplotlib.pyplot as plt

# aqui se ponen los puntos
puntos = {
    "A": (2, 3), "B": (5, 1), "C": (8, 3), "D": (1, 7), "E": (6, 5),
    "F": (9, 7), "G": (3, 2), "H": (10, 15), "I": (12, 8), "J": (14, 6),
    "K": (15, 10), "L": (18, 3), "M": (17, 15), "N": (2, 18), "O": (4, 12),
    "P": (8, 18), "Q": (5, 13), "R": (7, 9), "S": (3, 10), "T": (11, 11),
    "U": (19, 2), "V": (16, 12), "W": (0, 0), "X": (6, 16), "Y": (9, 3),
    "Z": (13, 17), "AA": (4, 4), "AB": (2, 9), "AC": (7, 14), "AD": (12, 2)
}


nombres = list(puntos.keys())
coordenadas = np.array(list(puntos.values()))

# Calcula distancia
distancias = distance_matrix(coordenadas, coordenadas)
df_distancias = pd.DataFrame(distancias, index=nombres, columns=nombres)

# print de la matriz
print("Matriz de distancias entre puntos:")
print(df_distancias)


umbral = 5.0  #umbral de los clusters
clusters = []
visitados = set()

# Crear clusters en base al umbral
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

# print los clusters
print("\nClusters formados con umbral de distancia 5.0:")
for i, cluster in enumerate(clusters, 1):
    print(f"Cluster {i}: {', '.join(cluster)}")

# grafico
plt.figure(figsize=(10, 8))
colores = plt.cm.rainbow(np.linspace(0, 1, len(clusters)))

for cluster, color in zip(clusters, colores):
    for nombre in cluster:
        idx = nombres.index(nombre)
        x, y = coordenadas[idx]
        plt.scatter(x, y, color=color, label=f"Cluster {clusters.index(cluster)+1}" if cluster.index(nombre) == 0 else "")
        plt.text(x + 0.2, y + 0.2, nombre, fontsize=10)

plt.xlabel("Coordenada X")
plt.ylabel("Coordenada Y")
plt.title("Distribución de Puntos y Clusters")
plt.legend(loc="upper right", fontsize=8, title="Clusters")
plt.grid(True)
plt.savefig("Cluster y distancia.png")
plt.show()
