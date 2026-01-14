import sys


def solve():
    input = sys.stdin.readline

    N, K = map(int, input().split())
    MOD = 10**9 + 7

    # 場合わけを行う

    # ケース1: ブロックが1個の場合
    # どの色でもいい
    if N == 1:
        print(K % MOD)

    # ケース2: ブロックが2個の場合
    # 1つ目はK通り,2つ目は(K-1)通り
    elif N == 2:
        ans = K * (K - 1)
        print(ans)

    # ケース3: ブロックが3個の場合
    else:
        if K < 2:
            print(0)
            return

        # 計算式: K * (K-1) * (K-2)^(N-2)

        # まず最初の2つ分
        initial_part = K * (K - 1) % MOD

        # 残りの N-2 個分は全て (K-2) 通り
        # Pythonのpow(底, 指数, 余り) は高速に計算できる
        remaining_part = pow(K - 2, N - 2, MOD)

        ans = initial_part * remaining_part % MOD
        print(ans)


if __name__ == "__main__":
    solve()
