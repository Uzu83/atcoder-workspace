import sys


def solve():
    input = sys.stdin.readline
    N = int(input())

    if N % 2 != 0:
        return

    candidates = []
    for i in range(1 << N):
        candidate = ""
        for j in reversed(range(N)):
            if (i >> j) & 1:
                candidate += ")"
            else:
                candidate += "("
        candidates.append(candidate)

    for candidate in candidates:
        count = 0
        for char in candidate:
            if char == "(":
                count += 1
            else:
                count -= 1

            if count < 0:
                break

        if count != 0:
            continue
        else:
            print(candidate)


if __name__ == "__main__":
    solve()
