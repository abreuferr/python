"""
============================================================
  Algoritmo de Huffman — Demonstração Completa em Python
============================================================
  Etapas demonstradas:
    1. Contagem de frequências dos caracteres
    2. Construção da árvore de Huffman (min-heap)
    3. Geração dos códigos binários
    4. Codificação (encode) da mensagem
    5. Decodificação (decode) da mensagem
    6. Exibição de estatísticas de compressão
============================================================
"""

import heapq
from collections import Counter


# ──────────────────────────────────────────────
# Nó da Árvore de Huffman
# ──────────────────────────────────────────────
class No:
    def __init__(self, caractere, frequencia):
        self.caractere = caractere
        self.frequencia = frequencia
        self.esquerda = None
        self.direita = None

    # heapq precisa comparar nós — comparamos pela frequência
    def __lt__(self, outro):
        return self.frequencia < outro.frequencia

    def __repr__(self):
        return f"No('{self.caractere}', {self.frequencia})"


# ──────────────────────────────────────────────
# 1. Contar frequências
# ──────────────────────────────────────────────
def contar_frequencias(texto: str) -> dict:
    return dict(Counter(texto))


# ──────────────────────────────────────────────
# 2. Construir a árvore de Huffman
# ──────────────────────────────────────────────
def construir_arvore(frequencias: dict) -> No:
    heap = [No(ch, freq) for ch, freq in frequencias.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        esq = heapq.heappop(heap)   # menor frequência
        dir = heapq.heappop(heap)   # segunda menor

        # nó interno: caractere None, frequência = soma dos filhos
        interno = No(None, esq.frequencia + dir.frequencia)
        interno.esquerda = esq
        interno.direita = dir

        heapq.heappush(heap, interno)

    return heap[0]  # raiz da árvore


# ──────────────────────────────────────────────
# 3. Gerar tabela de códigos (recursivo)
# ──────────────────────────────────────────────
def gerar_codigos(no: No, prefixo: str = "", tabela: dict = None) -> dict:
    if tabela is None:
        tabela = {}

    if no is not None:
        if no.caractere is not None:          # folha
            tabela[no.caractere] = prefixo or "0"
        else:
            gerar_codigos(no.esquerda, prefixo + "0", tabela)
            gerar_codigos(no.direita,  prefixo + "1", tabela)

    return tabela


# ──────────────────────────────────────────────
# 4. Codificar o texto
# ──────────────────────────────────────────────
def codificar(texto: str, tabela: dict) -> str:
    return "".join(tabela[ch] for ch in texto)


# ──────────────────────────────────────────────
# 5. Decodificar a string binária
# ──────────────────────────────────────────────
def decodificar(bits: str, raiz: No) -> str:
    resultado = []
    no_atual = raiz

    for bit in bits:
        no_atual = no_atual.esquerda if bit == "0" else no_atual.direita

        if no_atual.caractere is not None:   # chegou a uma folha
            resultado.append(no_atual.caractere)
            no_atual = raiz                  # volta para a raiz

    return "".join(resultado)


# ──────────────────────────────────────────────
# Impressão visual da árvore (opcional)
# ──────────────────────────────────────────────
def imprimir_arvore(no: No, prefixo: str = "", lado: str = "Raiz"):
    if no is not None:
        label = f"'{no.caractere}'" if no.caractere else f"[{no.frequencia}]"
        print(f"{prefixo}{lado}: {label} (freq={no.frequencia})")
        imprimir_arvore(no.esquerda, prefixo + "    ", "0 ─►")
        imprimir_arvore(no.direita,  prefixo + "    ", "1 ─►")


# ──────────────────────────────────────────────
# Programa principal
# ──────────────────────────────────────────────
def main():
    print("=" * 60)
    print("       ALGORITMO DE HUFFMAN — DEMONSTRAÇÃO")
    print("=" * 60)

    texto = "este é um exemplo do algoritmo de huffman em python"
    print(f"\n📄 Texto original  : {texto!r}")
    print(f"   Comprimento     : {len(texto)} caracteres")

    # ── Etapa 1: Frequências ──────────────────
    frequencias = contar_frequencias(texto)
    print("\n📊 Frequências dos caracteres:")
    for ch, freq in sorted(frequencias.items(), key=lambda x: -x[1]):
        barra = "█" * freq
        label = repr(ch)
        print(f"   {label:<6} {freq:3d}  {barra}")

    # ── Etapa 2: Árvore ───────────────────────
    raiz = construir_arvore(frequencias)
    print("\n🌳 Estrutura da Árvore de Huffman:")
    imprimir_arvore(raiz)

    # ── Etapa 3: Tabela de Códigos ────────────
    tabela = gerar_codigos(raiz)
    print("\n🔑 Tabela de Códigos Huffman:")
    print(f"   {'Char':<8} {'Freq':<6} {'Código':<20} {'Bits'}")
    print("   " + "-" * 45)
    for ch, codigo in sorted(tabela.items(), key=lambda x: len(x[1])):
        freq = frequencias[ch]
        print(f"   {repr(ch):<8} {freq:<6} {codigo:<20} {len(codigo)}")

    # ── Etapa 4: Codificação ──────────────────
    bits = codificar(texto, tabela)
    print(f"\n✅ Texto codificado ({len(bits)} bits):")
    # exibe em blocos de 8 para facilitar a leitura
    blocos = " ".join(bits[i:i+8] for i in range(0, len(bits), 8))
    print(f"   {blocos[:80]}{'...' if len(blocos) > 80 else ''}")

    # ── Etapa 5: Decodificação ────────────────
    decodificado = decodificar(bits, raiz)
    print(f"\n🔓 Texto decodificado: {decodificado!r}")
    print(f"   Decodificação correta: {decodificado == texto}")

    # ── Estatísticas de Compressão ────────────
    bits_original = len(texto) * 8          # ASCII padrão (8 bits/char)
    bits_huffman  = len(bits)
    taxa = (1 - bits_huffman / bits_original) * 100

    print("\n📈 Estatísticas de Compressão:")
    print(f"   Bits sem compressão (ASCII) : {bits_original}")
    print(f"   Bits com Huffman            : {bits_huffman}")
    print(f"   Taxa de compressão          : {taxa:.1f}%")
    print("=" * 60)


if __name__ == "__main__":
    main()
