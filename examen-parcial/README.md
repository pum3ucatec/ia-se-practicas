### **Enunciado del Patrón: Distancia Coseno (Cosine Similarity)**

La **distancia coseno** es una medida matemática utilizada para calcular la similitud entre dos vectores en un espacio n-dimensional, basándose en el ángulo entre ellos en lugar de la magnitud. Es particularmente útil en casos donde el interés radica en la orientación de los vectores y no en su escala.

#### **Fórmula:**
La similitud coseno se calcula como:

$$
\text{similarity} = \cos(\theta) = \frac{\sum_{i=1}^{n} x_i \cdot y_i}{\sqrt{\sum_{i=1}^{n} x_i^2} \cdot \sqrt{\sum_{i=1}^{n} y_i^2}}
$$

Donde:  
- \( x_i \) y \( y_i \) son los componentes de los vectores \( X \) y \( Y \).  
- \( \cos(\theta) \) varía entre -1 (vectores opuestos) y 1 (vectores idénticos). Una similitud de 0 indica vectores ortogonales.

#### **Características:**
- Se centra en la dirección de los vectores y no en su magnitud.
- Es ideal para datos de alta dimensionalidad donde la normalización de escala es relevante.

#### **Aplicaciones en la Vida Real:**
1. **Sistemas de recomendación:**  
   Comparar perfiles de usuarios o productos para sugerir opciones similares basándose en intereses comunes.
   
2. **Procesamiento de texto y análisis semántico:**  
   Comparar documentos o frases mediante representaciones vectoriales como TF-IDF o Word2Vec, evaluando su similitud.

3. **Análisis de redes sociales:**  
   Identificar usuarios con comportamientos o preferencias similares.

4. **Visión por computadora:**  
   Comparar características de imágenes para tareas de reconocimiento de patrones o clasificación.

#### **Ejemplo Práctico:**
Si se tienen dos documentos representados por vectores TF-IDF:  
\( X = [0.2, 0.5, 0.1, 0.0] \) y \( Y = [0.3, 0.4, 0.0, 0.2] \),  
se calcula la similitud coseno entre ellos para determinar qué tan similares son en su contenido.

---

Este patrón es clave para analizar similitudes en datos complejos y tiene amplias aplicaciones en la Inteligencia Artificial y la ciencia de datos.

## Pregunta

Realizar el codigo en python para graficar el ejemplo practico
