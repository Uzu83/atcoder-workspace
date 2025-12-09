import sys


def solve():
    input = sys.stdin.readline
    S = input().rstrip()
    N = len(S)

    if N == 0:
        print(0)
        return

    # 1. ランレングス圧縮 (RLE)
    # rle = [(数字, 個数), (数字, 個数), ...]
    rle = []

    current_num = int(S[0])
    count = 1

    for i in range(1, N):
        next_num = int(S[i])
        if next_num == current_num:
            count += 1
        else:
            rle.append((current_num, count))
            current_num = next_num
            count = 1
    # 最後のブロックを追加
    rle.append((current_num, count))

    # 2. 隣り合うブロックをチェック
    ans = 0
    # ブロックのペアを見ていく
    for i in range(len(rle) - 1):
        val1, len1 = rle[i]
        val2, len2 = rle[i + 1]

        # 条件: 前の数字 + 1 が 後ろの数字
        if val1 + 1 == val2:
            # 作れるペアの数は、少ない方の長さに依存する
            ans += min(len1, len2)

    print(ans)


if __name__ == "__main__":
    solve()
