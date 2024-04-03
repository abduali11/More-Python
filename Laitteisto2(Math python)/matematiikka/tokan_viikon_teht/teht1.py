import numpy as np
import matplotlib.pyplot as plt

F = np.array([1, 2, 3, 5])
delta_s = np.array([9, 19, 27, 46])

k = delta_s[0] / F[0]

def jousi_funktio(F):
    return k * F
x = np.linspace(-1, 3, 100)

y = jousi_funktio(x)

plt.plot(x, y, label=r'$\Delta s = k \cdot F$')
plt.scatter(F, delta_s, color='red')
plt.xlabel('Voima (F)')
plt.ylabel('Venymä ($\Delta s$)')
plt.title('Jousen venymä ja voima')
plt.legend()
plt.grid(True)
plt.show()
