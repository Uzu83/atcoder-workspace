#生徒の人数と各生徒の成績を、クラスを判別しながら受け取る。
import sys

n = int(sys.stdin.readline().rstrip)

score_class_1 = [-1] * n
score_class_2 = [-1] * n

for i in range(n):
    num_class,score = map(int,sys.stdin.readline().stlip())
    if num_class == 1:
        score_class_1[i] = score
    else:
        score_class_2[i] = score

for i in range()