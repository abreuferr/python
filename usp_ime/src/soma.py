"""
AUTOR   : Caio Abreu Ferreira <abreuferr (a) gmail.com>
TÍTULO  : Soma de dois números
SOBRE   : Demonstra a soma de dois números inteiros e exibe o resultado formatado.
"""


def somar(x: float, y: float) -> float:
    """
    Calcula e retorna a soma de dois números.

    Parâmetros:
        x (float): Primeiro operando.
        y (float): Segundo operando.

    Retorna:
        float: O resultado da soma de x e y.

    Exemplo:
        >>> somar(1, 2)
        3
    """
    return x + y


# ── Execução principal ───────────────────────────────────────────────────────

if __name__ == "__main__":
    # Define os valores a serem somados
    x = 1
    y = 2

    # Calcula a soma chamando a função
    resultado = somar(x, y)

    # Exibe o resultado com formatação legível usando f-string
    print(f"O resultado da soma de {x} + {y} é: {resultado}")