import sys


def solve():
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))

    total_sum = sum(A)

    # 全体が10で割り切れない場合、1/10は整数にならないのでNo
    if total_sum % 10 != 0:
        print("No")
        return

    target = total_sum // 10

    # ポイント1 円環対策として,リストを2つ繋げて直線にする
    # これで「またぐ」ケースを考慮不要にする
    A_doubled = A + A

    # ポイント2 尺取り法
    left = 0
    current_sum = 0

    # rightを 0 から 2N-1 まで走査
    for right in range(2 * N):
        # 右端を伸ばして合計に足す
        current_sum += A_doubled[right]

        # 目標を超えている間、左端を縮めて合計から引く
        while current_sum > target:
            current_sum -= A_doubled[left]
            left += 1

        # 調整した後, 目標値と一致するか確認
        if current_sum == target:
            print("Yes")
            return

    print("No")


if __name__ == "__main__":
    solve()
