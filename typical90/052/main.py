import sys


def solve():
    input = sys.stdin.readline
    n = int(input())

    ans = 1
    for _ in range(n):
        ans *= sum(map(int, input().split()))
        ans %= 10**9 + 7

    print(ans)

    return


if __name__ == "__main__":
    solve()
