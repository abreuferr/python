# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRICAO  : jogo do NIM
# OBS : https://www.coursera.org/learn/ciencia-computacao-python-conceitos/programming/yEPxE/programa-completo-jogo-do-nim

# funcao usuario()
def usuario_escolhe_jogada(n,m):
    n = n - 1
    return n
#    if n <= m:
#        print("Fim do jogo, o USUARIO ganhou o jogo !!")
#        quit()
#    else:
#        a = int(input("Quantas peças você vai tirar? "))
#        if a > m:
#            while a > m:
#                print("Oops! Jogada inválida! Tente de novo.")
#                a = int(input("Quantas peças você vai tirar? "))      
#        else:
#            print("Você tirou", a , "peça(s).\n")
#            n = n-a
#            return computador_escolhe_jogada(n,m)

# funcao computador()
def computador_escolhe_jogada(n,m):
    n = n - 1
    return n
#    if n <= m:
#        print("Fim do jogo, o COMPUTADOR ganhou o jogo !!")
#        quit()
#    else:
#        contador = 1
#        while (contador <= m):
#            if (n-contador)%(m+1) == 0:
#                n = n-contador
#                print("O computador tirou", contador , "peça(s).\n")
#                return usuario_escolhe_jogada(n,m)
#            else:
#                contador += 1

def partida():
    # inicializando variavel
    j = 11 # 0=usuario e 1=computador
    # pecas
    n = int(input("Quantas pecas ? "))
    m = int(input("Limite de pecas por jogador? "))

    # quem comeca o jogo, usuario ou computador
    if (n%(m+1) == 0): # usuario
        print("\nVoce começa!\n")
        usuario_escolhe_jogada(n,m)
        print("u-Agora restam", n , "peças no tabuleiro.\n")
        j = 1 # computador
    elif (n%(m+1) != 0): # computador
        print("\nComputador começa !\n")
        computador_escolhe_jogada(n,m)
        print("c-Agora restam", n , "peças no tabuleiro.\n")
        j = 0 # usuario

    # restante das jogadas
    while n != 0:
        if (n%(m+1) == 0) or (j == 0) : # usuario
            usuario_escolhe_jogada(n,m)
            print("u-Agora restam", n , "peças no tabuleiro.\n")
            j = 1 # computador
        elif (n%(m+1) != 0) or (j == 1): # computador
            computador_escolhe_jogada(n,m)
            print("c-Agora restam", n , "peças no tabuleiro.\n")
            j = 0 # usuario

##################################################################################
# main()
escolha = int(input("Bem-vindo ao jogo do NIM! - Escolha !\n"
                    "1 - para jogar uma partida isolada\n"
                    "2 - para jogar um campeonato "))

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
    print(" ")
    print("Voce escolheu uma partida isolada!\n")
    partida()
else:
    print(" ")
    print("Voce escolheu um campeonato!\n")
    partida()
    partida()
    partida()