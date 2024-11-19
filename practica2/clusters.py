import numpy as np
from scipy.spatial.distance import pdist, squareform
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Generar 30 puntos aleatorios en 2D
np.random.seed(42)  # Para reproducibilidad
puntos = np.random.rand(30, 2)

# Calcular las distancias entre todos los puntos
distancias = squareform(pdist(puntos))

# Mostrar la matriz de distancias
print("Matriz de distancias:")
print(distancias)

# Visualizar los puntos generados
plt.scatter(puntos[:, 0], puntos[:, 1], c='blue', label='Puntos')
plt.title("30 Puntos Aleatorios")
plt.xlabel("Coordenada X")
plt.ylabel("Coordenada Y")
plt.legend()
plt.show()

# Calcular los clusters utilizando KMeans (por ejemplo, 3 clusters)
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(puntos)
etiquetas = kmeans.labels_

# Mostrar las etiquetas de los clusters
print("Etiquetas de clusters:")
print(etiquetas)

# Visualizar los clusters generados por KMeans
plt.scatter(puntos[:, 0], puntos[:, 1], c=etiquetas, cmap='viridis', label='Clusters')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='red', marker='x', label='Centroides')
plt.title("Clusters de los Puntos")
plt.xlabel("Coordenada X")
plt.ylabel("Coordenada Y")
plt.legend()
plt.show()