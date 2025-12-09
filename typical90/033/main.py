import sys

def solve():
    input = sys.stdin.readline
    H, W = map(int,input().split())
    
    
    #コーナーケースチェック
    if H == 1 or W == 1:
        print(H * W)
        return
    
    
    print(((H + 1) // 2) * ((W + 1) // 2))


if __name__ == "__main__":
    solve()