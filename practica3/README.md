
# Introducción a NLP con Python y NLTK

## 1. Familiarización básica con Python
Antes de trabajar con corpus o NLP, los estudiantes deben estar cómodos con conceptos básicos de Python.

### Ejercicios:
1. Escribir un script que cuente el número de palabras en un texto simple.
2. Manipular cadenas: convertir texto a minúsculas, eliminar signos de puntuación.
3. Usar estructuras de datos básicas como listas y diccionarios para almacenar palabras y sus frecuencias.

---

## 2. Introducción a NLTK
Familiarizarse con la biblioteca **NLTK** y su instalación.

### Actividad:
1. Instalar **NLTK** en Google Colab:
   ```python
   !pip install nltk
   import nltk
   nltk.download('punkt')
   ```
2. Usar `nltk.word_tokenize` para dividir un texto en palabras.

### Ejemplo:
```python
from nltk.tokenize import word_tokenize

texto = "Natural Language Processing is fun!"
tokens = word_tokenize(texto)
print(tokens)
```

---

## 3. Trabajar con corpus
Explorar y manipular corpus utilizando NLTK.

### Corpus preinstalados en NLTK:
Descargar el corpus `nltk.book`:
```python
import nltk
nltk.download('gutenberg')  # Corpus Gutenberg
nltk.download('stopwords') # Palabras vacías

from nltk.corpus import gutenberg
print(gutenberg.fileids())  # Muestra los archivos disponibles
```

### Actividad:
1. Leer un corpus como *"Emma"* de Jane Austen:
   ```python
   texto = gutenberg.raw('austen-emma.txt')
   print(texto[:500])  # Muestra las primeras 500 letras
   ```
2. Contar las palabras únicas y su frecuencia.
   ```python
   from collections import Counter
   tokens = word_tokenize(texto)
   conteo = Counter(tokens)
   print(conteo.most_common(10))  # Top 10 palabras más frecuentes
   ```

---

## 4. Tokenización avanzada con expresiones regulares
Entender y personalizar tokenización usando expresiones regulares.

### Ejemplo:
```python
import re
from nltk.tokenize import regexp_tokenize

texto = "The price of oil is $123.45 today. U.S.A. stocks fell by 5%..."
pattern = r'''(?x)               
              (?:[A-Z]\.)+         # Abreviaciones como U.S.A.
              | \$?\d+(?:\.\d+)?%? # Monedas y porcentajes
              | \w+(?:-\w+)*       # Palabras con guiones
              | \.\.\.             # Elipsis
              | [][.,;"'?():-_`]   # Otros tokens individuales
            '''
tokens = regexp_tokenize(texto, pattern)
print(tokens)
```

### Ejercicio:
Crear un patrón que reconozca hashtags y menciones de Twitter, como `#NLP` o `@user123`.

---

## 5. Stopwords y limpieza de texto
Limpiar texto eliminando palabras irrelevantes ("stopwords").

### Ejemplo:
```python
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

tokens_limpios = [word for word in tokens if word.lower() not in stop_words]
print(tokens_limpios)
```

### Ejercicio:
Eliminar stopwords de un texto en español (requiere `stopwords.words('spanish')`).

---

## 6. Visualización de frecuencias
Crear gráficos de frecuencias de palabras para análisis visual.

### Ejemplo:
```python
import matplotlib.pyplot as plt
from collections import Counter

frecuencias = Counter(tokens_limpios)
palabras, valores = zip(*frecuencias.most_common(10))

plt.bar(palabras, valores)
plt.title("Top 10 palabras más comunes")
plt.xticks(rotation=45)
plt.show()
```

### Ejercicio:
Crear una **nube de palabras** con la biblioteca `wordcloud`.

---

## 7. Análisis de concordancia
Buscar patrones de palabras en contexto.

### Ejemplo:
```python
from nltk.text import Text

text = Text(word_tokenize(texto))
text.concordance("love")  # Encuentra frases que contienen "love"
```

### Ejercicio:
Buscar varias palabras relacionadas y comparar sus contextos.

---

## 8. Extensiones futuras
- **Trabajar con datos reales:** Descarga un texto desde la web usando `requests` o `BeautifulSoup`.
- **Introducir conceptos básicos de stemming y lematización:**
   ```python
   from nltk.stem import PorterStemmer
   stemmer = PorterStemmer()
   print(stemmer.stem("running"))  # Resultado: run
   ```

### Ejercicio:
Probar diferentes algoritmos de stemming y comparar resultados.
