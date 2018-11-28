# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : estudo sobre OOP em Python - parte 3 - metodo __init__

# classe utilizada para testar o programa.
def main():
    # carro1 e carro2 sao instancias que assumem o conteudo do
    # objeto carro e cujos parametros estao dentro do ()
    carro1 = Carro('brasilia', 1968, 'amarela', 80) # objeto(parametros)
    carro2 = Carro('fuscao', 1981, 'preto', 95) # objeto(parametros)

    carro1.acelere(40)
    carro2.acelere(50)
    carro1.acelere(80)
    carro1.pare()
    carro2.acelere(100)

# definicao da classe Carro
class Carro:
    # metodo __init__()
    def __init__(self, modelo, ano, cor, vel_max):
        self.modelo  = modelo
        self.ano     = ano
        self.cor     = cor
        self.vel     = 0
        self.vel_max = vel_max  # velocidade maxima

    # metodo imprima()
    def imprima(self):
        if self.vel_atual == 0: # velocidade atual eh IGUAL a zero
            print( "%s %s %d"%(self.modelo, self.cor, self.ano)     )
        elif self.vel_atual < self.vel_max: # velocidade atual eh MENOR que a maxima
            print( "%s %s indo a %d Km/h"%(self.modelo, self.cor, self.vel) )
        else: # velocidade atual eh MAIOR que a maxima
            print( "%s %s indo muito rapido!"%(self.modelo, self.cor))

    # metodo acelere()
    def acelere(self, v):
        self.vel_atual = v
        if self.vel_atual > self.vel_max:
            self.vel_atual = self.vel_max
        self.imprima()
    
    # metodo pare()
    def pare(self):
        self.vel = 0
        self.imprima()

# main()
main()