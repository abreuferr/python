# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : estudo sobre OOP em Python - parte 3 - metodo __init__

def main():
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
    def __init__(self, m, a, c, vm):
        self.modelo = m
        self.ano    = a
        self.cor    = c
        self.vel    = 0
        self.maxV   = vm  # velocidade maxima

    # metodo imprima()
    def imprima(self):
        if self.vel == 0: # parado da para ver o ano
            print( "%s %s %d"%(self.modelo, self.cor, self.ano)     )
        elif self.vel < self.maxV:
            print( "%s %s indo a %d Km/h"%(self.modelo, self.cor, self.vel) )
        else:
            print( "%s %s indo muito rapido!"%(self.modelo, self.cor))

    # metodo acelere()
    def acelere(self, v):
        self.vel = v
        if self.vel > self.maxV:
            self.vel = self.maxV
        self.imprima()
    
    # metodo pare()
    def pare(self):
        self.vel = 0
        self.imprima()

# main()
main()