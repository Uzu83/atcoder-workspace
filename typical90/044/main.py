import sys


def solve():
    input = sys.stdin.readline

    n, q = map(int, input().split())
    a_list = list(map(int, input().split()))

    shift_count = 0

    for _ in range(q):
        t, x, y = map(int, input().split())
        if t == 1:
            real_x = (x - 1 - shift_count) % n
            real_y = (y - 1 - shift_count) % n

            a_list[real_x], a_list[real_y] = a_list[real_y], a_list[real_x]

        elif t == 2:
            shift_count += 1

        else:
            real_x = (x - 1 - shift_count) % n
            print(a_list[real_x])
    return


if __name__ == "__main__":
    solve()
