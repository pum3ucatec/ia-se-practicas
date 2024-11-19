import math

def cosine_similarity(x, y):
    """Calcula la similitud coseno entre dos vectores."""
    dot_product = sum(xi * yi for xi, yi in zip(x, y))
    magnitude_x = math.sqrt(sum(xi**2 for xi in x))
    magnitude_y = math.sqrt(sum(yi**2 for yi in y))
    if magnitude_x == 0 or magnitude_y == 0:
        return 0  # Evitar división por cero
    return dot_product / (magnitude_x * magnitude_y)


