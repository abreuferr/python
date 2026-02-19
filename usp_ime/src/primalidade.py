# -*- coding: utf-8 -*-
# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : Verifica se um número inteiro é primo ou não.
#              Um número primo é divisível apenas por 1 e por ele mesmo.
#              Exemplos: 2, 3, 5, 7, 11, 13 são primos.


def eh_primo(numero: int) -> bool:
    """
    Verifica se um número inteiro é primo.

    Parâmetros:
        numero (int): número a ser verificado.

    Retorna:
        bool: True se o número for primo, False caso contrário.

    Exemplos:
        eh_primo(2)  -> True
        eh_primo(9)  -> False  (9 = 3 × 3)
        eh_primo(13) -> True
    """
    # números menores que 2 não são primos por definição
    if numero < 2:
        return False

    # 2 é o único número primo par
    if numero == 2:
        return True

    # todo número par maior que 2 não é primo
    if numero % 2 == 0:
        return False

    # testa divisores ímpares a partir de 3 até a raiz quadrada do número.
    # basta ir até a raiz pois, se número = a × b e a > √número,
    # então b < √número já teria sido encontrado antes.
    divisor = 3
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return False  # encontrou um divisor: não é primo
        divisor += 2  # avança de 2 em 2, pulando números pares

    # nenhum divisor encontrado: o número é primo
    return True


def main():
    # leitura e validação da entrada do usuário
    try:
        numero = int(input("Digite um número inteiro: "))
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")
        return

    # exibe o resultado de forma clara
    if eh_primo(numero):
        print(f"{numero} é primo.")
    else:
        print(f"{numero} não é primo.")


# garante que main() só é executada quando o script é rodado diretamente,
# e não quando importado como módulo (ex: pelo Pytest)
if __name__ == "__main__":
    main()