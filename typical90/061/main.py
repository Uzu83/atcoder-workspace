import sys


def solve():
    input = sys.stdin.readline

    Q = int(input().rstrip())
    deck_upper = []
    deck_lower = []

    for _ in range(Q):
        t, x = map(int, input().split())

        if t == 1:
            deck_upper.append(x)
        elif t == 2:
            deck_lower.append(x)
        else:
            if x <= len(deck_upper):
                print(deck_upper[-x])
            else:
                idx = x - len(deck_upper) - 1
                print(deck_lower[idx])


if __name__ == "__main__":
    solve()
