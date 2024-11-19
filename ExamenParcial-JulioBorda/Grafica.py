import numpy as np
import matplotlib.pyplot as plt

def plot_and_save_graph():
    # Datos de ejemplo
    x = np.linspace(0, 10, 100)  # 100 puntos entre 0 y 10
    y1 = np.sin(x)                # Seno de x
    y2 = np.cos(x)                # Coseno de x

    # Crear la figura y los ejes
    plt.figure(figsize=(10, 6))

    # Graficar los datos
    plt.plot(x, y1, label='Seno', color='red')
    plt.plot(x, y2, label='Coseno', color='blue')

    # Añadir título y etiquetas
    plt.title('Gráfico de Seno y Coseno')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    
    # Añadir leyenda
    plt.legend()

    # Guardar el gráfico como 'grafico.png'
    plt.savefig('grafico.png', dpi=300, bbox_inches='tight')  # Guardar con alta resolución
    plt.close()  # Cerrar la figura para liberar memoria

# Llamar a la función para crear y guardar el gráfico
plot_and_save_graph()
print("El gráfico ha sido guardado como 'grafico.png'.")
