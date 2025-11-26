import sys

def solve():
    input = sys.stdin.readline
    S = input().rstrip()
    
    
    # Step 1: 連長圧縮
    # "1112222" -> [(1, 3), (2, 4)] の形にする
    
    rle = []
    if not S:
        print(0)
        return
    
    current_char = S[0]
    count = 0
    
    for char in S:
        if char == current_char:
            count += 1
        else:
            # (数字, 個数)を記録
            rle.append((int(current_char), count))
            current_char = char
            count = 1
    
    # 最後のカタマリを追加
    rle.append((int(current_char), count))
    
    
    # Step 2: 隣り合うカタマリをチェック
    ans = 0
    
    # リストの「i番目」と「i+1番目」を比較する
    for i in range(len(rle) - 1):
        num1, count1 = rle[i]
        num2, count2 = rle[i+1]
        
        # 条件: 右の数字が、左の数字 + 1 であること
        if num2 == num1 + 1:
            # 作れるペアの数は、少ない方の個数で決まる
            ans += min(count1, count2)
    
    print(ans)


if __name__ == "__main__":
    solve()