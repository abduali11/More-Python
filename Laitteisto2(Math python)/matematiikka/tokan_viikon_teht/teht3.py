#tehtävä 3
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 5, 100)

y = x**2 - 4*x + 3

plt.plot(x, y, label=r'$y = x^2 - 4x + 3$')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Funktion kuvaaja')
plt.legend()
plt.grid(True)
plt.show()
