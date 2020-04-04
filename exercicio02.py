import math

#obtendo valores
print('Equaçao do 2ºgrau: ax² + bx + c')
a=int(input('coeficiente a:') )
b = int( input('Coeficiente b: ') )
c = int( input('Coeficiente c: ') )

#delta
delta = b*b - (4*a*c)

#raizer
if delta < 0:
    print("A equação não possui raizes reais.")
elif delta == 0:
    raiz = (-b + math.sqrt(delta))/(2 * a)
    print("A equacao possui apenas uma raiz que e ",raiz)
elif delta > 0:
    raiz1 =(-b + math.sqrt(delta))/(2 * a)
    raiz2 =(-b - math.sqrt(delta))/(2 * a)
    print("As raizes da equacao sao:", "\n",raiz1, "e" ,raiz2)
