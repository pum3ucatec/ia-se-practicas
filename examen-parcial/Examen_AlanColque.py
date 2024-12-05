import numpy as np
import matplotlib.pyplot as plt

def calcular_similitud_coseno(X, Y):
    """
    Calcula la similitud coseno entre dos vectores.
    """
    dot_product = np.dot(X, Y)
    magnitude_X = np.linalg.norm(X)
    magnitude_Y = np.linalg.norm(Y)
    return dot_product / (magnitude_X * magnitude_Y)

def graficar_vectores(X, Y):
    """
    Grafica dos vectores en 3D y muestra su similitud coseno.
    """
    # Asegurar que los vectores tengan tres dimensiones
    X_vis = np.append(X, 0) if len(X) < 3 else X
    Y_vis = np.append(Y, 0) if len(Y) < 3 else Y

    # Calcular la similitud coseno
    similarity = calcular_similitud_coseno(X, Y)

    # Crear la figura y los ejes en 3D
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    # Origen
    origin = np.array([0, 0, 0])

    # Graficar vectores
    ax.plot([origin[0], X_vis[0]], [origin[1], X_vis[1]], [origin[2], X_vis[2]], color='r', label='Vector X')
    ax.plot([origin[0], Y_vis[0]], [origin[1], Y_vis[1]], [origin[2], Y_vis[2]], color='b', label='Vector Y')

    # Configuración de los ejes
    ax.set_xlim([0, max(0.6, X_vis[0], Y_vis[0])])
    ax.set_ylim([0, max(0.6, X_vis[1], Y_vis[1])])
    ax.set_zlim([0, max(0.6, X_vis[2], Y_vis[2])])
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')

    # Título y leyenda
    ax.set_title(f"Similitud Coseno: {similarity:.2f}", fontsize=14)
    ax.legend()

    plt.show()

# Ejemplo práctico
X = np.array([0.2, 0.5, 0.1, 0.0])
Y = np.array([0.3, 0.4, 0.0, 0.2])

# Llamar a la función para graficar
graficar_vectores(X, Y)
