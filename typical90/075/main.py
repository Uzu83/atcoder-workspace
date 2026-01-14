import sys


def prime_factorization(n):
    """
    素因数分解を行い、素因数のリストを返す関数
    計算量:O(√N)
    """
    factors = []

    # 2で割れるだけ割る
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # 3以上の奇数で割っていく
    f = 3
    while f * f <= n:
        if n % f == 0:
            factors.append(f)
            n //= f

        else:
            f += 2

    # 最後に残った数が1でなければ,それも素因数
    if n != 1:
        factors.append(n)

    return factors


def solve():
    input = sys.stdin.readline
    N = int(input())

    # ステップ1: 素因数分解して、要素の個数を数える
    factors = prime_factorization(N)
    K = len(factors)

    # ステップ2: 2^x >= K となる最小の x を探す
    x = 0
    while (1 << x) < K:
        x += 1

    print(x)


if __name__ == "__main__":
    solve()
