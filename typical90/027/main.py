import sys
input = sys.stdin.readline

N = int(input().rstrip())

usernames = set()
for i in range(N):
    username = input().rstrip()
    if username not in usernames:
        usernames.add(username)
        print(i+1)