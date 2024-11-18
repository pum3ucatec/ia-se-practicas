import numpy as np
from scipy.spatial import distance_matrix
import pandas as pd
import matplotlib.pyplot as plt

puntos = {
    "A1": (50, 32),
    "A2": (8, 65),
    "A3": (84, 45),
    "B1": (37, 32),
    "B2": (96, 92),
    "B3": (91, 74),
    "C1": (16, 67),
    "C2": (45, 1),
    "C3": (76, 84),
    "D1": (45, 43),
    "D2": (34, 23),
    "D3": (22, 48),
    "E1": (2, 53),
    "E2": (86, 34),
    "E3": (1, 71),
    "F1": (39, 10),
    "F2": (23, 45),
    "F3": (53, 18),
    "G1": (29, 17),
    "G2": (73, 95),
    "G3": (35, 91),
    "H1": (53, 50),
    "H2": (73, 31),
    "H3": (20, 9),
    "I1": (20, 75),
    "I2": (29, 66),
    "I3": (12, 92),
    "J1": (45, 8),
    "J2": (70, 32),
    "J3": (11, 74)
}

# def length(puntos):
    # return len(puntos)
# print(length(puntos))

#Asignacion de coordenadas y nombres
coordenadas = np.array(list(puntos.values()))
nombres = list(puntos.keys())

#Distancias
distancias = distance_matrix(coordenadas, coordenadas)
def_dist  = pd.DataFrame(distancias, columns=nombres, index=nombres)

#Imprimir la distancia entre los puntos
print("Distancia entre puntos:")
print(def_dist)

#Umbral y Cluster
umbral = 3.2
cluster = []
vistitados = set()

#CLusters
for i, nom_fila in enumerate(nombres):
    if nom_fila in vistitados:
        continue
    new_cluster = [nom_fila]
    vistitados.add(nom_fila)
    for j, nom_col in enumerate(nombres):
        if i != j and distancias[i, j] <= umbral:
            if nom_col not in vistitados:
                new_cluster.append(nom_col)
                vistitados.add(nom_col)
    cluster.append(new_cluster)

print(f"\nClusters formados con umbral de distancia {umbral}:")
for i, cluster in enumerate(cluster, 1):
    print(f"Cluster {i}: {', '.join(cluster)}")

#Imprimir gráfica
plt.figure(figsize=(15, 13))
for i, nombre in enumerate(nombres):
    x, y = coordenadas[i]
    plt.scatter(x, y, label=f'{nombre} ({x}, {y})')
    plt.text(x + 0.2, y + 0.2, nombre, fontsize=12)
plt.xlabel("Coordenada X")
plt.ylabel("Coordenada Y")
plt.title("Distribución de Puntos en Coordenadas")
plt.legend()
plt.grid(True)
plt.savefig("Grafica_Puntos_Practica2.png")