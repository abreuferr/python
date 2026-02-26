"""
Teste de Primalidade de Lucas-Lehmer
======================================
Baseado no algoritmo descrito em:
"How to Identify a Prime Number without a Computer" - Scientific American (2025)
por Manon Bischoff

O teste verifica se um número de Mersenne M(p) = 2^p - 1 é primo.

Algoritmo:
  1. Defina s0 = 4
  2. Para cada n: s_{n+1} = s_n^2 - 2  (mod M(p))
  3. M(p) é primo se e somente se s_{p-2} ≡ 0 (mod M(p))
"""


def lucas_lehmer(p: int) -> bool:
    """
    Testa se o número de Mersenne M(p) = 2^p - 1 é primo.

    Args:
        p: Expoente primo a ser testado

    Returns:
        True se M(p) for primo, False caso contrário
    """
    if p == 2:
        return True  # M(2) = 3 é primo

    M = (1 << p) - 1  # 2^p - 1

    s = 4
    for _ in range(p - 2):
        s = (s * s - 2) % M

    return s == 0


def is_prime(n: int) -> bool:
    """Verifica se n é primo (usado para validar o expoente p)."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def encontrar_mersenne_primos(limite_p: int) -> list[int]:
    """
    Encontra todos os primos de Mersenne M(p) = 2^p - 1
    para p primo até o limite fornecido.

    Args:
        limite_p: Valor máximo de p a verificar

    Returns:
        Lista dos expoentes p cujo M(p) é primo
    """
    expoentes = []
    for p in range(2, limite_p + 1):
        if is_prime(p) and lucas_lehmer(p):
            expoentes.append(p)
    return expoentes


# ─── Demonstração ────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 60)
    print("  TESTE DE PRIMALIDADE DE LUCAS-LEHMER")
    print("=" * 60)

    # Exemplo do artigo: 2^5 - 1 = 31
    print("\n📌 Exemplo do artigo: M(5) = 2⁵ - 1 = 31")
    p = 5
    M = (1 << p) - 1
    resultado = lucas_lehmer(p)
    print(f"   M({p}) = {M}")
    print(f"   É primo? {'✅ SIM' if resultado else '❌ NÃO'}")

    # Exemplo de não-primo: 2^11 - 1 = 2047 = 23 × 89
    print("\n📌 Contraexemplo: M(11) = 2¹¹ - 1 = 2047 = 23 × 89")
    p = 11
    M = (1 << p) - 1
    resultado = lucas_lehmer(p)
    print(f"   M({p}) = {M}")
    print(f"   É primo? {'✅ SIM' if resultado else '❌ NÃO'}")

    # O número famoso que Lucas provou manualmente: 2^127 - 1
    print("\n📌 O número de Lucas: M(127) = 2¹²⁷ - 1")
    p = 127
    M = (1 << p) - 1
    resultado = lucas_lehmer(p)
    print(f"   M({p}) = {M}")
    print(f"   ({len(str(M))} dígitos)")
    print(f"   É primo? {'✅ SIM' if resultado else '❌ NÃO'}")
    print("   (Maior primo encontrado sem computador, por Édouard Lucas)")

    # Busca de primos de Mersenne até p = 62
    limite = 62
    print(f"\n{'=' * 60}")
    print(f"  PRIMOS DE MERSENNE com p ≤ {limite}")
    print(f"{'=' * 60}")
    expoentes = encontrar_mersenne_primos(limite)
    print(f"\n{'p':>5}  {'M(p) = 2^p - 1':>45}  {'Dígitos':>8}")
    print("-" * 65)
    for p in expoentes:
        M = (1 << p) - 1
        s = str(M)
        exibir = s if len(s) <= 20 else s[:10] + "..." + s[-7:]
        print(f"{p:>5}  {exibir:>45}  {len(s):>8}")

    print(f"\nTotal encontrado: {len(expoentes)} primos de Mersenne")
    print("=" * 60)
