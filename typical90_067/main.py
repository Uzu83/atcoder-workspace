import sys
from collections import deque

def long_to_base9(n):
    """10進数の数値を9進数の数値(文字列)に変換して返す関数"""
    if n == 0:
        return "0"
    
    nums = deque()


    while n > 0:
        # 余り(%9) がその桁の数字になる
        remainder = n % 9
        nums.appendleft(str(remainder))

        #次のけたへ進むために9で割る
        n //= 9

    return "".join(nums)


def solve():
    input = sys.stdin.readline

    N_str, K = input().split()
    K = int(K)

    # コーナーケース
    if N_str == "0":
        print(0)
        return
    
    # K回繰り返す
    for _ in range(K):
        # 1. 8進数(文字列) -> 10進数(int)
        # int(文字列, 8)で一発
        n_10 = int(N_str, 8)

        # 2. 10進数(数値) -> 9進数(文字列)
        n_9_str = long_to_base9(n_10)

        # 3. "8" を "5" に書き直す -> これが次のN_strになる
        N_str = n_9_str.replace("8", "5")


    print(N_str)

if __name__ == "__main__":
    solve()