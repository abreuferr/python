# coletando dados
largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

while altura != 0:
    l = largura
    while largura != 0:
        print('#', end = "")
        largura -= 1
    print()
    largura = l
    altura -= 1