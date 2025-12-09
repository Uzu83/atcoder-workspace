import sys


def solve():
    input = sys.stdin.readline

    N, P, Q = map(int, input().split())
    A_list = [int(x) % P for x in input().rstrip().split()]

    count = 0

    # 5重ループ
    for i in range(N):
        a1 = A_list[i]
        for j in range(i + 1, N):
            a2 = (A_list[j] * a1) % P
            for k in range(j + 1, N):
                a3 = (A_list[k] * a2) % P
                for l in range(k + 1, N):
                    a4 = (A_list[l] * a3) % P
                    for m in range(l + 1, N):
                        a5 = (A_list[m] * a4) % P
                        if a5 == Q:
                            count += 1

    print(count)


if __name__ == "__main__":
    solve()
