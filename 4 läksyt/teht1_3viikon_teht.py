from sympy import symbols, Eq, solve


x, y = symbols('x y')


eq1 = Eq(5*x + 3*y, 9)
eq2 = Eq(2*x + y, 4)

ratkaisu = solve((eq1, eq2), (x, y))

print("Ratkaisu:")
print("x =", ratkaisu[x])
print("y =", ratkaisu[y])




x, y, z = symbols('x y z')


eq1 = Eq(2*x + y + z, 6)
eq2 = Eq(x + 3*y + z, 2)
eq3 = Eq(2*x + y + 2*z, 9)

ratkaisu = solve((eq1, eq2, eq3), (x, y, z))

print("Ratkaisu:")
print("x =", ratkaisu[x])
print("y =", ratkaisu[y])
print("z =", ratkaisu[z])





x, y, z = symbols('x y z')


eq1 = Eq(x + y + 3*z, -1)
eq2 = Eq(3*x + y + z, 5)
eq3 = Eq(2*x + y + 2*z, 2)


ratkaisu = solve((eq1, eq2, eq3), (x, y, z))

print("Ratkaisu:")
print("x =", ratkaisu[x])
print("y =", ratkaisu[y])
print("z =", ratkaisu[z])
