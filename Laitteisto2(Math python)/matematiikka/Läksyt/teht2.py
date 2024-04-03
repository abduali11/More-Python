import numpy as np
def f(x):
    return np.sin(x)
def derivaatta_3_pistetta(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)
x = 0.0
h = 0.001
derivaatta = derivaatta_3_pistetta(f, x, h)

# Tulosta tulos
print("Funktion derivaatta kohdassa x =", x, "on noin:", derivaatta)
