# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRICAO  : jogo do NIM
# OBS : https://www.coursera.org/learn/ciencia-computacao-python-conceitos/programming/yEPxE/programa-completo-jogo-do-nim

# funcao usuario()
def usuario_escolhe_jogada(n,m):
    valor = int(input("Quantas peças você vai tirar? "))
    if valor > m:
        while (valor > m) or (valor <= 0):
            print("\nOops! Jogada inválida! Tente de novo.\n")
            valor = int(input("Quantas peças você vai tirar? "))
        print("Você tirou", valor , "peça(s).\n")
        n = valor
        return n
    else:
        print("Você tirou", valor , "peça(s).\n")
        n = valor
        return n

# funcao computador()
def computador_escolhe_jogada(n,m):
    contador = 1
    while (contador <= m):
        if (n-contador)%(m+1) == 0:
            n = n - contador
            print("O computador tirou", contador , "peça(s).\n")
            n = contador
            return n
        else:
            contador += 1

def partida():
    # inicializando variavel
    j = 11 # 0=usuario e 1=computador
    n = 0
    m = 0
    # pecas
    n_inicial = int(input("Quantas pecas ? "))
    m = int(input("Limite de pecas por jogador? "))
    if n_inicial <= m:
        while (n_inicial => m) or (n_inicial <= 0):
            print("\nOops! Jogada inválida! Tente de novo.\n")
            n_inicial = int(input("Quantas pecas ? "))
            m = int(input("Limite de pecas por jogador? "))

        # quem comeca o jogo, usuario ou computador
        if (n%(m+1) == 0): # usuario
            print("\nVoce começa!\n")
            n = n_inicial
            n = usuario_escolhe_jogada(n,m)
            n = n_inicial - n
            print("u-Agora restam", n , "peças no tabuleiro.\n")
            n_inicial = n
            j = 1 # computador
        elif (n%(m+1) != 0): # computador
            print("\nComputador começa !\n")
            n = n_inicial
            n = computador_escolhe_jogada(n,m)
            n = n_inicial - n
            print("c-Agora restam", n , "peças no tabuleiro.\n")
            n_inicial = n
            j = 0 # usuario

    # restante das jogadas
    while n != 0:
        if (n%(m+1) == 0) or (j == 0) : # usuario
            n = usuario_escolhe_jogada(n,m)
            n = n_inicial - n
            print("u-Agora restam", n , "peças no tabuleiro.\n")
            n_inicial = n
            j = 1 # computador
        elif (n%(m+1) != 0) or (j == 1): # computador
            n = computador_escolhe_jogada(n,m)
            n = n_inicial - n
            print("c-Agora restam", n , "peças no tabuleiro.\n")
            n_inicial = n
            j = 0 # usuario
    if j == 0: # computador
        print("Fim do jogo ! O computador ganhou !")
    else: # usuario
        print("Fim do jogo ! O usuario ganhou !")

##################################################################################
# main()
escolha = int(input("Bem-vindo ao jogo do NIM! - Escolha !\n 1 - para jogar uma partida isolada\n 2 - para jogar um campeonato "))
if (escolha != 1) and (escolha != 2):
    while (escolha != 1) or (escolha != 2):
        print("\nOpcao errada, escolha as opcoes abaixo\n")
        escolha = int(input("1 - para jogar uma partida isolada\n"
                            "2 - para jogar um campeonato "))
        if escolha == 1:
            print(" ")
            print("Voce escolheu uma partida isolada!\n")
            partida()
        elif escolha == 2:
            print(" ")
            print("Voce escolheu um campeonato!\n")
            partida()
            partida()
            partida()
elif escolha == 1:
    print("\nVoce escolheu uma partida isolada!\n")
    partida()
else:
    print("\nVoce escolheu um campeonato!\n")
    print("Rodada 1\n")
    partida()
    print("\nRodada 2\n")
    partida()
    print("\nRodada 3\n")
    partida()