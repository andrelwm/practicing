def maior_primo(x):
    while True:
        cont = 0
        i = 1
        while i <= x:
            if x%i == 0:
                cont = cont + 1
                i = i + 1
            else:
                i = i + 1
        if cont <= 2:
            break
        else:
            x = x - 1
    return x
