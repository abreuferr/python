# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : calcula e exibir a tabuada de 0 a 10

# declaracao variavel
#
linha = 1
coluna = 1

while linha <= 10:
    while coluna <= 10:
        # exibe o resultado
        # \t equivale a tecla tab
        #
        print( linha * coluna, end = "\t")
        coluna += 1
    linha += 1
    
    # quebrar a linha
    #
    print()
    
    coluna = 1