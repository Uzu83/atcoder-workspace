import sys


def solve():
    input = sys.stdin.readline
    N = int(input())
    S = input().rstrip()

    # ステップ1: 全区間の個数を計算
    # 1からNまでの整数の和と同じ公式
    total_intervals = N * (N + 1) // 2

    # ステップ2: 条件を満たさない (oだけ、xだけ) 区間を数える
    bad_intervals = 0
    current_length = 0

    for i in range(N):
        current_length += 1

        # 次の文字が変わる、または文字列の最後に来たら、ここまでの連続区間を精算
        if i == N - 1 or S[i] != S[i + 1]:
            # 長さ current_length の区間の中に含まれる部分文字列の数
            # k * (k+1) / 2
            bad_intervals += current_length * (current_length + 1) // 2

            # 長さをリセット
            current_length = 0

    # ステップ3: 全体からダメな区間を引く
    print(total_intervals - bad_intervals)


if __name__ == "__main__":
    solve()
