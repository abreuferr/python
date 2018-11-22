# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : estudo sobre OOP em Python - parte 1

class carro:
    pass

# duas instancias, meu_carro e seu_carro, do 
# objeto carro()
meu_carro = carro()
seu_carro = carro()

# tres atributos, ano/modelo/cor, e foi adicionado 
# dados a esses tres atributos, 1968/fusca/azul
meu_carro.ano = 1968
meu_carro.modelo = "fusca"
meu_carro.cor = "azul"
print(meu_carro.ano) # 
print(meu_carro.cor)

# tres atributos, ano/modelo/cor, e foi adicionado 
# dados a esses tres atributos, 1991/brasilia/amarelo
seu_carro.ano = 1991
seu_carro.modelo = "brasilia"
seu_carro.cor = "amarelo"
print(seu_carro.modelo)

novo_fusca = meu_carro
novo_fusca.ano += 10
print(novo_fusca.ano)
print(meu_carro.ano)