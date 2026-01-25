import math  # Biblioteca usada para cálculo de raiz quadrada


def eh_primo(n):
    """
    Função que verifica se um número é primo.
    Retorna True se for primo, False caso contrário.
    """

    # Números menores que 2 não são primos
    if n < 2:
        return False

    # O número 2 é primo
    if n == 2:
        return True

    # Se for par e maior que 2, não é primo
    if n % 2 == 0:
        return False

    # Testa divisores ímpares até a raiz quadrada de n
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False  # Encontrou divisor, não é primo

    return True  # Nenhum divisor encontrado, é primo


def fatorar_em_dois_primos(n):
    """
    Tenta fatorar o número n em dois números primos.
    Retorna uma tupla (p, q) se possível, ou None caso contrário.
    """

    # Testa possíveis divisores de 2 até a raiz quadrada de n
    for i in range(2, int(math.sqrt(n)) + 1):

        # Verifica se i é divisor de n
        if n % i == 0:
            j = n // i  # Segundo fator

            # Verifica se ambos os fatores são primos
            if eh_primo(i) and eh_primo(j):
                return i, j  # Retorna os dois primos encontrados

    # Se não encontrar dois fatores primos
    return None


if __name__ == "__main__":
    # Solicita um número inteiro ao usuário
    numero = int(input("Digite um número inteiro: "))

    # Tenta fatorar o número em dois primos
    resultado = fatorar_em_dois_primos(numero)

    # Verifica o resultado
    if resultado:
        p, q = resultado
        print(f"{numero} = {p} × {q}")
    else:
        print("Não foi possível fatorar o número em dois números primos.")