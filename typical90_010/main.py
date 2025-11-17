import sys
input = sys.stdin.readline

# 生徒の番号,成績の受け取りと累積和の作成
N = int(input().rstrip())
class_1 = [0] * (N + 1)
class_2 = [0] * (N + 1)
for i in range(1,N+1):
    class_1[i] = class_1[i-1]
    class_2[i] = class_2[i-1]
    class_num, score = map(int,input().split())
    if class_num == 1:
        class_1[i] += score
    else:
        class_2[i] += score

# キューの処理
Q = int(input().rstrip())
for _ in range(Q):
    l,r = map(int,input().split())
    ans_1 = class_1[r] - class_1[l-1]
    ans_2 = class_2[r] - class_2[l-1]
    print(ans_1,ans_2)