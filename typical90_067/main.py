import sys

def long_to_base9(n):
    """10進数の整数を9進数の文字列に変換する関数"""
    if n == 0:
        return "0"
    
    res = []
    while n > 0:
        # 9で割った余りを記録 (一番下の桁から決まる)
        res.append(str(n % 9))
        # 9で割って桁を下げる
        n //= 9

    # 下の桁から順に入れたので、ひっくり返して結合
    return "".join(res[::-1])

def solve():
    input = sys.stdin.readline

    # Nは最初「文字列」として受け取るのがコツ (int(N, 8)で使うため)
    N_str, K = input().split()
    K = int(K)

    # コーナーケース： N=0 の場合は何もしなくていい
    if N_str == "0":
        print(0)
        return

    
    for _ in range(K):
        # 1. 8進数(文字列) -> 10進数(数値)
        # int(string, base) を使うと一撃!
        n_10 = int(N_str, 8)

        # 2. 10進数(数値) -> 9進数(文字列)
        n_9_str = long_to_base9(n_10)

        # 3. "8" を "5"　に書き直す -> これが次の N_str になる
        N_str = n_9_str.replace("8", "5")

    print(N_str)


if __name__ == "__main__":
    solve()