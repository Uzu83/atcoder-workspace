import sys


def solve():
    input = sys.stdin.readline

    n = int(input())

    a = [int(x) % 46 for x in input().split()]
    b = [int(x) % 46 for x in input().split()]
    c = [int(x) % 46 for x in input().split()]

    count_a = [0] * 46
    count_b = [0] * 46
    count_c = [0] * 46

    for x in a:
        count_a[x] += 1
    for x in b:
        count_b[x] += 1
    for x in c:
        count_c[x] += 1

    ans = 0
    for i in range(46):
        for j in range(46):
            for k in range(46):
                if (i + j + k) % 46 == 0:
                    ans += count_a[i] * count_b[j] * count_c[k]

    print(ans)


if __name__ == "__main__":
    solve()
