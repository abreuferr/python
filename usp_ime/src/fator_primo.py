# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : Calcula os fatores primos e multiplicidades de um número
#              Exemplo: 1000 = 2³ × 5³

def fatorar(numero: int) -> list[tuple[int, int]]:
    """
    Recebe um número inteiro maior que 1 e retorna uma lista de tuplas
    no formato (fator_primo, multiplicidade).

    Exemplo:
        fatorar(1000) -> [(2, 3), (5, 3)]
        pois 1000 = 2³ × 5³
    """
    fatores = []  # lista que armazenará os pares (fator, multiplicidade)
    fator = 2     # menor fator primo possível

    # itera apenas até a raiz quadrada do número, pois todo fator primo
    # maior que a raiz quadrada só pode aparecer uma única vez no final
    while fator * fator <= numero:
        multiplicidade = 0  # contador de quantas vezes o fator divide o número

        # divide o número pelo fator atual enquanto for divisível,
        # contando quantas vezes a divisão é possível (multiplicidade)
        while numero % fator == 0:
            multiplicidade += 1
            numero //= fator  # divisão inteira para evitar erros de ponto flutuante

        # só registra o fator se ele dividiu o número ao menos uma vez
        if multiplicidade > 0:
            fatores.append((fator, multiplicidade))

        fator += 1  # avança para o próximo candidato a fator

    # se após o loop ainda restar um número maior que 1,
    # ele é necessariamente um fator primo (com multiplicidade 1)
    if numero > 1:
        fatores.append((numero, 1))

    return fatores


def main():
    # leitura e validação da entrada do usuário
    try:
        numero = int(input("Digite um número inteiro maior que 1: "))
        if numero <= 1:
            raise ValueError  # rejeita valores fora do domínio esperado
    except ValueError:
        print("Entrada inválida. Digite um número inteiro maior que 1.")
        return

    # exibe os fatores primos e suas respectivas multiplicidades
    for fator, multiplicidade in fatorar(numero):
        print(f"fator: {fator}  |  multiplicidade: {multiplicidade}")


# garante que main() só é executada quando o script é rodado diretamente,
# e não quando importado como módulo por outro arquivo
if __name__ == "__main__":
    main()