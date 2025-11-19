import sys
input = sys.stdin.readline

# H, Wの受け取り
H,W = map(int,input().split())


# コーナーケースチェック
if H == 1 or W == 1:
    print(H * W)

else:
    print(((H + 1) // 2) * ((W + 1) // 2))