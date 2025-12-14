import sys
from collections import defaultdict


def solve():
    input = sys.stdin.readline

    N, M = map(int, input().split())
    # 文字列として受け取る (桁数の計算で使うため)
    S = input().split()
    # 計算用に整数リストも作る
    A = list(map(int, S))

    # 【事前計算】
    # cnt[k][r] := 配列Aの中に「10^k倍してMで割ると余りがrになる数」が何個あるか
    # kは 1~10 (A_iの最大が10^9なので桁数は最大10)
    cnt = [defaultdict(int) for _ in range(11)]

    for x in A:
        for k in range(1, 11):
            # pow(10, k, M) は10^k % Mを高速に計算する
            rem = (x * pow(10, k, M)) % M
            cnt[k][rem] += 1

    ans = 0

    # 全ての j についてペアを探す
    for i in range(N):
        x_val = A[i]
        x_len = len(S[i])

        # 式: (A_i * 10^|A_j|) % M == (M - A_j % M) % M
        # 必要な　A_i の余り (target) を計算
        x_rem = x_val % M
        target = (M - x_rem) % M

        # 桁数 x_len に対応する辞書から、 target となる余を持つ個数を足す
        ans += cnt[x_len][target]

    print(ans)


if __name__ == "__main__":
    solve()
