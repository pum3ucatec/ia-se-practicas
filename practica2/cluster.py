import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from scipy.spatial.distance import pdist, squareform

# 1. Crear 30 puntos aleatorios en 2D
np.random.seed(42)  # Fijar semilla para reproducibilidad
points = np.random.rand(30, 2)

# 2. Calcular la matriz de distancias
distances = squareform(pdist(points))

# 3. Aplicar clustering (K-means) con 3 clusters
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(points)

# 4. Visualizar los resultados
plt.figure(figsize=(8, 6))
plt.scatter(points[:, 0], points[:, 1], c=clusters, cmap='viridis', s=50)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='red', marker='X', s=200, label='Centroides')
plt.title("Clustering K-means de 30 puntos")
plt.xlabel("Coordenada X")
plt.ylabel("Coordenada Y")
plt.legend()
plt.grid()
plt.show()

# Imprimir resultados
print("Matriz de distancias:")
print(distances)

print("\nPuntos agrupados por cluster:")
for i in range(3):
    print(f"Cluster {i}: {points[clusters == i]}")
