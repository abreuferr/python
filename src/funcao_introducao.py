# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : estudo sobre funcao

# funcao soma
#
def soma(valorX, valorY=100):
    valorSoma = valorX + valorY
    return valorSoma

print(soma(10, 20))
print(soma(10))

print(__name__) # exibe o nome da funcao