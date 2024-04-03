from sympy import symbols, diff

x = symbols('x')

funktio = 2*x**2 - 3
derivaatta = diff(funktio, x)

print("Funktion derivaatta:", derivaatta)
