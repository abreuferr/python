import random
import pygame

# =========================
# CONFIGURAÇÕES DO JOGO
# =========================
LARGURA_GRADE = 80   # número de colunas
ALTURA_GRADE = 60    # número de linhas
TAMANHO_CELULA = 10  # pixels

PROB_VIVO = 0.25     # probabilidade inicial de uma célula nascer viva
FPS = 15             # quadros por segundo (velocidade da simulação)

COR_FUNDO = (0, 0, 0)        # preto
COR_CELULA = (0, 255, 0)     # verde
COR_GRADE = (40, 40, 40)     # cinza escuro

# =========================
# FUNÇÕES DA SIMULAÇÃO
# =========================

def cria_grade(largura, altura, prob_vivo=0.25):
    """Cria uma grade aleatória de células vivas/mortas."""
    grade = []
    for _ in range(altura):
        linha = [1 if random.random() < prob_vivo else 0 for _ in range(largura)]
        grade.append(linha)
    return grade

def conta_vizinhos_toro(grade, x, y):
    """
    Conta vizinhos vivos da célula (x, y) usando borda toroidal.
    Ou seja, se sair pela direita, volta pela esquerda, etc.
    """
    altura = len(grade)
    largura = len(grade[0])
    vizinhos = 0

    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            if dx == 0 and dy == 0:
                continue  # ignora a própria célula

            nx = (x + dx) % largura
            ny = (y + dy) % altura

            vizinhos += grade[ny][nx]
    return vizinhos

def proxima_geracao(grade):
    """Calcula a próxima geração da grade."""
    altura = len(grade)
    largura = len(grade[0])

    nova = [[0] * largura for _ in range(altura)]

    for y in range(altura):
        for x in range(largura):
            vivos = conta_vizinhos_toro(grade, x, y)
            if grade[y][x] == 1:
                # célula viva
                if vivos == 2 or vivos == 3:
                    nova[y][x] = 1  # continua viva
                else:
                    nova[y][x] = 0  # morre
            else:
                # célula morta
                if vivos == 3:
                    nova[y][x] = 1  # nasce
    return nova

# =========================
# DESENHO COM PYGAME
# =========================

def desenha_grade(screen, grade):
    """Desenha todas as células na tela."""
    altura = len(grade)
    largura = len(grade[0])

    screen.fill(COR_FUNDO)

    # desenha células
    for y in range(altura):
        for x in range(largura):
            if grade[y][x] == 1:
                rect = pygame.Rect(
                    x * TAMANHO_CELULA,
                    y * TAMANHO_CELULA,
                    TAMANHO_CELULA,
                    TAMANHO_CELULA
                )
                pygame.draw.rect(screen, COR_CELULA, rect)

    # desenha linhas da grade (opcional, só pra ficar bonito)
    for x in range(largura + 1):
        pygame.draw.line(
            screen,
            COR_GRADE,
            (x * TAMANHO_CELULA, 0),
            (x * TAMANHO_CELULA, altura * TAMANHO_CELULA),
            1
        )
    for y in range(altura + 1):
        pygame.draw.line(
            screen,
            COR_GRADE,
            (0, y * TAMANHO_CELULA),
            (largura * TAMANHO_CELULA, y * TAMANHO_CELULA),
            1
        )

def pos_mouse_para_celula(pos):
    """Converte coordenadas de pixel do mouse para coordenadas da grade."""
    x_pix, y_pix = pos
    x = x_pix // TAMANHO_CELULA
    y = y_pix // TAMANHO_CELULA
    return x, y

# =========================
# LOOP PRINCIPAL
# =========================

def main():
    pygame.init()
    largura_tela = LARGURA_GRADE * TAMANHO_CELULA
    altura_tela = ALTURA_GRADE * TAMANHO_CELULA

    screen = pygame.display.set_mode((largura_tela, altura_tela))
    pygame.display.set_caption("Jogo da Vida de Conway - Toroidal (Pygame)")

    clock = pygame.time.Clock()

    grade = cria_grade(LARGURA_GRADE, ALTURA_GRADE, PROB_VIVO)
    rodando = True
    pausado = False

    while rodando:
        # =========================
        # EVENTOS
        # =========================
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    rodando = False
                elif event.key == pygame.K_SPACE:
                    pausado = not pausado
                elif event.key == pygame.K_c:
                    # limpa a grade
                    grade = [[0] * LARGURA_GRADE for _ in range(ALTURA_GRADE)]
                elif event.key == pygame.K_r:
                    # randomiza de novo
                    grade = cria_grade(LARGURA_GRADE, ALTURA_GRADE, PROB_VIVO)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # alterna célula viva/morta com o mouse
                if event.button == 1:  # botão esquerdo
                    x, y = pos_mouse_para_celula(event.pos)
                    if 0 <= x < LARGURA_GRADE and 0 <= y < ALTURA_GRADE:
                        grade[y][x] = 1 - grade[y][x]  # toggle

        # Se o mouse estiver pressionado, pode "desenhar" célula viva
        if pygame.mouse.get_pressed()[0]:
            x, y = pos_mouse_para_celula(pygame.mouse.get_pos())
            if 0 <= x < LARGURA_GRADE and 0 <= y < ALTURA_GRADE:
                grade[y][x] = 1

        # =========================
        # LÓGICA DA SIMULAÇÃO
        # =========================
        if not pausado:
            grade = proxima_geracao(grade)

        # =========================
        # DESENHO
        # =========================
        desenha_grade(screen, grade)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()

