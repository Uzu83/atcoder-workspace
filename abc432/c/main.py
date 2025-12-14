import sys


def solve():
    input = sys.stdin.readline

    N, X, Y = map(int, input().split())
    A_list = list(map(int, input().split()))

    diff = Y - X
    major = A_list[0] * X

    for i in range(N):
        if ((A_list[i] * X) - major) % diff != 0:
            print(-1)
            return

    max_weight = min(A_list) * Y
    min_weight = max(A_list) * X

    if max_weight < min_weight:
        print(-1)
        return

    best_weight = max_weight - ((max_weight - major) % diff)

    if best_weight < min_weight:
        print(-1)
        return

    ans = 0
    for i in range(N):
        X_count = (best_weight - (A_list[i] * X)) // diff
        ans += X_count

    print(ans)


if __name__ == "__main__":
    solve()
