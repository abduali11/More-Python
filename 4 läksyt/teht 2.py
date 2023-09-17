from sympy import symbols, Eq, solve


x, y, z = symbols('x y z')


eq1 = Eq(2*x + 4*y - z, 11)
eq2 = Eq(6*x - y - 3*z, 7)
eq3 = Eq(4*x + 5*y - 2*z, 16)


ratkaisu = solve((eq1, eq2, eq3), (x, y, z))

print("Ratkaisu:")
print("x =", ratkaisu[x])
print("y =", ratkaisu[y])
print("z =", ratkaisu[z])






x, y, z = symbols('x y z')

eq1 = Eq(4*x + 2*y - 2*z, 0)
eq2 = Eq(2*x + y - z, 1)
eq3 = Eq(3*x + y - 2*z, 1)


ratkaisu = solve((eq1, eq2, eq3), (x, y, z))

print("Ratkaisu:")
print("x =", ratkaisu[x])
print("y =", ratkaisu[y])
print("z =", ratkaisu[z])
