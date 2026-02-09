import sys


def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    S = set(list(input().rstrip()))
    T = set(list(input().rstrip()))
    common = S & T
    S_only = S - common
    T_only = T - common
    Q = int(input())
    for i in range(Q):
        word = set(list(input().rstrip()))
        if S_only & word:
            print("Takahashi")
        elif T_only & word:
            print("Aoki")
        else:
            print("Unknown")


if __name__ == "__main__":
    solve()
