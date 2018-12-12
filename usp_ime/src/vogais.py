# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : indicar se o caractere digitado eh vogal ou consoante

# funcao vogal
def vogal(caractere):
    if caractere == "a" or caractere == "e" or caractere == "i" or caractere == "o" or caractere == "u":
        return True
    elif caractere == "A" or caractere == "E" or caractere == "I" or caractere == "O" or caractere == "U":
        return True
    else:
        return False

caractere = input("Digite uma letra: ")
vogal(caractere)