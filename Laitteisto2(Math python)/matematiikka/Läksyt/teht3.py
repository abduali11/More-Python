import numpy as np

def f(x):
    return np.exp(-x**2)
def derivaatta_3_pistetta(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)
x = 1.5
dx = 0.001
derivaatta = derivaatta_3_pistetta(f, x, dx)

print("Funktion derivaatta kohdassa x =", x, "on noin:", derivaatta)
