import math

x1 = int(input("Digite a coordenada x do primeiro ponto: "))
y1 = int(input("Digite a coordenada y do primeiro ponto: "))
x2 = int(input("Digite a coordenada x do segundo ponto: "))
y2 = int(input("Digite a coordenada y do segundo ponto: "))

distancia = math.sqrt((x1-x2)**2 + (y1-y2)++2)

if distancia >= 10:
    print("longe")
else:
    print("perto")