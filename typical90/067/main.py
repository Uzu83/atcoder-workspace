import sys


def long_to_9(n):
    if n == 0:
        return "0"

    n_list = []

    while n > 0:
        n_list.append(str(n % 9))
        n //= 9

    return "".join(reversed(n_list))


def solve():
    input = sys.stdin.readline

    N_str, K = input().split()
    K = int(K)

    if N_str == "0":
        print(0)
        return

    for _ in range(K):
        # 8based -> 10based
        N_int = int(N_str, 8)

        # 10based -> 9based
        N_int_9 = long_to_9(N_int)

        # "8" -> "5"
        N_str = N_int_9.replace("8", "5")

    print(N_str)


if __name__ == "__main__":
    solve()
