#join-k solution

t = int(raw_input())
for i in range(1,t+1):
    param = raw_input().split(' ')
    n = int(param[0])
    k = int(param[1])
    board = []
    for j in range(1,n+1):
        line = raw_input()
        for l in range(1,n+1):
            board[j-1][l-1] = line[l-1]
        print board
