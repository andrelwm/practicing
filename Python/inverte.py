lista = []
while True:
    x = int(input("Digite um número: "))
    if x == 0:
        break
    lista.append(x)

lista_nova = []
for i in range(len(lista)):
    lista_nova.append(lista[-(i+1)])
    
print()
for i in lista_nova:
    print (i)
    