# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : Calcula o fatorial de um número inteiro não negativo.
#              Exemplo: 5! = 5 × 4 × 3 × 2 × 1 = 120
# OBS        : Estruturado em funções para facilitar o uso com Pytest


def fatorial(numero: int) -> int:
    """
    Calcula o fatorial de um número inteiro não negativo.

    Parâmetros:
        numero (int): valor de entrada, deve ser >= 0

    Retorna:
        int: o fatorial de 'numero'

    Exemplos:
        fatorial(0) -> 1   (por definição matemática, 0! = 1)
        fatorial(5) -> 120
    """
    # caso base: 0! e 1! são iguais a 1 por definição
    if numero == 0:
        return 1

    resultado = 1  # acumulador do produto

    # multiplica resultado por cada inteiro de 'numero' até 2
    # (não é necessário multiplicar por 1, pois não altera o valor)
    while numero > 1:
        resultado *= numero  # equivalente a: resultado = resultado * numero
        numero -= 1          # decrementa o contador

    return resultado


def main():
    # leitura e validação da entrada do usuário
    try:
        numero = int(input("Digite o valor de n: "))
        if numero < 0:
            raise ValueError  # fatorial não é definido para negativos
    except ValueError:
        print("Entrada inválida. Digite um número inteiro maior ou igual a 0.")
        return

    # calcula e exibe o resultado
    resultado = fatorial(numero)
    print(f"{numero}! = {resultado}")


# garante que main() só é executada quando o script é rodado diretamente,
# e não quando importado como módulo (ex: pelo Pytest)
if __name__ == "__main__":
    main()