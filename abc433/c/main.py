import sys


def solve():
    input = sys.stdin.readline

    S = input().rstrip()

    nums_list = []
    base = None
    counter = 0

    for char in S:
        if base == None:
            base = char

        if char == base:
            counter += 1
        else:
            nums_list.append((int(base), counter))
            base = char
            counter = 1
    else:
        nums_list.append((int(base), counter))

    ans = 0
    for i in range(len(nums_list) - 1):
        if nums_list[i][0] + 1 == nums_list[i + 1][0]:
            ans += min(nums_list[i][1], nums_list[i + 1][1])

    print(ans)


if __name__ == "__main__":
    solve()
