import sys
input = sys.stdin.readline

num = int(input().rstrip())
l = [int(x) for x in list(str(num))]

count = 0
for i in range(len(l)):
    length = 2
    for right in range(i+1,len(l)):
        if l[i] == l[right] - 1 and length % 2 == 0 and l[length // 2 - 1 + i] == l[length // 2 + i] - 1:
            count += 1
            break
        elif l[i] != l[right] and l[i] + 1 != l[right] and l[right - 1] > l[right]:
            break
        else:
            length += 1

print(count)