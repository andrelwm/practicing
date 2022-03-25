def é_hipotenusa(x):
    i = 1
    j = 1
    while i < x:
        while j < x:
            if x**2 == (i**2 + j**2):
                return True
            else:
                j = j + 1
        i = i + 1
        j = 1
    
    return False
    
def soma_hipotenusas(n):
    soma = 0
    i = 1
    while i <= n:
        if é_hipotenusa(i):
            soma = soma + i
            i = i + 1
        else:
            i = i + 1
    return soma
    
