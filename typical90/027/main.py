import sys

def solve():
    input = sys.stdin.readline
    
    
    usernames = set()
    N = int(input().rstrip())
    
    for i in range(N):
        username = input().rstrip()
        
        if username not in usernames:
            print(i+1)
            usernames.add(username)


if __name__ == "__main__":
    solve()