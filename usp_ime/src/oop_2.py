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
# dados - ferrari, 1980 e vermelho
carro_do_meu_avo = Carro("Ferrari", 1980, "vermelho")

# exibir o conteudo "instancai.atributo" 
# (carro_do_meu_avo.cor)
print(carro_do_meu_avo.cor)