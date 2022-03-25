def n_primos(x):
    quantidade = 1
    fator = 2
    if x == 2:
        return quantidade
    
    primo = 3
    while primo <= x:
        while primo % fator != 0 and fator <= primo/2:
            fator = fator + 1
    
        if primo % fator == 0:
            primo = primo + 1
            fator = 2
        else:
            quantidade = quantidade + 1
            fator = 2
            primo = primo + 1
    
    return quantidade