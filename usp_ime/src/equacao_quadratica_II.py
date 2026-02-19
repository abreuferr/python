"""
AUTOR      : Caio Abreu Ferreira <abreuferr (a) gmail.com>
TÍTULO     : Equação do segundo grau (ax² + bx + c = 0)
SOBRE       : Calcula as raízes reais de uma equação quadrática usando a Fórmula de Bhaskara.

Fórmulas:
    Δ  = b² - 4ac
    x  = (-b ± √Δ) / (2a)

Casos possíveis:
    Δ > 0  →  duas raízes reais distintas (x1 e x2)
    Δ = 0  →  uma raiz real dupla (x1 = x2)
    Δ < 0  →  nenhuma raiz real (raízes complexas)
"""

import math


# ── Funções ──────────────────────────────────────────────────────────────────

def calcular_delta(a: float, b: float, c: float) -> float:
    """
    Calcula o discriminante (Δ) da equação quadrática ax² + bx + c = 0.

    Parâmetros:
        a, b, c (float): Coeficientes da equação.

    Retorna:
        float: Valor do discriminante Δ = b² - 4ac.

    Exemplo:
        >>> calcular_delta(1, -5, 6)
        1.0
    """
    return b ** 2 - 4 * a * c


def calcular_raizes(a: float, b: float, delta: float) -> tuple[float, float]:
    """
    Calcula as duas raízes reais pela Fórmula de Bhaskara.

    Deve ser chamada apenas quando delta >= 0.

    Parâmetros:
        a     (float): Coeficiente quadrático (≠ 0).
        b     (float): Coeficiente linear.
        delta (float): Discriminante pré-calculado (deve ser ≥ 0).

    Retorna:
        tuple[float, float]: Par (x1, x2) com x1 ≥ x2.
        Quando delta == 0, x1 == x2 (raiz dupla).

    Exemplos:
        >>> calcular_raizes(1, -5, 1)   # delta = b²-4ac = 25-24 = 1
        (3.0, 2.0)                       # x = (5 ± 1) / 2
    """
    raiz_delta = math.sqrt(delta)
    x1 = (-b + raiz_delta) / (2 * a)
    x2 = (-b - raiz_delta) / (2 * a)
    return x1, x2


def coletar_coeficiente(nome: str) -> float:
    """
    Solicita ao usuário um coeficiente numérico, repetindo até entrada válida.

    Parâmetros:
        nome (str): Nome do coeficiente exibido no prompt (ex: 'a', 'b', 'c').

    Retorna:
        float: Valor numérico informado pelo usuário.
    """
    while True:
        try:
            return float(input(f"  Valor de {nome}: "))
        except ValueError:
            print(f"  Entrada inválida. '{nome}' deve ser um número. Tente novamente.")


# ── Execução principal ───────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=== EQUAÇÃO DO SEGUNDO GRAU ===")
    print("       ax² + bx + c = 0\n")

    # Coleta os coeficientes com validação de entrada
    while True:
        a = coletar_coeficiente("a")
        if a != 0:
            break
        print("  O coeficiente 'a' não pode ser zero (seria equação linear).\n")

    b = coletar_coeficiente("b")
    c = coletar_coeficiente("c")

    # Exibe a equação montada com os valores fornecidos
    print(f"\nEquação: ({a})x² + ({b})x + ({c}) = 0")

    # Calcula o discriminante
    delta = calcular_delta(a, b, c)
    print(f"Δ = {b}² - 4×{a}×{c} = {delta:.4f}\n")

    # Analisa o valor de delta e exibe o resultado correspondente
    if delta > 0:
        # Duas raízes reais distintas
        x1, x2 = calcular_raizes(a, b, delta)
        print("Duas raízes reais distintas:")
        print(f"  x1 = {x1:.4f}")
        print(f"  x2 = {x2:.4f}")

    elif delta == 0:
        # Uma raiz real dupla (x1 == x2)
        x1, _ = calcular_raizes(a, b, delta)
        print("Uma raiz real dupla:")
        print(f"  x1 = x2 = {x1:.4f}")

    else:
        # Delta negativo: raízes complexas (sem solução no conjunto dos reais)
        print("Nenhuma raiz real.")
        print(f"  Δ = {delta:.4f} < 0 → raízes complexas (não reais).")