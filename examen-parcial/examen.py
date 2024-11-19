import numpy as np
import matplotlib.pyplot as plt

# Vectores del ejemplo práctico
X = np.array([0.2, 0.5, 0.1, 0.0])
Y = np.array([0.3, 0.4, 0.0, 0.2])

# Función para calcular la similitud coseno
def similitud_coseno(vec1, vec2):
    numerador = np.dot(vec1, vec2)
    denominador = np.linalg.norm(vec1) * np.linalg.norm(vec2)
    return numerador / denominador

# Calcular la similitud coseno
similitud = similitud_coseno(X, Y)
print(f"Similitud coseno entre X y Y: {similitud:.4f}")

# Graficar los vectores X y Y en 2D
plt.figure(figsize=(8, 6))

# Normalizar los vectores para graficarlos
X_norm = X / np.linalg.norm(X)
Y_norm = Y / np.linalg.norm(Y)

# Dibujar los vectores
plt.quiver(0, 0, X_norm[0], X_norm[1], angles='xy', scale_units='xy', scale=1, color='blue', label='Vector X (Normalizado)')
plt.quiver(0, 0, Y_norm[0], Y_norm[1], angles='xy', scale_units='xy', scale=1, color='red', label='Vector Y (Normalizado)')

# Dibujar el ángulo entre los vectores
angle = np.arccos(similitud)
plt.text(0.1, 0.4, f"Ángulo: {np.degrees(angle):.2f}°", fontsize=12, color="green")

plt.xlim(-0.5, 1)
plt.ylim(-0.5, 1)
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.title("Similitud Coseno: Representación de los Vectores")
plt.xlabel("Componente X1")
plt.ylabel("Componente X2")
plt.legend()
plt.tight_layout()
plt.savefig("Similitud_Coseno_Vectores.png")

