# importar a classe Ponto do arquivo ponto.py
from ponto import Ponto

# importar a a funcao distancia do arquivo veiculo.py
# NAO EH OOP
from ponto import distancia

# classe main()
def main():
    p = Ponto(7,6) # variavel(p) faz referencia a um novo objeto da classe Ponto cujos tratributos sao 7 e 6
    q = Ponto(0,0) # variavel(q) faz referencia a um novo objeto da classe Ponto cujos tratributos sao 0 e 0

    # primeiro teste
    print("nada acontece")

    # segundo teste
    print(p) # print(Ponto(7,6))
    print(q) # print(Ponto(0,0))
    print(p is q) # falso pois sao objetos diferentes

    # terceiro teste
    # exibir as coordenadas de x,y
    print(p.getX()) # print(Ponto(7,6).getX())
    print(p.getY()) # print(Ponto(7,6).getY())

    # quarto teste
    # calcular a distancia da origem ate o ponto
    print(p.distancia_origem())

    # quinto teste (funcao + oop)
    # funcao "calcula" utilizada para calcular distancia
    # entre dois pontos
    p = Ponto(4,3)
    q = Ponto(0,0)
    print(distancia(p,q))

    # sexto teste
    # imprime string como resultado
    p = Ponto(7,6)
    print(p)

    # setimo teste
    p = Ponto(3,4) # variavel "p" contem uma referencia a um novo objeto da classe ponto
    q = Ponto(5,12) # a variavel "q" contem uma referente a um novo objeto da classe Ponto
    mid = p.meio(q) #
    print(mid)
    print(mid.getX())
    print(mid.getY())

# main()
main()