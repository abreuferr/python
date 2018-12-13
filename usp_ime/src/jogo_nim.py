# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRICAO  : jogo do NIM
# OBS : https://www.coursera.org/learn/ciencia-computacao-python-conceitos/programming/yEPxE/programa-completo-jogo-do-nim

def computador_escolhe_jogada(n,m):
    print("Computador começa!")
    return

def usuario_escolhe_jogada(n,m):
    x = int(input("Quantas peças você vai tirar? "))
    if x > m:
        while x > m:
            print("Oops! Jogada inválida! Tente de novo.")
            x = int(input("Quantas peças você vai tirar? "))
        
    else:
        print("Continua o jogo")

def partida():
    # pecas
    n = int(input("Quantas pecas? "))
    m = int(input("Limite de pecas por jogador? "))

    # computador ou usuario comecam o jogo
    if (n%(m+1) == 0):
        usuario_escolhe_jogada(n,m)
    else:
        computador_escolhe_jogada(n,m)

#
# main()
#

# tipo de partida
escolha = int(input("Bem-vindo ao jogo do NIM! - Escolha !\n"
                    "1 - para jogar uma partida isolada\n"
                    "2 - para jogar um campeonato "))
if escolha == 1:
    partida()
else:
    print("Campeonato")
    #campeonato()