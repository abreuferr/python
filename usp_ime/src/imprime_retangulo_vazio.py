# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : desenhar um quadrado ou retangulo com o interior vazado.

# aquisicao dos dados
largura = int(input("digite o valor da largura: "))
altura = int(input("Digite o valor da altura: "))

# inicializando variavel
contador_a = 1 # contador da altura

# desenhar as linhas
while (contador_a <= altura):
    print("#", end = "") # gerar o topo e a borda
    # inicializando variavel
    contador_l = 2
    while (contador_l < largura): 
        if (contador_a == 1) or (contador_a == altura) or (contador_l == largura):
            print("#",end="") # gerar o topo e a borda
        else:
            print(end = " ") # gerar os espacos em branco dentro do quadrado
        # incrimentar o contador da largura
        contador_l += 1
    # desenhar o topo e a borda
    # desenhar as bordas laterais
    print("#")
    # incrementar o contador da altura
    contador_a += 1