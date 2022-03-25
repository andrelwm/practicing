import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("\nEntre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("\nDigite o texto {} (aperte enter para sair):".format(i))
    while texto:
        textos.append(texto)
        i += 1
        texto = input("\nDigite o texto {} (aperte enter para sair):".format(i))

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''Essa funcao recebe duas assinaturas de texto e devolve o grau de similaridade nas assinaturas.'''
    soma = 0
    for assinatura in range(6):
        soma = soma + abs(as_a[assinatura] - as_b[assinatura])
    
    similaridade = soma/6
    
    return similaridade
    
def calcula_assinatura(texto):
    '''Essa funcao recebe um texto e devolve a assinatura do texto.'''
    sentencas = separa_sentencas(texto)
    frases = []
    palavras = []
    caracteres_texto = 0
    caracteres_sentencas = 0
    caracteres_frases = 0

    for sentenca in sentencas:
        frases = frases + separa_frases(sentenca)
        caracteres_sentencas = caracteres_sentencas + len(sentenca)

    for frase in frases:
        palavras = palavras + separa_palavras(frase)
        caracteres_frases = caracteres_frases + len(frase)

    for palavra in palavras:
        caracteres_texto = caracteres_texto + len(palavra)

    palavras_dif = n_palavras_diferentes(palavras)
    palavras_uni = n_palavras_unicas(palavras)


    wal = caracteres_texto/len(palavras)
    ttr = palavras_dif/len(palavras)
    hlr = palavras_uni/len(palavras)
    sal = caracteres_sentencas/len(sentencas)
    sac = len(frases)/len(sentencas)
    pal = caracteres_frases/len(frases)
    
    return [wal, ttr, hlr, sal, sac, pal]

def avalia_textos(textos, ass_cp):
    '''Essa funcao recebe uma lista de textos e uma assinatura ass_cp e devolve o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    comparacoes = []
    for texto in textos:
        assinatura = calcula_assinatura(texto)
        similaridade = compara_assinatura(ass_cp, assinatura)
        comparacoes.append(similaridade)
    infectado = comparacoes.index(min(comparacoes)) + 1
    
    return infectado
    
