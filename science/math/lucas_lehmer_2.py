"""
Verificador de Primalidade
===========================
Baseado no algoritmo de Lucas-Lehmer descrito em:
"How to Identify a Prime Number without a Computer" - Scientific American (2025)
por Manon Bischoff

Estratégia:
  - Se o número for da forma 2^p - 1 (Mersenne) → usa o Teste de Lucas-Lehmer
  - Caso contrário → usa divisão por tentativa (trial division)
"""

import math


# ─── Algoritmos ──────────────────────────────────────────────────────────────

def lucas_lehmer(p: int) -> bool:
    """
    Testa se o número de Mersenne M(p) = 2^p - 1 é primo.
    Requer que p seja primo.
    """
    if p == 2:
        return True  # M(2) = 3 é primo

    M = (1 << p) - 1  # 2^p - 1
    s = 4
    for _ in range(p - 2):
        s = (s * s - 2) % M

    return s == 0


def trial_division(n: int) -> bool:
    """Verifica primalidade por divisão por tentativa."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.isqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def mersenne_exponent(n: int) -> int | None:
    """
    Se n for um número de Mersenne (2^p - 1), retorna p.
    Caso contrário, retorna None.
    """
    m = n + 1
    if m < 2 or (m & (m - 1)) != 0:
        return None
    return m.bit_length() - 1


def verificar_primo(n: int) -> tuple[bool, str]:
    """
    Verifica se n é primo e retorna o método utilizado.

    Returns:
        (é_primo, método_usado)
    """
    exp = mersenne_exponent(n)

    if exp is not None and trial_division(exp):
        # n é um número de Mersenne com expoente primo → Lucas-Lehmer
        primo = lucas_lehmer(exp)
        metodo = f"Lucas-Lehmer (2^{exp} − 1)"
    else:
        primo = trial_division(n)
        metodo = "Divisão por tentativa (Trial Division)"

    return primo, metodo


# ─── Interface interativa ─────────────────────────────────────────────────────

def main():
    print("=" * 55)
    print("  VERIFICADOR DE PRIMALIDADE — LUCAS-LEHMER")
    print("=" * 55)
    print("  Digite um número inteiro para saber se é primo.")
    print("  Para sair, digite 'sair' ou pressione Ctrl+C.")
    print("=" * 55)

    while True:
        print()
        entrada = input("  🔢 Digite um número: ").strip()

        if entrada.lower() in ("sair", "exit", "quit", "q"):
            print("\n  Encerrando. Até mais! 👋\n")
            break

        try:
            n = int(entrada)
        except ValueError:
            print("  ⚠️  Entrada inválida. Digite um número inteiro.")
            continue

        if n < 0:
            print(f"  ℹ️  {n} é negativo. Números primos são positivos maiores que 1.")
            continue

        primo, metodo = verificar_primo(n)

        print(f"\n  Número   : {n}")
        print(f"  Método   : {metodo}")

        if primo:
            print(f"  Resultado: ✅ {n} É PRIMO")
        else:
            print(f"  Resultado: ❌ {n} NÃO é primo")

            # Mostra um divisor para curiosidade
            if n >= 4:
                for d in range(2, int(math.isqrt(n)) + 1):
                    if n % d == 0:
                        print(f"  Divisível por {d} → {n} = {d} × {n // d}")
                        break

        print("  " + "-" * 40)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n  Encerrando. Até mais! 👋\n")
