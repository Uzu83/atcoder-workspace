import sys
import math


def solve():
    input = sys.stdin.readline

    # T: 1周にかかる時間
    t_period = float(input())

    # L: 観覧車の高さ(直径), X, Y: 像の座標
    l_height, x_statue, y_statue = map(int, input().split())

    # Q: クエリ数
    q_count = int(input())

    # 定数計算
    # 半径 r
    radius = l_height / 2

    # クエリ処理
    for _ in range(q_count):
        e_time = int(input())

        # 1. 回転角 theta (ラジアン) の計算
        # 1周(2π) を T分 で回る
        theta = (2 * math.pi * e_time) / t_period

        # 2. 観覧車上の座標 (0, y_pos, z_pos) の計算
        # 問題文の挙動に合わせた三角関数
        # sin, cos の因数はラジアン
        y_pos = -1 * radius * math.sin(theta)
        z_pos = radius - (radius * math.cos(theta))

        # 3. 俯角の計算
        # 水平距離 (XY平面上の距離)
        # 自分のx座標は常に0
        dx = x_statue - 0
        dy = y_statue - y_pos
        horizontal_dist = math.sqrt(dx**2 + dy**2)

        # 俯角 (depression angle)
        # atan2(y, x) は y/x のアークタンジェントを返す
        # ここでは 高さ / 水平距離
        angle_rad = math.atan2(z_pos, horizontal_dist)

        # 度数法に変換して出力
        print(math.degrees(angle_rad))


if __name__ == "__main__":
    solve()
