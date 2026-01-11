import sys


def solve():
    input = sys.stdin.readline

    N, L = map(int, input().split())

    dp = [0] * (N + 1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, N + 1):
        dp[i] = dp[i - 1]
        if i >= L:
            dp[i] += dp[i - L]

    dp[i] %= 10**9 + 7

    print(dp[N] % (10**9 + 7))


if __name__ == "__main__":
    solve()
