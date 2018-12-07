# definicao da classe Triangulo
class Triangulo:
  
    # metodo __init__
    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

    # metodos a, b, c
    def a(self, ladoA):
        return self.ladoA
    def b(self, ladoB):
        return self.ladoB
    def c(self, ladoC):
        return self.ladoC
    
    # metodo para calcular o perimetro
    def perimetro(self):
        return (self.ladoA + self.ladoB + self.ladoC)