import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 10, 100)
y = -0.0063*x**2 + 0.55*x

# Piirretään kuvaaja
plt.plot(x, y, label=r'$y = -0.0063x^2 + 0.55x$')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Funktion kuvaaja')
plt.legend()
plt.grid(True)
plt.show()
