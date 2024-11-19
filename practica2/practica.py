import matplotlib.pyplot as plt
import random
import math

# Función para calcular la distancia entre dos puntos (x1, y1) y (x2, y2)
def calcular_distancia(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Función para generar puntos aleatorios únicos
def generar_puntos_unicos(cantidad, x_min, x_max, y_min, y_max):
    puntos = {}
    while len(puntos) < cantidad:
        # Generar coordenadas aleatorias
        x = random.randint(x_min, x_max)
        y = random.randint(y_min, y_max)
        # Crear un nombre único basado en la cantidad de puntos
        nombre = chr(65 + len(puntos)) if len(puntos) < 26 else f"A{len(puntos)-26+1}"
        if (x, y) not in puntos.values():  # Verificar que no se repita
            puntos[nombre] = (x, y)
    return puntos

# Generar 30 puntos aleatorios únicos
puntos = generar_puntos_unicos(30, 0, 10, 0, 10)

# Extraer nombres y coordenadas de los puntos
nombres = list(puntos.keys())
coordenadas = list(puntos.values())

# Imprimir los puntos generados
print("Puntos generados:")
for nombre, coord in puntos.items():
    print(f"{nombre}: {coord}")

# Calcular y mostrar las distancias entre cada par de puntos
print("\nDistancias entre los puntos:")
distancias = []
for i in range(len(coordenadas)):
    for j in range(i + 1, len(coordenadas)):
        distancia = calcular_distancia(coordenadas[i], coordenadas[j])
        distancias.append((nombres[i], nombres[j], distancia))
        print(f"Distancia entre {nombres[i]} y {nombres[j]}: {distancia:.2f}")

# Crear una figura y un gráfico de dispersión
plt.figure(figsize=(12, 12))

# Graficar cada punto y etiquetarlo
for i, nombre in enumerate(nombres):
    x, y = coordenadas[i]
    plt.scatter(x, y, label=f'{nombre} ({x}, {y})')
    # Desplazar las etiquetas hacia la derecha del punto (x+0.2)
    plt.text(x + 0.2, y, nombre, fontsize=12)

# Configurar el gráfico
plt.xlabel("Coordenada X")
plt.ylabel("Coordenada Y")
plt.title("Puntos aleatorios sin repeticiones")
plt.grid(True)

# Mover la leyenda a la derecha del gráfico
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Mostrar el gráfico
# plt.show()

# Guardar el gráfico
plt.savefig("Grafico_practica2.png")
