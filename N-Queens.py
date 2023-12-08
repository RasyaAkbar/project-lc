#What is the board of n queens that don't attack each other?
ans = []
q = int(input("Input the number of queens "))
def board_valid(board, row, column):
    #check column
    for i in range(row, -1, -1):
        if board[i][column] == "Q": return False
    #check left diagonal
    i, j = row, column
    while i>=0 and j>=0:
        if board[i][j] == "Q": return False
        i-=1
        j-=1
    #check right diagonal
    i, j = row, column
    while i>=0 and j<len(board):
        if board[i][j] == "Q": return False
        i-=1
        j+=1
    return True

def dfs(board, row):
    if row == len(board):
        ans.append(board[:])
        return
    for column in range(len(board)):
        if board_valid(board, row, column):
            board[row]=board[row][:column]+ "Q"+ board[row][column+1:]
            dfs(board, row+1)
            board[row]=board[row][:column]+ "."+ board[row][column+1:]

def Queens():
    board = ["."*q]*q
    dfs(board, 0)
    return ans

print("Your queen board is: ")
for i in range(len(Queens())):
    print('\n')
    for j in Queens()[i]:
        print(j)
