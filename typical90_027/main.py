import sys

# 高速入力の準備
input = sys.stdin.readline

# Nの受け取り
n = int(input().rstrip())

# ここがポイント! リスト[] ではなく セット set() を使う
registered_users = set()

for i in range(n):
    username = input().rstrip()

    # セットの中にあるか確認 (これは爆速! O(1))
    if username in registered_users:
        continue
    else:
        registered_users.add(username)
        print(i + 1)