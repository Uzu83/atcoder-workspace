import sys


def solve():
    S = input().rstrip()

    # 圧縮
    S_RL = []
    base = None
    count = 0
    for char in S:
        if base == None:
            base = char

        if base == char:
            count += 1
        else:
            S_RL.append((int(base), count))
            base = char
            count = 1
    else:
        S_RL.append((int(base), count))

    ans = 0
    for i in range(len(S_RL) - 1):
        if S_RL[i][0] + 1 == S_RL[i + 1][0]:
            ans += min(S_RL[i][1], S_RL[i + 1][1])

    print(ans)


if __name__ == "__main__":
    solve()
