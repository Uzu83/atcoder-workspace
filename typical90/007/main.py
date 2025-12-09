import sys
import bisect


def solve():
    input = sys.stdin.readline
    N = int(input().rstrip())
    rate_list = list(map(int, input().split()))
    Q = int(input().rstrip())

    # Pythonでの無限大の表現
    INF = 10**18

    rate_list_sorted = sorted(rate_list)

    for _ in range(Q):
        rate = int(input().rstrip())

        # 挿入すべき位置を探す
        idx = bisect.bisect_left(rate_list_sorted, rate)

        diff = INF

        # 候補1: 自分より大きい (または等しい) 値との差
        # idx が N (リストの末尾) の時は存在しないのでスキップ
        if idx < N:
            diff = min(diff, abs(rate_list_sorted[idx] - rate))

        # 候補2: 自分より小さい値との差
        # idx が 0 (リストの先頭) の時は存在しないのでスキップ
        if idx > 0:
            diff = min(diff, abs(rate_list_sorted[idx - 1] - rate))

        print(diff)


if __name__ == "__main__":
    solve()
