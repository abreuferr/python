"""
AUTOR      : Caio Abreu Ferreira <abreuferr (a) gmail.com>
TÍTULO     : Distância entre dois pontos
SOBRE      : Calcula a distância euclidiana entre dois pontos A(xa, ya) e B(xb, yb)
            no plano cartesiano e classifica como 'perto' ou 'longe' (limiar: 10).
            Fórmula: d = √((xb - xa)² + (yb - ya)²)
"""

import math


# Limiar que define se os pontos são considerados próximos ou distantes
LIMIAR_DISTANCIA = 10


def calcular_distancia(xa: float, ya: float, xb: float, yb: float) -> float:
    """
    Calcula a distância euclidiana entre os pontos A e B.

    Parâmetros:
        xa, ya (float): Coordenadas do ponto A.
        xb, yb (float): Coordenadas do ponto B.

    Retorna:
        float: Distância entre os dois pontos.

    Exemplo:
        >>> calcular_distancia(0, 0, 3, 4)
        5.0
    """
    # Diferença entre as coordenadas de cada eixo
    delta_x = xb - xa
    delta_y = yb - ya

    # Teorema de Pitágoras: d = √(Δx² + Δy²)
    # math.hypot é equivalente a sqrt(x² + y²), porém mais preciso e conciso
    return math.hypot(delta_x, delta_y)


def classificar_distancia(distancia: float, limiar: float = LIMIAR_DISTANCIA) -> str:
    """
    Classifica a distância como 'longe' ou 'perto' com base em um limiar.

    Parâmetros:
        distancia (float): Distância calculada entre os pontos.
        limiar    (float): Valor de corte (padrão: 10).

    Retorna:
        str: 'longe' se distância >= limiar, caso contrário 'perto'.
    """
    return "longe" if distancia >= limiar else "perto"


def coletar_coordenada(nome: str) -> float:
    """
    Solicita ao usuário uma coordenada numérica, repetindo até obter entrada válida.

    Parâmetros:
        nome (str): Nome da coordenada exibido no prompt (ex: 'xa').

    Retorna:
        float: Valor numérico informado pelo usuário.
    """
    while True:
        try:
            return float(input(f"Insira o valor de {nome}: "))
        except ValueError:
            print(f"  Entrada inválida. '{nome}' deve ser um número. Tente novamente.")


# ── Execução principal ───────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=== DISTÂNCIA ENTRE DOIS PONTOS ===\n")

    # Coleta as coordenadas dos dois pontos com validação de entrada
    print("Ponto A:")
    xa = coletar_coordenada("xa")
    ya = coletar_coordenada("ya")

    print("\nPonto B:")
    xb = coletar_coordenada("xb")
    yb = coletar_coordenada("yb")

    # Calcula a distância entre os pontos
    distancia = calcular_distancia(xa, ya, xb, yb)

    # Classifica a distância com base no limiar definido
    classificacao = classificar_distancia(distancia)

    # Exibe o resultado de forma descritiva
    print(f"\nA({xa}, {ya})  →  B({xb}, {yb})")
    print(f"Distância    : {distancia:.2f}")
    print(f"Classificação: {classificacao} (limiar: {LIMIAR_DISTANCIA})")