import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist, squareform
from sklearn.cluster import KMeans

# Paso 1: Crear 30 puntos aleatorios en un espacio 2D
np.random.seed(42)  # Fijar semilla para reproducibilidad
points = np.random.rand(30, 2)  # 30 puntos en 2 dimensiones

# Paso 2: Calcular la matriz de distancias (Euclídea)
distances = squareform(pdist(points, metric='euclidean'))

# Paso 3: Aplicar clustering (usaremos KMeans con 3 clusters como ejemplo)
num_clusters = 3
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
labels = kmeans.fit_predict(points)

# Paso 4: Visualización
plt.figure(figsize=(10, 8))

# Dibujar los puntos con colores por cluster
for i in range(num_clusters):
    cluster_points = points[labels == i]
    plt.scatter(cluster_points[:, 0], cluster_points[:, 1], label=f'Cluster {i+1}')

# Marcar los centroides
centroids = kmeans.cluster_centers_
plt.scatter(centroids[:, 0], centroids[:, 1], s=200, c='black', marker='X', label='Centroides')

# Etiquetas y leyendas
plt.title('Clustering y distancias de puntos', fontsize=16)
plt.xlabel('Coordenada X', fontsize=12)
plt.ylabel('Coordenada Y', fontsize=12)
plt.grid(True)
plt.legend()
plt.show()

# Paso 5: Mostrar distancias (opcional, imprimir la matriz)
print("Matriz de distancias (Euclídea) entre los puntos:")
print(distances)
