# importando a classe math
import math

# definicao da classe Ponto
class Ponto:
    """ 
    classe Ponto utilizado para representar
    e manipular as coordenadas x,y
    """
    
    # metodo __init__
    def __init__(self, initX, initY):
        self.x = initX # atributo x
        self.y = initY # attibuto y
    
    # metodo getX
    def getX(self):
        return self.x

    # metodo getY
    def getY(self):
        return self.y
    
    # metodo distancia_origem
    # calcular a distancia entre a origem e um ponto
    def distancia_origem(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
    
    # metodo __str__
    # nos outros metodos, o retorno sempre foi um 
    # valor numerico. Nesse metodo, o retorno eh 
    # uma string
    def __str__(self):
        return "x = " + str(self.x) + ", y = " + str(self.y)
    
    def meio(self, alvo):
         mx = (self.x + alvo.x)/2
         my = (self.y + alvo.y)/2
         return Ponto(mx, my)
    
# funcao distancia (funcao + oop)
# calcular a distancia entre dois pontos
def distancia(ponto1, ponto2):
    xdif = ponto2.getX()-ponto1.getX()
    ydif = ponto2.getY()-ponto1.getY()
    dist = math.sqrt(xdif**2 + ydif**2)
    return dist