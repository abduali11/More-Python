#Suorakulmaisen kolmion kateetit ovat pituudeltaan 2,3 ja 4,7.
# Määritä hypotenuusan pituus sekä kolmion kaksi muuta kulmaa asteina.
import math
a = 2.3
b = 4.7
c = math.sqrt(a**2 + b**2)

#määritetään kulmat asteina

kulma1_rad = math.atan(a/b)
kulma2_rad = math.atan(b/a)
kulma1_ast = math.degrees(kulma1_rad)
kulma2_ast = math.degrees(kulma2_rad)
print(c)
print(kulma1_ast)
print(kulma2_ast)

