# Práctica de NLP con Python y Google Colab para n-gramas

Objetivo
Analizar el texto de un libro y generar n-gramas para entender la estructura del lenguaje.

Requisitos
- Cuenta de Google Colab
- Conocimientos básicos de Python y NLP
- Librerías necesarias: nltk, pandas, matplotlib

Código

import nltk
from nltk.util import ngrams
import pandas as pd
import matplotlib.pyplot as plt

# Cargar el texto del libro
url = "(link unavailable)"
texto = pd.read_csv(url, header=None, names=["texto"])

# Tokenizar el texto
tokens = nltk.word_tokenize(texto["texto"].iloc[0])

# Generar n-gramas
ngramas = ngrams(tokens, 2)  # 2-gramas

# Mostrar los 10 primeros n-gramas
print(list(ngramas)[:10])

# Generar n-gramas de longitud 3
ngramas_3 = ngrams(tokens, 3)

# Mostrar los 10 primeros n-gramas de longitud 3
print(list(ngramas_3)[:10])

``` bash
# Gráfica de frecuencia de n-gramas

freq_ngramas = nltk.FreqDist(ngramas)
plt.bar(freq_ngramas.keys(), freq_ngramas.values())
plt.xlabel("N-gramas")
plt.ylabel("Frecuencia")
plt.title("Frecuencia de n-gramas")
plt.show()
```

``` bash
# Gráfica de distribución de frecuencias de n-gramas
plt.hist(freq_ngramas.values(), bins=10)
plt.xlabel("Frecuencia")
plt.ylabel("Cantidad")
plt.title("Distribución de frecuencias de n-gramas")
plt.show()
```

``` bash
# Gráfica de n-gramas más frecuentes
ngramas_más_frecuentes = freq_ngramas.most_common(10)
plt.bar([ngrama[0] for ngrama in ngramas_más_frecuentes], [ngrama[1] for ngrama in ngramas_más_frecuentes])
plt.xlabel("N-gramas más frecuentes")
plt.ylabel("Frecuencia")
plt.title("N-gramas más frecuentes")
plt.show()
```

Explicación

1. Cargamos el texto del libro "Alicia en el país de las maravillas" desde un repositorio de GitHub o de otro lugar.
2. Tokenizamos el texto utilizando la función word_tokenize de NLTK.
3. Generamos n-gramas de longitud 2 utilizando la función ngrams de NLTK.
4. Mostramos los 10 primeros n-gramas.
5. Generamos n-gramas de longitud 3 y mostramos los 10 primeros.
6. Creamos una gráfica de frecuencia de n-gramas utilizando la función FreqDist de NLTK y la biblioteca matplotlib.
7. Creamos una gráfica de distribución de frecuencias de n-gramas utilizando la función hist de matplotlib.
8. Creamos una gráfica de n-gramas más frecuentes utilizando la función most_common de FreqDist y la biblioteca matplotlib.

Tareas

1. Cambia la longitud de los n-gramas a 4 o 5 y observa cómo cambia la salida.
2. Utiliza la función FreqDist de NLTK para calcular la frecuencia de cada n-grama.
3. Utiliza la función plot de matplotlib para visualizar la distribución de frecuencias de los n-gramas.

Recursos adicionales

- Documentación de NLTK: (link unavailable)
- Tutorial de NLP con Python: (link unavailable)
- Documentación de matplotlib: (link unavailable)

## Entregables
- Subir a la plataforma
- Subir a este repositorio creando una rama `P5-GastonQuelali` el archivo de Google Colab
