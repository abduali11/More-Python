import numpy as np
#kolmas tehtävä
u = np.array([2, 3])
v = np.array([4, -7])
uu = np.array([1, 1, 1])
vv = np.array([3, -3, 2])

norm_u = np.linalg.norm(u)
norm_v = np.linalg.norm(v)
norm_uu = np.linalg.norm(uu)
norm_vv = np.linalg.norm(vv)

print("Vektorin u normi:", norm_u)
print("Vektorin v normi:", norm_v)
print("Vektorin uu normi:", norm_uu)
print("Vektorin vv normi:", norm_vv)
