import math

a = int(input("qual valor de a? "))
b = int(input("qual valor de b? "))
c = int(input("qual valor de c? "))

delta = (b**2) - (4*a*c)

if delta < 0:
	print("NÃO EXISTE RAIZES REAIS")
else:
	if delta == 0:
		print("Duas raizes iguais x' e x'' =", (-b)/ 2*a )
	else:
		deltaRaiz = math.sqrt(delta)
		x1 = (-b + deltaRaiz) / 2*a
		x2 = (-b - deltaRaiz) / 2*a
		print("x' =",x1, "x'' =", x2)

