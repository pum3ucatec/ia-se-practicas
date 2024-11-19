import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance_matrix


np.random.seed(0) 
puntos = {f"P{i+1}": (np.random.uniform(0, 10), np.random.uniform(0, 10)) for i in range(30)}


nombres = list(puntos.keys())
coordenadas = np.array(list(puntos.values()))


distancias = distance_matrix(coordenadas, coordenadas)

# Definir un umbral de distancia para formar los clusters
umbral = 2.5 
clusters = []
visitados = set()

# Crear los clusters basados en el umbral de distancia
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
print("\nClusters formados con un umbral de distancia de 2.5:")
for i, cluster in enumerate(clusters, 1):
    print(f"Cluster {i}: {', '.join(cluster)}")


plt.figure(figsize=(10, 8))

colores = plt.cm.get_cmap("tab20", len(clusters))


for i, cluster in enumerate(clusters):
    color = colores(i)
    for nombre in cluster:
        x, y = puntos[nombre]
        plt.scatter(x, y, color=color, label=nombre if nombre == cluster[0] else "", s=50)
        plt.text(x + 0.2, y + 0.2, nombre, fontsize=9, color=color)

plt.xlabel("Coordenada X")
plt.ylabel("Coordenada Y")
plt.title("Distribución de Puntos y sus Clusters")
plt.legend(loc='upper left', fontsize=8)
plt.grid(True)

plt.savefig("grafico-practica2.png")

plt.show()
