#各初期条件を受け取る
import sys
#n = int(sys.stdin.readline.rstrip())
n = int(sys.stdin.readline().rstrip())

# sum_list_1[i]は「学籍番号1~i」の「1組」の合計点
sum_list_1 = [0] * (n + 1)
# sum_list_2[i]は「学籍番号1~i」の「2組」の合計点
sum_list_2 = [0] * (n + 1)
"""#student_list_i[j]はiクラスの学籍番号jの生徒の成績を示す
student_list_1 = [-1] * (n + 1)
student_list_2 = [-1] * (n + 1)

for i in range(n):
    student_class, student_score = map(int,sys.stdin.readline.split())
    if student_class == 1:
        student_list_1[i+1] = student_score
    else:
        student_list_2[i+1] = student_score

#sum_list_i[j]はiクラスの学籍番号1からjまでの生徒の成績の和を示す
sum_list_1 = [0] * (n+1)
sum_list_2 = [0] * (n+1)

for i in range(1,n+1):
    if student_list_1[i] != -1:
        sum_list_1[i] = sum_list_1[i-1] + student_list_1[i]
        sum_list_2[i] = sum_list_2[i-1]
    else:
        sum_list_2[i] = sum_list_2[i-1] + student_list_2[i]
        sum_list_1[i] = sum_list_1[i-1]"""

#入力を受け取りながら累積和を作るとよりシンプル
for i in range(1,n + 1):
    student_class, student_score = map(int,sys.stdin.readline().split())

    # 1. まず、前の学籍h番号までの合計をそのまま引き継ぐ
    sum_list_1[i] = sum_list_1[i-1]
    sum_list_2[i] = sum_list_2[i-1]

    # 2. 該当するクラスの合計にだけ、今回の点数を加算する
    if student_class == 1:
        sum_list_1[i] += student_score
    else:
        sum_list_2[i] += student_score
        

#Qと各質問のLとRを受け取り出力する
#q = int(sys.stdin.readline)
q = int(sys.stdin.readline().rstrip())

# Q個の質問を処理
for _ in range(q):
    left,right = map(int,sys.stdin.readline().split())

    #累積和を使って区間[left,right]の合計を計算
    #(rightまでの合計) - (left-1までの合計)
    ans_one = sum_list_1[right] - sum_list_1[left-1]
    ans_two = sum_list_2[right] - sum_list_2[left-1]
    
    print(ans_one,ans_two)