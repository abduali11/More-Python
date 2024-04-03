
def g(x):
    return (x - 1) / (x + 1)

def derivaatta_3_pistetta(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)


x = 0.3
dx = 0.001


derivaatta = derivaatta_3_pistetta(g, x, dx)

# Tulosta tulos
print("Funktion derivaatta kohdassa x =", x, "on noin:", derivaatta)
