# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : funcao que retorna as letras maiusculas de uma string

def maiusculas(frase):
    # inicializacao variavel
    contador_string = 0
    valor_ascii = 0
    caracteres_maiusculos = ""

    # while para percorer todos os caracteres da string
    while contador_string < len(frase):

        # le cada caractere da string e armazenar na
        # variavel caractere
        caractere = frase[contador_string]

        # obter o valor ASCII do caractere
        valor_ascii = ord(caractere)

        # verifica se o caractere é maiusculo ou nao
        if valor_ascii >= 65 and valor_ascii <= 90:

            # se sim, salva o caractere em uma variavel
            caracteres_maiusculos = caracteres_maiusculos + caractere
        
        # incremento
        contador_string += 1
    
    # retorna todos os cacteres maiusculos
    return caracteres_maiusculos

# main()
# atribui valor a variavel
frase = "PrOgRaMaMoS em python!"

# chama a funcao maiusculas
total_maiusculas = maiusculas(frase)

# exibe o resultado com 
print(total_maiusculas)