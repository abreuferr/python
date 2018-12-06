# importar a classe Ponto do arquivo ponto.py
from ponto import Ponto

# importar a a funcao distancia do arquivo veiculo.py
# NAO EH OOP
from ponto import distancia

# classe main()
def main():
    p = Ponto(7,6) # variavel(p) faz referencia ao objeto Ponto e instancia o mesmo
    q = Ponto(0,0) # variavel(q) faz referencia ao objeto Ponto e instancia o mesmo

    # primeiro teste
    print("nada acontece")

    # segundo teste
    print(p)
    print(q)
    print(p is q)

    # terceiro teste
    # exibir as coordenadas de x,y
    print(p.getX())
    print(p.getY())

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
    p = Ponto(3,4)
    q = Ponto(5,12)
    mid = p.meio(q) # q vai ser o alvo
    print(mid)
    print(mid.getX())
    print(mid.getY())

# main()
main()