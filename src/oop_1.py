# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : estudo sobre OOP em Python - parte 1

class carro:
    pass

meu_carro = carro()
seu_carro = carro()

meu_carro.ano = 1968
meu_carro.modelo = "fusca"
meu_carro.cor = "azul"
print(meu_carro.ano)
print(meu_carro.cor)

seu_carro.ano = 1991
seu_carro.modelo = "brasilia"
seu_carro.cor = "amarelo"
print(seu_carro.modelo)

novo_fusca = meu_carro
novo_fusca.ano += 10
print(novo_fusca.ano)
print(meu_carro.ano)