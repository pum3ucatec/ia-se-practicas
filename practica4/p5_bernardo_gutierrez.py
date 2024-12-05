# Instalación de bibliotecas necesarias
!pip install nltk pandas matplotlib requests --quiet

# Importar bibliotecas
import nltk
from nltk.util import ngrams
from nltk.probability import FreqDist
import pandas as pd
import matplotlib.pyplot as plt
import requests

# Descargar recursos necesarios de NLTK
nltk.download('punkt')
nltk.download('punkt_tab') # Download the missing 'punkt_tab' package

# Cargar el texto del libro desde la URL
url = "https://www.gutenberg.org/files/11/11-0.txt"  # Ejemplo: "Alicia en el país de las maravillas"
response = requests.get(url)
response.encoding = "utf-8"  # Establecer la codificación correcta
texto_completo = response.text

# Tokenizar el texto
tokens = nltk.word_tokenize(texto_completo)

# Función para generar n-gramas
def generar_ngrams(tokens, n):
    return list(ngrams(tokens, n))

# Generar bigramas (n=2)
bigramas = generar_ngrams(tokens, 2)

# Mostrar los primeros 10 bigramas
print("Primeros 10 bigramas:")
print(bigramas[:10])

# Generar trigramas (n=3)
trigramas = generar_ngrams(tokens, 3)

# Mostrar los primeros 10 trigramas
print("\nPrimeros 10 trigramas:")
print(trigramas[:10])

# Generar frecuencia de bigramas
freq_bigramas = FreqDist(bigramas)

# Gráfica de bigramas más frecuentes
bigramas_mas_frecuentes = freq_bigramas.most_common(10)
plt.figure(figsize=(10, 5))
plt.bar([" ".join(b) for b, _ in bigramas_mas_frecuentes], [c for _, c in bigramas_mas_frecuentes])
plt.xticks(rotation=45)
plt.xlabel("Bigramas más frecuentes")
plt.ylabel("Frecuencia")
plt.title("Bigramas más frecuentes")
plt.show()

# Generar frecuencia de trigramas
freq_trigramas = FreqDist(trigramas)

# Gráfica de trigramas más frecuentes
trigramas_mas_frecuentes = freq_trigramas.most_common(10)
plt.figure(figsize=(10, 5))
plt.bar([" ".join(t) for t, _ in trigramas_mas_frecuentes], [c for _, c in trigramas_mas_frecuentes])
plt.xticks(rotation=45)
plt.xlabel("Trigramas más frecuentes")
plt.ylabel("Frecuencia")
plt.title("Trigramas más frecuentes")
plt.show()

# Tarea adicional: cambiar la longitud de n-gramas
n = 4  # Cambia este valor para generar 4-gramas o 5-gramas
ngrams_personalizados = generar_ngrams(tokens, n)
freq_ngrams_personalizados = FreqDist(ngrams_personalizados)

# Gráfica de n-gramas personalizados más frecuentes
ngrams_mas_frecuentes = freq_ngrams_personalizados.most_common(10)
plt.figure(figsize=(10, 5))
plt.bar([" ".join(n) for n, _ in ngrams_mas_frecuentes], [c for _, c in ngrams_mas_frecuentes])
plt.xticks(rotation=45)
plt.xlabel(f"{n}-gramas más frecuentes")
plt.ylabel("Frecuencia")
plt.title(f"{n}-gramas más frecuentes")
plt.show()
