import numpy as np
import matplotlib.pyplot as plt

def calcular_similitud_coseno(X, Y):
    #SIMILUTUD DE COSENOS
    dot_product = np.dot(X, Y)
    magnitude_X = np.linalg.norm(X)
    magnitude_Y = np.linalg.norm(Y)
    return dot_product / (magnitude_X * magnitude_Y)

def graficar_vectores(X, Y):
    # Asegurar que los vectores tengan tres dimensiones
    X_vis = np.append(X, 0) if len(X) < 3 else X
    Y_vis = np.append(Y, 0) if len(Y) < 3 else Y

    # SIMILITUD COSENO
    similarity = calcular_similitud_coseno(X, Y)

    # CREA LA FIGURA EN 3D
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    # PUNTO DE ORIGEN
    origin = np.array([0, 0, 0])

    #FLECHAS
    ax.plot([origin[0], X_vis[0]], [origin[1], X_vis[1]], [origin[2], X_vis[2]], color='r', label='Vector X')
    ax.plot([origin[0], Y_vis[0]], [origin[1], Y_vis[1]], [origin[2], Y_vis[2]], color='b', label='Vector Y')

    # Configuración de los ejes
    ax.set_xlim([0, max(0.6, X_vis[0], Y_vis[0])])
    ax.set_ylim([0, max(0.6, X_vis[1], Y_vis[1])])
    ax.set_zlim([0, max(0.6, X_vis[2], Y_vis[2])])
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')

    # TITULO Y ESTILO DE TITULO
    ax.set_title(f"Similitud Coseno: {similarity:.2f}", fontsize=14)
    ax.legend()

    plt.show()

# EJEMPLO PRACTICO DE CLASE SE PUEDE CAMBIAR

X = np.array([0.2, 0.5, 0.1, 0.0])
Y = np.array([0.3, 0.4, 0.0, 0.2])

# ESTO GRAFICA NO QUITAR
graficar_vectores(X, Y)
