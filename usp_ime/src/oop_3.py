# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRICAO  : estudo sobre OOP em Python - parte 3 - metodo __init__

# metodo main()
def main():
    # nome_da_instancia = nome_do_objeto(valor_atributo1, valor_atributo2)
    carro1 = Carro('brasilia', 1968, 'amarela', 80)
    carro2 = Carro('fuscao', 1981, 'preto', 95)

    # chamada de um metodo.
    # nome_da_instancia.nome_do_metodo(valor_atribuido)
    carro1.acelere(40)
    carro2.acelere(50)
    carro1.acelere(80)
    carro1.pare()
    carro2.acelere(100)

# definicao da classe Carro
class Carro:
    # metodo __init__()
    def __init__(self, modelo, ano, cor, vm):
        self.modelo = modelo
        self.ano    = ano
        self.cor    = cor
        self.vel    = 0
        self.vel_max   = vm  # velocidade maxima

    # metodo imprima()
    def imprima(self):
        if self.vel == 0: # parado da para ver o ano
            print( "%s %s %d"%(self.modelo, self.cor, self.ano)     )
        elif self.vel < self.vel_max:
            print( "%s %s indo a %d Km/h"%(self.modelo, self.cor, self.vel) )
        else:
            print( "%s %s indo muito rapido !"%(self.modelo, self.cor))

    # metodo acelere()
    def acelere(self, vel_atual):
        self.vel = vel_atual
        if self.vel > self.vel_max:
            self.vel = self.vel_max
        self.imprima()

    # metodo pare()
    def pare(self):
        self.vel = 0
        self.imprima()

# main()
main()