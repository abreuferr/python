import random
import os
import time
from copy import deepcopy

LARGURA = 40   # número de colunas
ALTURA = 20    # número de linhas
PROB_VIVO = 0.25  # probabilidade inicial de uma célula nascer viva
INTERVALO = 0.1   # tempo (em segundos) entre gerações

def cria_grade(largura, altura, prob_vivo=0.25):
    """Cria uma grade aleatória de células vivas/mortas."""
    grade = []
    for _ in range(altura):
        linha = [1 if random.random() < prob_vivo else 0 for _ in range(largura)]
        grade.append(linha)
    return grade

def conta_vizinhos(grade, x, y):
    """Conta os vizinhos vivos da célula (x, y)."""
    altura = len(grade)
    largura = len(grade[0])
    vizinhos = 0

    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            if dx == 0 and dy == 0:
                continue  # ignora a própria célula
            nx = x + dx
            ny = y + dy
            if 0 <= nx < largura and 0 <= ny < altura:
                vizinhos += grade[ny][nx]
    return vizinhos

def proxima_geracao(grade):
    """Calcula a próxima geração da grade."""
    altura = len(grade)
    largura = len(grade[0])
    nova = deepcopy(grade)

    for y in range(altura):
        for x in range(largura):
            vivos = conta_vizinhos(grade, x, y)
            if grade[y][x] == 1:
                # célula viva
                if vivos < 2 or vivos > 3:
                    nova[y][x] = 0  # morre
            else:
                # célula morta
                if vivos == 3:
                    nova[y][x] = 1  # nasce
    return nova

def mostra_grade(grade, geracao):
    os.system("cls" if os.name == "nt" else "clear")
    print(f"Jogo da Vida de Conway - Geração {geracao}")
    print("-" * (len(grade[0]) + 2))
    for linha in grade:
        print("|" + "".join("#" if cel == 1 else " " for cel in linha) + "|")
    print("-" * (len(grade[0]) + 2))

def main():
    grade = cria_grade(LARGURA, ALTURA, PROB_VIVO)
    geracao = 0
    try:
        while True:
            mostra_grade(grade, geracao)
            grade = proxima_geracao(grade)
            geracao += 1
            time.sleep(INTERVALO)
    except KeyboardInterrupt:
        print("\nEncerrado pelo usuário.")

if __name__ == "__main__":
    main()

