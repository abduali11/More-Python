from sympy import symbols, Eq, solve


x, y, z = symbols('x y z')

eq1 = Eq(x - 2*y - 2*z, 0)
eq2 = Eq(-2*x + y - z, -3)
eq3 = Eq(3*x + 2*y + z, 4)


ratkaisu = solve((eq1, eq2, eq3), (x, y, z))

print("Ratkaisu:")
print("x =", ratkaisu[x])
print("y =", ratkaisu[y])
print("z =", ratkaisu[z])



x, y, z = symbols('x y z')


eq1 = Eq(x + y, 1)
eq2 = Eq(2*x + y - z, 1)
eq3 = Eq(3*x + y - 2*z, 1)


ratkaisu = solve((eq1, eq2, eq3), (x, y, z))

print("Ratkaisu:")
print("x =", ratkaisu[x])
print("y =", ratkaisu[y])
print("z =", ratkaisu[z])
