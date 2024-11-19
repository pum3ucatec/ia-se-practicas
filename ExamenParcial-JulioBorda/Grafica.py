import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt

def cosine_similarity(vec1, vec2):
    """Calcula la similitud coseno entre dos vectores."""
    dot_product = np.dot(vec1, vec2)
    norm_a = np.linalg.norm(vec1)
    norm_b = np.linalg.norm(vec2)
    if norm_a == 0 or norm_b == 0:
        return 0.0  # Evitar división por cero
    return dot_product / (norm_a * norm_b)

def plot_vectors(vec1, vec2):
    """Grafica los dos vectores en un gráfico 2D."""
    plt.figure()
    origin = np.array([0, 0])  # Origen para los vectores

    plt.quiver(*origin, vec1[0], vec1[1], angles='xy', scale_units='xy', scale=1, color='r', label='Vector 1')
    plt.quiver(*origin, vec2[0], vec2[1], angles='xy', scale_units='xy', scale=1, color='b', label='Vector 2')

    # Configuración del gráfico
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    plt.axhline(0, color='black',linewidth=0.5, ls='--')
    plt.axvline(0, color='black',linewidth=0.5, ls='--')
    plt.grid()
    plt.title('Visualización de Vectores')
    plt.legend()
    plt.show()

def calculate_similarity():
    """Obtiene los vectores de las entradas y calcula la similitud."""
    try:
        # Obtener los valores de los campos de entrada
        vec1 = list(map(float, entry_vec1.get().split(',')))
        vec2 = list(map(float, entry_vec2.get().split(',')))

        # Asegurarse de que los vectores tengan la misma dimensión
        if len(vec1) != len(vec2):
            messagebox.showerror("Error", "Los vectores deben tener la misma dimensión.")
            return
        
        # Calcular similitud coseno
        similarity = cosine_similarity(np.array(vec1), np.array(vec2))
        
        # Mostrar el resultado
        messagebox.showinfo("Resultado", f"Similitud Coseno: {similarity:.4f}")

        # Graficar los vectores
        plot_vectors(np.array(vec1), np.array(vec2))

    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese números válidos separados por comas.")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Calculadora de Similitud Coseno")

# Etiquetas y campos de entrada
label_vec1 = tk.Label(root, text="Ingrese el vector 1 (ej: 0.2,0.5):")
label_vec1.pack()

entry_vec1 = tk.Entry(root)
entry_vec1.pack()

label_vec2 = tk.Label(root, text="Ingrese el vector 2 (ej: 0.3,0.4):")
label_vec2.pack()

entry_vec2 = tk.Entry(root)
entry_vec2.pack()

# Botón para calcular la similitud
button_calculate = tk.Button(root, text="Calcular Similitud", command=calculate_similarity)
button_calculate.pack()

# Ejecutar la aplicación
root.mainloop()
