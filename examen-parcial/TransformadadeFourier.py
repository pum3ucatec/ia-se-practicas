import numpy as np
import matplotlib.pyplot as plt

# aca puse los parametros de la ciudad
fs = 1000  # Frecuencia de muestreo de los HZ 
t = np.linspace(0, 1, fs, endpoint=False)  # Tiempo: 1 segundo, muestreado a 1000 Hz
freq1, freq2 = 50, 150  # Frecuencias de las señales (Hz)

# Crear señal, aca puse la combinación de dos ondas sinusoidales
signal = np.sin(2 * np.pi * freq1 * t) + 0.5 * np.sin(2 * np.pi * freq2 * t)

# Aca aplicop la Transformada de Fourier
fft_result = np.fft.fft(signal)  # Transformada rápida de Fourier
frequencies = np.fft.fftfreq(len(t), 1/fs)  # Frecuencias correspondientes

# Aca Filtrar las frecuencias positivas
positive_freqs = frequencies > 0
frequencies = frequencies[positive_freqs]
fft_magnitude = np.abs(fft_result[positive_freqs])  # Magnitud de las frecuencias

# Esta es la funcion de Visualización
plt.figure(figsize=(12, 6))

# Aca puse el Gráfico del dominio del tiempo
plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.title("Señal en el dominio del tiempo")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid()

# Aca puse Gráfico del dominio de la frecuencia
plt.subplot(2, 1, 2)
plt.plot(frequencies, fft_magnitude, color='r')
plt.title("Transformada de Fourier (Dominio de la frecuencia)")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.grid()

plt.tight_layout()
plt.show()
