import sys


def solve():
    input = sys.stdin.readline

    # 1. 入力の受け取り
    n = int(input().rstrip())

    a, b, c = map(int, input().split())

    # 2. 定数の設定
    # 問題文の制約 「効果の合計枚数は9999枚以下」に基づく探索上限
    max_coins = 9999

    # 最小枚数を格納する変数。初期値は上限値で設定
    min_total_coins = max_coins

    # 3. 全探索処理
    # i: A円硬貨の枚数 (0 から max_coins まで)
    for i in range(max_coins + 1):
        # A円硬貨だけでN円を超えたら、それ以上探索しても無駄なのでbreak
        if a * i > n:
            break

        # j: B円硬貨の枚数 (0 から 残りの許容枚数 まで)
        # i + j が max_coins を超えない範囲で探索
        for j in range(max_coins - i + 1):

            # 現在の合計金額を計算
            current_sum = a * i + b * j

            # 合計がNを超えていたら、このjのループはこれ以上増やしても無駄なのでbreak
            if current_sum > n:
                break

            # 残りの金額 (C円硬貨で払うべき金額)
            remainder = n - current_sum

            # 残額が0以上 かつ Cで割り切れる場合のみ、解の候補となる
            if remainder % c == 0:
                # k: C円硬貨の枚数
                k = remainder // c

                # 合計枚数を計算
                total_coins = i + j + k

                # 最小値を更新
                # 制約上 total_coins <= 9999 は保証されるが、念のためminをとる
                if total_coins < min_total_coins:
                    min_total_coins = total_coins

    # 4. 結果の出力
    print(min_total_coins)


if __name__ == "__main__":
    solve()
