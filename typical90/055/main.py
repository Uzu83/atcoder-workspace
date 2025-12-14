import sys


def solve():
    input = sys.stdin.readline

    N, P, Q = map(int, input().split())
    A_list = [int(x) % P for x in list(map(int, input().split()))]

    count = 0
    for i in range(N):
        x1 = A_list[i]
        for j in range(i + 1, N):
            x2 = (x1 * A_list[j]) % P
            for k in range(j + 1, N):
                x3 = (x2 * A_list[k]) % P
                for l in range(k + 1, N):
                    x4 = (x3 * A_list[l]) % P
                    for m in range(l + 1, N):
                        x5 = (x4 * A_list[m]) % P
                        if x5 == Q:
                            count += 1

    print(count)


if __name__ == "__main__":
    solve()
