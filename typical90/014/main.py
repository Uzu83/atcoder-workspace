import sys


def solve():
    input = sys.stdin.readline

    N = int(input().rstrip())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))

    ans = 0
    for i in range(N):
        ans += abs(A[i] - B[i])

    print(ans)


if __name__ == "__main__":
    solve()
