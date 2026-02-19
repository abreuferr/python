"""
AUTOR   : Caio Abreu Ferreira <abreuferr (a) gmail.com>
TÍTULO  : Remoção de duplicatas e soma de elementos
SOBRE   :Fornece duas funções utilitárias para listas numéricas:
  - remove_repetidos : elimina elementos duplicados e ordena a lista.
  - soma_elementos   : calcula a soma de todos os elementos da lista.
"""

def remove_repetidos(lista: list) -> list:
    """
    Remove elementos duplicados de uma lista e a retorna ordenada.

    Utiliza `set` para eliminar duplicatas de forma eficiente e
    converte o resultado de volta para lista antes de ordenar.

    Parâmetros:
        lista (list): Lista de elementos (comparáveis e hasheáveis).

    Retorna:
        list: Nova lista sem duplicatas, em ordem crescente.

    Exemplo:
        >>> remove_repetidos([7, 3, 33, 12, 3, 7])
        [3, 7, 12, 33]
    """
    # set() elimina duplicatas automaticamente; sorted() retorna lista ordenada
    return sorted(set(lista))


def soma_elementos(lista: list) -> float:
    """
    Calcula e retorna a soma de todos os elementos de uma lista numérica.

    Parâmetros:
        lista (list): Lista de números a serem somados.

    Retorna:
        float: Soma total dos elementos.

    Exemplo:
        >>> soma_elementos([3, 7, 12, 33, 100])
        155
    """
    return sum(lista)


# ── Execução principal ───────────────────────────────────────────────────────

if __name__ == "__main__":
    # Lista original com valores repetidos
    lista_original = [7, 3, 33, 12, 3, 3, 3, 7, 12, 100]
    print(f"Lista original       : {lista_original}")

    # Remove os elementos duplicados e ordena a lista
    lista_sem_duplicatas = remove_repetidos(lista_original)
    print(f"Sem duplicatas       : {lista_sem_duplicatas}")

    # Calcula a soma dos elementos sem duplicatas
    total = soma_elementos(lista_sem_duplicatas)
    print(f"Soma dos elementos   : {total}")