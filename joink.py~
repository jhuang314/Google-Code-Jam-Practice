#join-k solution

def fall(line, n):
    pointer = n-1
    line.reverse()

    index = 0
    openIndex = 0
    for c in line:
        if c != '.':
            line[index] = '.'
            line[openIndex] = c
            openIndex += 1
            
        index += 1
    line.reverse()

'''        
    for i in range(n-1,-1,-1):


        if line[i] != '.':
            line[pointer] = line[i]
            line[i] = '.'
            pointer -= 1
'''
            
def row(board,k):
    winner = []
    for r in board:
        streak = 1
        prev = ''
        r.reverse()


        for ch in r:

            if ch == '.':
                break
            else:
                if prev == ch:
                    streak += 1
                else:
                    prev = ch
                    streak = 1

            if streak >= k and (prev not in winner):
                winner.append(prev)

    return winner
                
def col(board,k):
    temp = []
    for c in zip(*board):
        if c != None:
            temp.append(list(c))

    winner = row(temp,k)
    return winner

def diag1(board,k,n):
    for c in board:
        print c
    winner = []
    for i in range(0,n):
        streak = 1
        prev = ''
        
        for j in range(0,i+1):
            if board[i-j][j] != prev:
                streak = 1
                prev = board[i-j][j]
            else:
                streak += 1
            if (prev != '.') and (streak >= k) and (prev not in winner):
                winner.append(prev)
            
#            print board[i-j][j]
    for i in range(1,n):
        streak = 1
        prev = ''
        for j in range(0,n-i):
            if board[n-j-1][i+j] != prev:
                streak = 1
                prev = board[n-j-1][i+j]
            else:
                streak += 1
            if (prev != '.') and (streak >= k) and (prev not in winner):
                winner.append(prev)
    return winner
#            print board[n-j-1][i+j]
#            print (n-j-1,i+j)

def diag2(board,k,n):
    for c in board:
        print c
    winner = []
    for i in range(n-1,-1,-1):
        streak = 1
        prev = ''
        
        for j in range(0,i+1):
            print (j,i+j)
'''            
            if board[j][i+j] != prev:
                streak = 1
                prev = board[j][i+j]
            else:
                streak += 1
            if (prev != '.') and (streak >= k) and (prev not in winner):
                winner.append(prev)
            
#            print board[i-j][j]
    for i in range(1,n):
        streak = 1
        prev = ''
        for j in range(0,n-i):
            if board[i+j][n-j-1] != prev:
                streak = 1
                prev = board[i+j][n-j-1]
            else:
                streak += 1
            if (prev != '.') and (streak >= k) and (prev not in winner):
                winner.append(prev)
'''
#    return winner


t = int(raw_input())
for i in range(1,t+1):
    param = raw_input().split(' ')
    n = int(param[0])
    k = int(param[1])
    board = []
    for j in range(1,n+1):
        line = list(raw_input())
        fall(line,n)
        board.append(line)
    print diag2(board,k,n)
#    print col(board,k)
