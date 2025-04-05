# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : estudo sobre OOP em Python - parte 2 - metodo __init__

# classe Carro
class Carro:
    # método __init__(atributos)
    # metodo especial.
    # conhecido como Construtor da classe.
    # chamado automaticamente pelo interpretador quando os
    # objetos sao criados, como por exemplo, quando as classes
    # sao instanciadas.
    def __init__(self, modelo, ano, cor):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

# objeto - carro
# atributos - modelo, ano, cor 
# dados - 'Brasilia', 1968, 'amarela'
carro_do_meu_avo = Carro('Brasilia', 1968, 'amarela')
carro_do_meu_primo = Carro('Fusca', 1981, 'preto')

# exibir o conteudo "instancia.atributo" 
# nome_do_objeto.nome_do_atributo
print(carro_do_meu_avo.cor)
print(carro_do_meu_primo.ano)