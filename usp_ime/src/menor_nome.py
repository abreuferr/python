# -*- coding: utf-8 -*-
# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : O programa encontra o menor nome dentro de uma lista de strings.

def normalizar(nomes: list[str]) -> list[str]:
    """
    Normaliza uma lista de nomes aplicando as seguintes transformações:
      1. Remove espaços em branco extras nas bordas (strip).
      2. Converte para letras minúsculas.
      3. Capitaliza a primeira letra.

    Parâmetros:
        nomes (list[str]): lista de nomes a normalizar.

    Retorna:
        list[str]: lista de nomes normalizados.

    Exemplo:
        normalizar(['  MARIA ', 'josé']) -> ['Maria', 'José']
    """
    # strip() remove espaços no início e no fim; capitalize() ajusta as maiúsculas
    # tudo em uma única passagem com list comprehension
    return [nome.strip().capitalize() for nome in nomes]


def menor_nome(nomes: list[str]) -> str:
    """
    Encontra e retorna o menor nome (em número de caracteres) de uma lista.
    Em caso de empate, retorna o primeiro nome encontrado com aquele tamanho.

    Parâmetros:
        nomes (list[str]): lista de nomes (podem conter espaços extras e
                           letras maiúsculas/minúsculas misturadas).

    Retorna:
        str: o menor nome normalizado.

    Levanta:
        ValueError: se a lista estiver vazia.

    Exemplos:
        menor_nome(['maria', 'josé', 'PAULO', 'Catarina']) -> 'José'
        menor_nome(['LU   ', ' josé ', 'PAULO', 'Catarina']) -> 'Lu'
    """
    # garante que a lista não está vazia antes de processar
    if not nomes:
        raise ValueError("A lista de nomes não pode estar vazia.")

    # normaliza os nomes antes de comparar
    nomes_normalizados = normalizar(nomes)

    # min() com key=len encontra o nome de menor comprimento de forma eficiente,
    # sem necessidade de variáveis auxiliares de controle manual
    return min(nomes_normalizados, key=len)


def main():
    # cada caso de teste exibe a lista de entrada e o menor nome encontrado
    casos = [
        ['maria', 'josé', 'PAULO', 'Catarina'],       # esperado: 'José'
        ['maria', ' josé ', '   PAULO', 'Catarina '],  # esperado: 'José'
        ['LU   ', ' josé ', 'PAULO', 'Catarina'],      # esperado: 'Lu'
        ['zé', ' lu', 'fê'],                           # esperado: 'Zé' (empate, retorna o primeiro)
    ]

    for nomes in casos:
        resultado = menor_nome(nomes)
        print(f"Entrada : {nomes}")
        print(f"Resultado: {resultado}\n")


# garante que main() só é executada quando o script é rodado diretamente
if __name__ == "__main__":
    main()