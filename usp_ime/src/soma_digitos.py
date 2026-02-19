"""
AUTOR      : Caio Abreu Ferreira <abreuferr (a) gmail.com>
TÍTULO     : Soma dos dígitos de um número inteiro
SOBRE      : Calcula a soma de todos os dígitos de um número inteiro informado pelo usuário.
             Exemplo: 6532 → 6 + 5 + 3 + 2 = 16
"""

def soma_digitos(numero: int) -> int:
    """
    Calcula a soma de todos os dígitos de um número inteiro.

    Converte o número para string para iterar sobre cada dígito,
    tornando a lógica mais simples e legível do que operações
    aritméticas de módulo e divisão inteira.

    Parâmetros:
        numero (int): Número inteiro (positivo ou negativo).

    Retorna:
        int: Soma de todos os dígitos do número.

    Exemplos:
        >>> soma_digitos(6532)
        16
        >>> soma_digitos(-731)
        11
    """
    # abs() garante que números negativos sejam tratados corretamente,
    # ignorando o sinal "-" na conversão para string
    return sum(int(digito) for digito in str(abs(numero)))


# ── Execução principal ───────────────────────────────────────────────────────

if __name__ == "__main__":
    # Coleta o número informado pelo usuário e valida a entrada
    while True:
        try:
            numero = int(input("Digite um número inteiro: "))
            break  # entrada válida, sai do loop
        except ValueError:
            print("Entrada inválida. Por favor, digite apenas números inteiros.")

    # Calcula a soma dos dígitos
    total = soma_digitos(numero)

    # Exibe o resultado de forma descritiva
    digitos = " + ".join(str(d) for d in str(abs(numero)))
    print(f"Soma dos dígitos de {numero}: {digitos} = {total}")