import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist, squareform
from sklearn.cluster import KMeans
# 1. Generar 30 puntos aleatorios en un espacio 2D
np.random.seed(42)  # Para reproducibilidad
points = np.random.rand(30, 2)  # 30 puntos en un espacio 2D
# 2. Calcular las distancias entre cada par de puntos
distances = squareform(pdist(points))
# Imprimir la matriz de distancias (opcional)
print("Matriz de distancias:")
print(distances)
# 3. Realizar clustering con KMeans
num_clusters = 3  # Número de clusters
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
clusters = kmeans.fit_predict(points)
# 4. Visualizar los puntos y los clusters
plt.figure(figsize=(8, 6))
for cluster_id in range(num_clusters):
    cluster_points = points[clusters == cluster_id]
    plt.scatter(cluster_points[:, 0], cluster_points[:, 1], label=f'Cluster {cluster_id}') 
# Añadir los centros de los clusters
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], 
            c='red', marker='x', s=100, label='Centroides')
plt.title("Clustering de puntos")
plt.xlabel("Coordenada X")
plt.ylabel("Coordenada Y")
plt.legend()
plt.grid()
plt.show()