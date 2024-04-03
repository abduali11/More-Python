import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)

y1 = 2 * x
y2 = 2 * x + 3
y3 = -0.5 * x - 4

plt.plot(x, y1, label='y = 2x')
plt.plot(x, y2, label='y = 2x + 3')
plt.plot(x, y3, label='y = -1/2x - 4')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Suorat y = 2x, y = 2x + 3 ja y = -1/2x - 4')
plt.grid(True)
plt.legend()
plt.show()
