# AUTORES : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# TITULO  : Ordem lexicográfica
"""
Escreva a função primeiro_lex(lista) que recebe uma lista
de strings como parâmetro e devolve o primeiro string na
ordem lexicográfica. Neste exercício, considere letras
maiúsculas e minúsculas.
"""


def primeiro_lex(lista):
    """
    Retorna a primeira string em ordem lexicográfica de uma lista,
    considerando letras maiúsculas e minúsculas (case-insensitive).

    Parâmetros:
        lista (list[str]): Lista de strings a ser analisada.

    Retorna:
        str: O primeiro elemento na ordem lexicográfica.

    Exemplos:
        >>> primeiro_lex(['maria', 'jose', 'Catarina', 'PAULO'])
        'Catarina'
        >>> primeiro_lex(['ze', 'lu', 'fe'])
        'fe'
    """
    # Valida se a lista não está vazia para evitar erros
    if not lista:
        raise ValueError("A lista não pode estar vazia.")

    # Usa a função min() com key=str.lower para comparar de forma
    # case-insensitive, respeitando letras maiúsculas e minúsculas
    return min(lista, key=str.lower)


# ── Testes ──────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # Cada teste imprime a entrada e o resultado esperado
    casos = [
        (['maria', 'jose', 'Catarina', 'PAULO'], 'Catarina'),
        (['ze', 'lu', 'fe'],                      'fe'),
        (['banana', 'Abacaxi', 'cereja'],          'Abacaxi'),
        (['Z', 'a'],                               'a'),
    ]

    for lista, esperado in casos:
        resultado = primeiro_lex(lista)
        status = "✓" if resultado == esperado else "✗"
        print(f"{status} primeiro_lex({lista}) → '{resultado}'  (esperado: '{esperado}')")