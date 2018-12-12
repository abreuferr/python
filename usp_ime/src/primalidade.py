# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : exibir os numeros impares entre 1 e um determinado valor
# OBS: 5 = 1 3 5 7 9

# variavel auxiliar
contador = 2
primo = True

# inserir o valor de n
numero = int(input("Digite um número inteiro:"))

while (contador != numero):
    resto = numero % contador 
    if resto == 0: 
        primo = False
        break
        
    contador += 1

if primo == False:
    print("não primo")
else:
    print("primo")