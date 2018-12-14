# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRICAO  : jogo do NIM
# OBS : https://www.coursera.org/learn/ciencia-computacao-python-conceitos/programming/yEPxE/programa-completo-jogo-do-nim

# funcao usuario()
def usuario_escolhe_jogada(n,m):
    if n <= m:
        print("Fim do jogo, o USUARIO ganhou o jogo !!")
        quit()
    else:
        a = int(input("Quantas peças você vai tirar? "))
        if a > m:
            while a > m:
                print("Oops! Jogada inválida! Tente de novo.")
                a = int(input("Quantas peças você vai tirar? "))      
        else:
            print("Você tirou", a , "peça(s).\n")
            n = n-a
            return computador_escolhe_jogada(n,m)

# funcao computador()
def computador_escolhe_jogada(n,m):
    if n <= m:
        print("Fim do jogo, o COMPUTADOR ganhou o jogo !!")
        quit()
    else:
        contador = 1
        while (contador <= m):
            if (n-contador)%(m+1) == 0:
                n = n-contador
                print("O computador tirou", contador , "peça(s).\n")
                return usuario_escolhe_jogada(n,m)
            else:
                contador += 1

def partida():
    # pecas
    n = int(input("Quantas pecas ? "))
    m = int(input("Limite de pecas por jogador? "))

    if (n%(m+1) == 0): # usuario
        print(" ")
        print("Voce começa!\n")
        usuario_escolhe_jogada(n,m)
        print("u-Agora restam", n , "peças no tabuleiro.\n")
    else: # computador
        print("Computador começa !\n")
        computador_escolhe_jogada(n,m)
        print("c-Agora restam", n , "peças no tabuleiro.\n")

#
# main()
#
# tipo de partida
escolha = int(input("Bem-vindo ao jogo do NIM! - Escolha !\n"
                    "1 - para jogar uma partida isolada\n"
                    "2 - para jogar um campeonato "))
if escolha == 1:
    print(" ")
    print("Voce escolheu uma partida isolada!\n")
else:
    print(" ")
    print("Voce escolheu um campeonato!\n")
    partida()