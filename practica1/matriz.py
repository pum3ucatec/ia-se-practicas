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
    "F": (3, 9),
    "G": (4, 8),
    "H": (7, 2),
    "I": (9, 6),
    "J": (5, 7),
    "K": (3, 4),
    "L": (6, 1),
    "M": (8, 8),
    "N": (2, 6),
    "O": (4, 3),
    "P": (9, 9),
    "Q": (7, 5),
    "R": (1, 8),
    "S": (3, 1),
    "T": (6, 9),
    "U": (5, 3),
    "V": (8, 7),
    "W": (2, 2),
    "X": (7, 8),
    "Y": (9, 1),
    "Z": (1, 5),
    "AA": (4, 6),
    "AB": (3, 7),
    "AC": (6, 8),
    "AD": (5, 5)
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
<<<<<<< HEAD
plt.savefig("Grafico.png")
=======
plt.savefig("Grafica_Matriz.png")
>>>>>>> origin/master
