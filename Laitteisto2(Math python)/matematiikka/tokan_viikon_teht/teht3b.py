import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)
y = -1.5*x**2 - 3*x + 7


plt.plot(x, y, label=r'$y = -1.5x^2 - 3x + 7$')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Funktion kuvaaja')
plt.legend()
plt.grid(True)
plt.show()
