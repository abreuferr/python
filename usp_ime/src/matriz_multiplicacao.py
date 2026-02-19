"""
AUTOR      : Caio Abreu Ferreira <abreuferr (a) gmail.com>
TÍTULO     : Multiplicação de duas matrizes
SOBRE       : Calcula o produto de duas matrizes A (m×n) e B (n×p), resultando em C (m×p).
            Regra fundamental: o número de COLUNAS de A deve ser igual ao número de
            LINHAS de B. Caso contrário, a multiplicação não é definida.
"""

# ── Tipo auxiliar para clareza ───────────────────────────────────────────────

Matriz = list[list[float]]


# ── Funções ──────────────────────────────────────────────────────────────────

def dimensao(matriz: Matriz) -> tuple[int, int]:
    """
    Retorna as dimensões (linhas, colunas) de uma matriz.

    Parâmetros:
        matriz (Matriz): Matriz representada como lista de listas.

    Retorna:
        tuple[int, int]: (número de linhas, número de colunas).

    Exemplo:
        >>> dimensao([[1, 2, 3], [4, 5, 6]])
        (2, 3)
    """
    return len(matriz), len(matriz[0])


def multiplicar_matrizes(matriz_a: Matriz, matriz_b: Matriz) -> Matriz:
    """
    Calcula o produto matricial A × B.

    Para cada elemento C[i][j] da matriz resultado, aplica a fórmula:
        C[i][j] = Σ (A[i][k] × B[k][j])  para k de 0 até n-1

    Parâmetros:
        matriz_a (Matriz): Matriz A com dimensões m×n.
        matriz_b (Matriz): Matriz B com dimensões n×p.

    Retorna:
        Matriz: Matriz resultado C com dimensões m×p.

    Lança:
        ValueError: Se o número de colunas de A ≠ número de linhas de B.

    Exemplo:
        >>> multiplicar_matrizes([[1,2],[3,4]], [[5,6],[7,8]])
        [[19, 22], [43, 50]]
    """
    linhas_a, colunas_a = dimensao(matriz_a)
    linhas_b, colunas_b = dimensao(matriz_b)

    # Pré-condição: colunas de A devem ser iguais às linhas de B
    if colunas_a != linhas_b:
        raise ValueError(
            f"Dimensões incompatíveis: A é {linhas_a}×{colunas_a} "
            f"e B é {linhas_b}×{colunas_b}. "
            f"Colunas de A ({colunas_a}) ≠ Linhas de B ({linhas_b})."
        )

    # Inicializa a matriz resultado C (m×p) preenchida com zeros
    # usando list comprehension para evitar referências compartilhadas
    matriz_c = [[0.0] * colunas_b for _ in range(linhas_a)]

    # Produto escalar: para cada célula C[i][j], soma os produtos
    # dos elementos da linha i de A pela coluna j de B
    for i in range(linhas_a):          # itera sobre as linhas de A
        for j in range(colunas_b):     # itera sobre as colunas de B
            for k in range(colunas_a): # acumula o produto escalar
                matriz_c[i][j] += matriz_a[i][k] * matriz_b[k][j]

    return matriz_c


def exibir_matriz(matriz: Matriz, nome: str = "Matriz") -> None:
    """
    Exibe uma matriz formatada no terminal, linha por linha.

    Parâmetros:
        matriz (Matriz): Matriz a ser exibida.
        nome   (str)   : Rótulo exibido antes da matriz (padrão: 'Matriz').
    """
    linhas, colunas = dimensao(matriz)
    print(f"{nome} ({linhas}×{colunas}):")

    for linha in matriz:
        # Formata cada elemento com largura fixa para alinhar as colunas
        print("  " + "  ".join(f"{valor:6.1f}" for valor in linha))

    print()  # linha em branco após a matriz


# ── Execução principal ───────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=== MULTIPLICAÇÃO DE MATRIZES ===\n")

    # Matrizes de teste: A (2×3) e B (3×2)
    matriz_a = [[1, 2, 3],
                [4, 5, 6]]

    matriz_b = [[1, 2],
                [3, 4],
                [5, 6]]

    # Exibe as matrizes de entrada
    exibir_matriz(matriz_a, "Matriz A")
    exibir_matriz(matriz_b, "Matriz B")

    # Calcula e exibe o produto A × B
    try:
        resultado = multiplicar_matrizes(matriz_a, matriz_b)
        exibir_matriz(resultado, "Resultado A × B")
    except ValueError as erro:
        print(f"Erro: {erro}")