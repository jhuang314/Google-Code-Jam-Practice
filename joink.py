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

def diag2(board,k,n):

    winner = []

    for i in range(0,n):
        streak = 1
        prev = ''
        
        for j in range(0,i):
            if board[n-i+j][j] != prev:
                streak = 1
                prev = board[n-i+j][j]
            else:
                streak += 1

            if (prev != '.') and (streak >= k) and (prev not in winner):
                winner.append(prev)

    for i in range(0,n+1):
        streak = 1
        prev = ''
        for j in range(0,n-i):
            if board[j][i+j] != prev:
                streak = 1
                prev = board[j][i+j]
            else:
                streak += 1

            if (prev != '.') and (streak >= k) and (prev not in winner):
                winner.append(prev)

    return winner


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

    d1 = diag1(board,k,n)
    d2 = diag2(board,k,n)
    cv = col(board,k)
    rv = row(board,k)

    result = []

    if 'R' in (d1+d2+cv+rv):
        if 'B' in (d1+d2+cv+rv):
            print "Case #" + str(i) + ": Both"
        else:
            print "Case #" + str(i) + ": Red"
            
    elif 'B' in (d1+d2+cv+rv):
        print "Case #" + str(i) + ": Blue"
    else:
        print "Case #" + str(i) + ": Neither"

            
