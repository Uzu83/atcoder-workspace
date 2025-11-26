import sys

def solve():
    input = sys.stdin.readline

    N, K = map(int,input().split())
    A_line = list(map(int,input().rstrip().split()))
    B_line = list(map(int,input().rstrip().split()))

    diff = 0

    for a, b in zip(A_line, B_line):
        diff += abs(a - b)

    if diff > K or (diff - K) % 2 != 0:
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    solve()