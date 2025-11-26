import sys
from collections import defaultdict

def solve():
    input = sys.stdin.readline
    
    N, M = map(int, input().split())
    A = list(map(int, input().rstrip().split()))
    
    # Step 1: 前準備
    # 「もし自分が "上" にきたら、、余りはどうなる？」を全通り計算してメモする
    #
    # cnt[k][r] :=
    # 「後ろに k 桁の数字がついたとき、全体を M で割った余りが r になるような、
    #  前側(Ai)の数字の個数」
    
    
    # 桁数(1~10)ごとに辞書を作る
    cnt = [defaultdict(int) for _ in range(11)]
    
    for a in A:
        # 後ろに来る数字の桁数 k (1桁~10桁) を想定してループ
        for k in range(1, 11):
            # a を 10^k 倍して M で割った余りを計算
            # pow(10, k, M) は (10**k) % M を高速にやる書き方
            rem = (a * pow(10, k, M)) % M
            
            # 「k桁ずらして余りが rem になるやつ、ここに１個いたよ！」 と記録
            cnt[k][rem] += 1
    
    
    # ---------------------------------------------------------
    # Step 2: 本番 (Main Loop)
    # 自分が "下（Suffix）" になったとき、相方が何人いるか数える
    # ---------------------------------------------------------
    ans = 0

    for a in A:
        # 自分の桁数を調べる (これが Step 1 の k になる)
        # str(a) は遅いので len(str(a)) だけ使う
        L = len(str(a))
        
        # 自分の余り
        my_rem = a % M
        
        # 相方(上に来る数字)に求める余り
        # (相方 + 自分) % M == 0 にしたいので、
        # 相方の余りは (M - 自分) % M になればいい
        target_rem = (M - my_rem) % M
        
        # 「L桁ズラしたときの余りが target_rem になるやつ」は何人いる？
        count = cnt[L][target_rem]
        
        ans += count

    print(ans)

if __name__ == "__main__":
    solve()