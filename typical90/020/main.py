import sys


def solve():
    input = sys.stdin.readline

    a, b, c = map(int, input().split())

    right_val = c**b

    if a < right_val:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    solve()
