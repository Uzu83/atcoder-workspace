import sys
import bisect

INF = float("inf")


def solve():
    input = sys.stdin.readline

    N = int(input().rstrip())
    A = sorted(list(map(int, input().split())))
    Q = int(input().rstrip())

    for _ in range(Q):
        b = int(input().rstrip())

        # b を A に挿入するならどこか? (二分探索)
        # idx は A[idx] >= b となる最小のインデックス
        idx = bisect.bisect_left(A, b)

        # 候補1: 挿入箇所の右側 (A[idx]) との差
        # idx が N (リストの末尾) の場合は存在しないので無限大にする
        diff1 = INF
        if idx < N:
            diff1 = abs(A[idx] - b)

        # 候補2: 挿入箇所の左側 (A[idx-1]) との差
        # idx が 0 (リストの先頭) の場合は存在しないので無限大にする
        diff2 = INF
        if idx > 0:
            diff2 = abs(A[idx - 1] - b)

        print(min(diff1, diff2))


if __name__ == "__main__":
    solve()
