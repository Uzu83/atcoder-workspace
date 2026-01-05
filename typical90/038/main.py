import sys
import math


def solve():
    input = sys.stdin.readline

    A, B = map(int, input().split())
    ans = A * B // math.gcd(A, B)

    if ans > 10**18:
        print("Large")
    else:
        print(ans)


if __name__ == "__main__":
    solve()
