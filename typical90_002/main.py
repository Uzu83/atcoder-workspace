import sys

def solve():
    input = sys.stdin.readline
    N = int(input().rstrip())
    if N % 2 != 0:
        return
    
    
    # Bit全探索の型
    #
    # 2のN乗 通りをすべて試す
    # (1 << N) は 2**N と同じ意味だが、競プロではこっちが主流
    for i in range(1 << N):
        
        candidate = ""
        
        # i を２進数とみなして、N桁の文字列を作る
        # 上の桁(N-1)から下の桁(0)に向かって見ていく
        for j in range(N - 1, -1, -1):
        
            # i の j ビット目が 0 か 1 かを判定する魔法の式
            # (i >> j) & 1
            # 結果が 0 なら「(」, 1 なら「)」にする
            # (辞書順で '(' のほうが早いため、0を'('に割り当てる)
            if (i >> j) & 1 == 0:
                candidate += "("
            else:
                candidate += ")"
        
        
        # 正しいカッコ列かどうかの判定
        score = 0
        is_valid = True
        
        for char in candidate:
            if char == "(" :
                score += 1
            else:
                score -= 1
            
            # 途中でマイナスになったらアウト(例: "())")
            if score < 0:
                is_valid = False
                break
        
        #最後まで見て、スコアがちょうど0なら合格 (例:"(())")
        if is_valid and score == 0:
            print(candidate)


if __name__ == "__main__":
    solve()