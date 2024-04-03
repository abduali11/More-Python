import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, solve, diff, sin

def f(x):
    return x**2

dx = 10**(-3)
x = 2
derivaatta = (f(x + dx) - f(x))/dx
virhe = np.abs(derivaatta - 4)
print('Derivaatta:', derivaatta, '     Virhe:', virhe)