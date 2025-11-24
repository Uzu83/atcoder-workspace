import sys
input = sys.stdin.readline

N = int(input().rstrip())

class_1_score_sums = [0] * (N + 1)
class_2_score_sums = [0] * (N + 1)

for i in range(1,N+1):
    class_num, score = map(int,input().split())
    class_1_score_sums[i] = class_1_score_sums[i-1]
    class_2_score_sums[i] = class_2_score_sums[i-1]


    if class_num == 1:
        class_1_score_sums[i] += score
    else:
        class_2_score_sums[i] += score

Q = int(input().rstrip())
for _ in range(Q):
    left, right = map(int,input().split())
    ans_1 = class_1_score_sums[right] - class_1_score_sums[left-1]
    ans_2 = class_2_score_sums[right] - class_2_score_sums[left-1]
    print(ans_1,ans_2)