"""
AUTOR      : Caio Abreu Ferreira <abreuferr (a) gmail.com>
TÍTULO     : Tabuada de 0 a 10
SOBRE      : Calcula e exibe a tabuada completa de 1 a 10,
             formatada em colunas alinhadas para fácil leitura.
"""

def exibir_tabuada(limite: int = 10) -> None:
    """
    Exibe a tabuada de 1 até `limite` em formato de tabela.

    Parâmetros:
        limite (int): Valor máximo da tabuada (padrão: 10).
    """
    # Cabeçalho com os multiplicadores (colunas)
    cabecalho = "\t" + "\t".join(f"x{col}" for col in range(1, limite + 1))
    print(cabecalho)
    print("-" * (limite * 8))  # linha separadora

    # Itera sobre cada linha da tabuada (multiplicando)
    for linha in range(1, limite + 1):

        # Exibe o rótulo da linha seguido dos resultados
        print(f"{linha}\t", end="")

        # Itera sobre cada coluna (multiplicador) e calcula o produto
        for coluna in range(1, limite + 1):
            print(linha * coluna, end="\t")

        # Quebra de linha ao final de cada linha da tabuada
        print()


# ── Execução principal ───────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=== TABUADA DE 1 A 10 ===\n")
    exibir_tabuada(limite=10)