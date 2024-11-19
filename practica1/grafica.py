import matplotlib.pyplot as plt

# Definir los puntos con sus coordenadas en el plano 2D
puntos = {
    "A": (2, 3),
    "B": (5, 1),
    "C": (8, 3),
    "D": (1, 7),
    "E": (6, 5)
}

# Extraer nombres y coordenadas de los puntos
nombres = list(puntos.keys())
coordenadas = list(puntos.values())
print (Nombres)
print (coordenadas)
# Crear una figura y un gráfico de dispersión
plt.figure(figsize=(8, 6))

# Graficar cada punto y etiquetarlo
for i, nombre in enumerate(nombres):
    x, y = coordenadas[i]
    plt.scatter(x, y, label=f'{nombre} ({x}, {y})')
    plt.text(x + 0.2, y + 0.2, nombre, fontsize=12)

# Configurar el gráfico
plt.xlabel("Coordenada X")
plt.ylabel("Coordenada Y")
plt.title("Simulación de puntos en coordenadas")
plt.legend()
plt.grid(True)
# plt.show()
plt.savefig("Grafico.png")
