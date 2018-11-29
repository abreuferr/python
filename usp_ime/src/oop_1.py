# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : estudo sobre OOP em Python - parte 1

# classe "carro" que nao faz nada
class carro:
    pass

# duas instancias/variaveis(meu_carro e seu_carro) 
# do objeto carro()
meu_carro = carro()
seu_carro = carro()

# tres atributos(ano/modelo/cor) e foi adicionado 
# dados a esses tres atributos(1968/fusca/azul) 
# instancia.atributo = dado 
meu_carro.ano = 1968
meu_carro.modelo = "fusca"
meu_carro.cor = "azul"
print(meu_carro.ano) # 
print(meu_carro.cor)

# tres atributos(ano/modelo/cor) e foi adicionado 
# dados a esses tres atributos(1991/brasilia/amarelo)
#  
# instancia.atributo = dado 
seu_carro.ano = 1981
seu_carro.modelo = "brasilia"
seu_carro.cor = "amarelo"
print(seu_carro.modelo)

# "novo_fusca" esta se referenciando a "meu_carro"
# duas variaveis(meu_carro e novo_fusca) apontando 
# para o mesmo objeto (carro)
novo_fusca = meu_carro

# somando o valor 10 ao atributo ANO da variavel
# novo_fusca
novo_fusca.ano += 10 
print(novo_fusca.ano) # 1968 para 1978
# como meu_carro e novo_fusca estao apontando para
# o mesmo objeto (carro), entao, meu_carro.ano e 
# novo_fusca serao acrescidos em 10 nos seus respectivos
# valores.
print(meu_carro.ano) # 1981 para 1991