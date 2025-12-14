import sys


def long_to_base_9(num):
    if num == 0:
        return "0"

    num_list = []

    while num > 0:
        num_list.append(str(num % 9))
        num //= 9

    return "".join(reversed(num_list))


def solve():
    input = sys.stdin.readline

    N, K = input().split()
    K = int(K)

    if N == "0":
        print(0)
        return

    for i in range(K):
        N_int = int(N, 8)

        # N を 10進法 → 9進法(str)にする
        N_str_9 = long_to_base_9(N_int)

        # N の "8" を "5" に置き換え, N に再代入
        N = N_str_9.replace("8", "5")

    print(N)


if __name__ == "__main__":
    solve()
