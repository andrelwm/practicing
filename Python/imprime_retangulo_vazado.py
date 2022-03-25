largura = int(input("Digite a largura (número inteiro): "))
altura = int(input("Digite a altura (número inteiro): "))

altura_escolhida = altura
while altura > 0:
    if altura == altura_escolhida or altura == 1:
        print(largura*"#")
        altura -= 1
    else:
        print("#", (largura-4)*" ", "#")
        altura -= 1