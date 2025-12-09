import sys


def solve():
    input = sys.stdin.readline

    # 1. 入力受け取り
    N = int(input().rstrip())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 2. ソート (Greedy戦略の準備)
    # 小さい順に並べることで、「左端の人」と「左端の学校」を対応させる準備をする
    A.sort()
    B.sort()

    # 3. 距離の総和を計算
    ans = 0
    # zip関数を使うと、A[0]とB[0], A[1]とB[1]...というペアを簡単に作れる
    for a, b in zip(A, B):
        ans += abs(a - b)

    print(ans)


if __name__ == "__main__":
    solve()
