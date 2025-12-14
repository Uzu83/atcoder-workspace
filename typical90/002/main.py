import sys


def solve():
    input = sys.stdin.readline

    N = int(input().rstrip())

    if N % 2 != 0:
        return

    candidates_list = []
    for i in range(1 << N):
        candidate = ""
        for j in range(N - 1, -1, -1):
            if (i >> j) & 1 == 0:
                candidate += "("
            else:
                candidate += ")"

        candidates_list.append(candidate)

    for candidate in candidates_list:
        count = 0
        for char in candidate:
            if char == "(":
                count += 1
            else:
                count -= 1

            if count < 0:
                break

        if count == 0:
            print(candidate)


if __name__ == "__main__":
    solve()
