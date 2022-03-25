def menu_inicial():
    print ("Bem vindo ao jogo do NIM! Escolha: ")
    escolha = int(input("1 - para jogar uma partida isolada\n2 - para jogar um campeonato\n\n-->"))
    while escolha < 1 or escolha > 2:
        int(input("\nEscolha inválida, tente novamente: "))
    if escolha == 1:
        print("\nVocê escolheu uma partida isolada!")
        partida()
    else:
        campeonato()

def usuario_escolhe_jogada(n_escolhido, m_escolhido):
    n_escolhido = int(input("\nQuantas peças você vai tirar? "))
    while n_escolhido > m_escolhido:
        n_escolhido = int(input("\nOops! Jogada inválida! Tente de novo.\n\nQuantas peças você vai tirar? "))
    
    if n_escolhido == 1:
        print("Você tirou uma peça.")
    else:
        print("Você tirou {} peças.".format(n_escolhido))
        
    return n_escolhido
    
def computador_escolhe_jogada(n, m):
    escolha = n - (m+1)
    if escolha < 1:
        escolha = n
    elif escolha > m:
        escolha = m
    
    if escolha == 1:
        print("\nO computador tirou uma peça.")
    else:
        print("\nO computador tirou {} peças.".format(escolha))
    return escolha
    
    
def partida():
    voce = 0
    computador = 0
    n_inicial = int(input("\nQuantas peças? "))
    m_inicial = int(input("Limite de peças por jogada? "))
    if (m_inicial + 1)%n_inicial == 0:
        print("\nVocê começa!")
        usuario = 1
    else:
        print("\nComputador começa!")
        usuario = 0
        
    while n_inicial != 0:
        if usuario == 1:
            n_inicial -= usuario_escolhe_jogada(n_inicial, m_inicial)
            if n_inicial == 1:
                print("Agora resta apenas uma peça no tabuleiro.")
            else:
                print("Agora restam {} peças no tabuleiro.".format(n_inicial))
            usuario = 0
        else:
            n_inicial -= computador_escolhe_jogada(n_inicial, m_inicial)
            if n_inicial == 1:
                print("Agora resta apenas uma peça no tabuleiro.")
            else:
                print("Agora restam {} peças no tabuleiro.".format(n_inicial))
            usuario = 1
        
    if usuario == 1:
        print("Fim do jogo! O computador ganhou!\n")
        return 1
    else:
        print("Fim do jogo! Você ganhou!\n")
        return 0



def campeonato():
    voce = 0
    computador = 0
    
    print("\nVocê escolheu um campeonato!\n")
    i = 1
    while i < 4:
        print("======== partida {} ========".format(i))
        i += 1
        if partida() == 1:
            computador += 1
        else:
            voce += 1
    print("======= Final do campeonato =======")
    print("Placar: Você {} X {} Computador".format(voce, computador))
    
    
menu_inicial()