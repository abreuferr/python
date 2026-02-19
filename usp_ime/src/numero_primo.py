"""
AUTOR       : Caio Abreu Ferreira <abreuferr (a) gmail.com>
TÍTULO      : Verificação de número primo
SOBRE       : Verifica se um número inteiro informado pelo usuário é primo ou não.
            O programa continua solicitando números até que o usuário digite 0 para sair.
            Um número é primo se for maior que 1 e divisível apenas por 1 e por ele mesmo.
"""

import math


def is_primo(numero: int) -> bool:
    """
    Verifica se um número inteiro é primo.

    Utiliza a otimização de testar divisores apenas até a raiz quadrada
    do número, reduzindo a complexidade de O(n) para O(√n).
    Também trata os casos especiais de números menores que 2 e
    o número 2 (único primo par).

    Parâmetros:
        numero (int): Número inteiro a ser verificado.

    Retorna:
        bool: True se o número for primo, False caso contrário.

    Exemplos:
        >>> is_primo(7)
        True
        >>> is_primo(9)
        False
        >>> is_primo(1)
        False
    """
    # Números menores que 2 não são primos por definição
    if numero < 2:
        return False

    # 2 é o único número primo par
    if numero == 2:
        return True

    # Números pares maiores que 2 nunca são primos
    if numero % 2 == 0:
        return False

    # Testa divisores ímpares de 3 até √numero.
    # Se nenhum dividir exatamente, o número é primo.
    # Testar até √numero é suficiente: se numero = a × b e a > √numero,
    # então b < √numero, e b já teria sido encontrado antes.
    for fator in range(3, math.isqrt(numero) + 1, 2):
        if numero % fator == 0:
            return False

    return True


def coletar_numero(mensagem: str) -> int:
    """
    Solicita ao usuário um número inteiro, repetindo até obter entrada válida.

    Parâmetros:
        mensagem (str): Texto exibido no prompt de entrada.

    Retorna:
        int: Valor inteiro informado pelo usuário.
    """
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("  Entrada inválida. Digite apenas números inteiros.")


# ── Execução principal ───────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=== VERIFICADOR DE NÚMEROS PRIMOS ===")
    print("(Digite 0 para sair)\n")

    while True:
        numero = coletar_numero("Digite um número inteiro (≥ 2): ")

        # Encerra o programa se o usuário digitar 0
        if numero == 0:
            print("Encerrando o programa.")
            break

        # Valida se o número está no intervalo aceito
        if numero < 2:
            print("  Por favor, digite um número maior ou igual a 2.\n")
            continue

        # Verifica e exibe se o número é primo ou não
        if is_primo(numero):
            print(f"  {numero} É primo. ✓\n")
        else:
            print(f"  {numero} NÃO é primo. ✗\n")