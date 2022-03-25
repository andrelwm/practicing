import math

a = int(input("Digite o coeficiente de grau 2 do polinômio: "))
b = int(input("Digite o coeficiente de grau 1 do polinômio: "))
c = int(input("Digite o coeficiente de grau 0 do polinômio: "))

delta = (b**2 - (4*a*c))

if delta < 0:
    print("esta equação não possui raízes reais")
elif delta == 0:
    raiz = (-b + math.sqrt(delta))/(2*a)
    print("a raiz desta equação é {}".format(raiz))
else:
    raiz1 = (-b + math.sqrt(delta))/(2*a)
    raiz2 = (-b - math.sqrt(delta))/(2*a)
    if raiz1 < raiz2:
        print("as raízes da equação são {} e {}".format(raiz1, raiz2))
    else:
        print("as raízes da equação são {} e {}".format(raiz2, raiz1))

