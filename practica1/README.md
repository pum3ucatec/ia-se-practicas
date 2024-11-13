# Clustering Basado en Distancia Euclidiana

Este proyecto tiene como objetivo resolver un problema de **clustering** en un plano 2D utilizando la **distancia euclidiana** como métrica de proximidad. En este caso, se cuenta con cinco puntos en un espacio bidimensional, y se debe implementar un programa en Python que calcule las distancias entre cada par de puntos y determine los clusters formados en función de un umbral de distancia.

## Fórmula de Distancia Euclidiana

La **distancia euclidiana** es una medida de proximidad entre dos puntos en un espacio. Dada una pareja de puntos \( A \) y \( B \) con coordenadas \( (x_1, y_1) \) y \( (x_2, y_2) \), respectivamente, la distancia entre ellos se calcula con la siguiente fórmula:

\[
\text{Distancia} = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
\]

Esta fórmula se utiliza para calcular la distancia entre cada par de puntos en el conjunto y decidir qué puntos están lo suficientemente cerca para formar un cluster.

## Problema

Dado el siguiente conjunto de puntos en un plano 2D:

- **A**: (2, 3)
- **B**: (5, 1)
- **C**: (8, 3)
- **D**: (1, 7)
- **E**: (6, 5)

Se requiere implementar un programa en Python que:
1. **Calcule la matriz de distancias** entre cada par de puntos usando la fórmula de distancia euclidiana.
2. **Visualice la matriz de distancias** en un formato legible en la consola.
3. **Forme clusters** de puntos usando un umbral de distancia, por ejemplo, 4.5. Los puntos que están a una distancia menor o igual al umbral respecto a otros puntos deben agruparse en el mismo cluster.
4. **Muestre los clusters formados** y visualice la distribución de puntos en un gráfico.

## Instrucciones de Implementación

1. **Calcular la Matriz de Distancias**:
   - Usa la biblioteca **SciPy** para calcular la distancia euclidiana entre los puntos y crear una **matriz de distancias**.
   
2. **Establecer un Umbral de Distancia**:
   - Define un valor de umbral de 4.5 para decidir qué puntos deben agruparse. Si la distancia entre dos puntos es menor o igual a este valor, considera que pertenecen al mismo cluster.

3. **Algoritmo de Clustering**:
   - Implementa un algoritmo que recorra la matriz de distancias y agrupe los puntos en clusters en función del umbral.
   - Utiliza un enfoque donde los puntos pueden pertenecer al mismo cluster si están dentro del umbral respecto a algún miembro del cluster.

4. **Visualización**:
   - Utiliza **Matplotlib** para graficar los puntos en el plano 2D y mostrar los clusters visualmente.
   - Asegúrate de etiquetar los puntos en el gráfico y de hacer que la visualización sea clara.

5.  **Setup**:
-
6.   