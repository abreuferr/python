# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : Calcula os fatores primos e multiplicidades de um número
#              Exemplo: 1000 = 2³ × 5³

def fatorar(numero: int) -> list[tuple[int, int]]:
    """Retorna uma lista de tuplas (fator, multiplicidade)."""
    fatores = []
    fator = 2

    while fator * fator <= numero:
        multiplicidade = 0
        while numero % fator == 0:
            multiplicidade += 1
            numero //= fator
        if multiplicidade > 0:
            fatores.append((fator, multiplicidade))
        fator += 1

    if numero > 1:  # fator primo restante
        fatores.append((numero, 1))

    return fatores


def main():
    try:
        numero = int(input("Digite um número inteiro maior que 1: "))
        if numero <= 1:
            raise ValueError
    except ValueError:
        print("Entrada inválida. Digite um número inteiro maior que 1.")
        return

    for fator, multiplicidade in fatorar(numero):
        print(f"fator: {fator}  |  multiplicidade: {multiplicidade}")


if __name__ == "__main__":
    main()