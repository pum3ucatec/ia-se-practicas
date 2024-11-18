import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial import distance_matrix
import matplotlib.pyplot as plt

# Crear 30 puntos aleatorios en 2D
np.random.seed(42)  # Fijar la semilla para reproducibilidad
puntos = np.random.rand(30, 2) * 100  # Coordenadas en un rango de 0 a 100

# Calcular la matriz de distancias entre puntos
distancias = distance_matrix(puntos, puntos)

# Mostrar la matriz de distancias
print("Matriz de Distancias:")
print(np.round(distancias, 2))

# Realizar clustering (usando k-means con 3 clusters)
kmeans = KMeans(n_clusters=3, random_state=42).fit(puntos)
etiquetas = kmeans.labels_

# Visualizar los clusters
plt.figure(figsize=(8, 6))
for cluster in range(3):
    cluster_puntos = puntos[etiquetas == cluster]
    plt.scatter(cluster_puntos[:, 0], cluster_puntos[:, 1], label=f'Cluster {cluster}')
    
# Agregar centros de los clusters
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], 
            c='black', marker='X', s=100, label='Centroides')
plt.title('Clustering de Puntos')
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')
plt.legend()
plt.show()
