import sys


def solve():
    input = sys.stdin.readline
    N = int(input().rstrip())

    if N % 2 == 1:
        return

    for i in range(1 << N):
        candidate = ""

        for j in range(N - 1, -1, -1):
            if not (i & (1 << j)):
                candidate += "("
            else:
                candidate += ")"

        score = 0
        is_valid = True

        for char in candidate:
            if char == "(":
                score += 1
            else:
                score -= 1

            if score < 0:
                is_valid = False
                break

        if is_valid and score == 0:
            print(candidate)


if __name__ == "__main__":
    solve()
