import numpy as np
from scipy.spatial import distance_matrix
import pandas as pd
import matplotlib.pyplot as plt

# Definir los puntos con sus coordenadas en el plano 2D
puntos = {
    "P1": (4,0), "P2": (5,0),
    "P3": (4,1), "P4": (5,1), "P5": (3,1), "P6": (2,1), "P7": (6,1), "P8": (7,1),
    "P9": (3,2), "P10": (6,2),
    "P11": (4,3), "P12": (5,3), "P13": (3,3), "P14": (2,3), "P15": (6,3), "P16": (7,3),
    "P17": (3,4), "P18": (6,4),
    "P19": (4,5), "P20": (5,5), "P21": (3,5), "P22": (2,5), "P23": (6,5), "P24": (7,5),
    "P25": (3,6), "P26": (6,6),
    "P27": (4,7), "P28": (5,7),
    "P29": (4.5,8),
    "P30": (4.5,9),
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
umbral = 1.5
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
print("\nClusters formados con umbral de distancia 1.5:")
for i, cluster in enumerate(clusters, 1):
    print(f"Cluster {i}: {', '.join(cluster)}")

# Visualizar los puntos y los clusters en un gráfico
plt.figure(figsize=(10, 8))
for i, nombre in enumerate(nombres):
    x, y = coordenadas[i]
    plt.scatter(x, y, label=nombre)
    plt.text(x + 0.1, y + 0.1, nombre, fontsize=9)

plt.xlabel("Coordenada X")
plt.ylabel("Coordenada Y")
plt.title("Practica 30 puntos con clusteres")
plt.grid(True)
plt.tight_layout()
plt.savefig("Grafica.png")