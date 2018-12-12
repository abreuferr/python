# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRICAO  : calcular a distancia entre dois pontos

# import
import math

# inserir os dados
xa = int(input("Insira o valor de xa "))
ya = int(input("Insira o valor de ya "))
xb = int(input("Insira o valor de xb "))
yb = int(input("Insira o valor de yb "))

# calculo da distancia
xba = (xb-xa)
yba = (yb-ya)
distancia = math.sqrt(math.pow(xba,2) + math.pow(yba,2))

if distancia >= 10:
    print("longe")
else:
    print("perto")