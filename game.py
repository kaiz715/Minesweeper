import random



def print_board(board):
    for i in board:

        for j in i:
            print(j, end =" ")
        print()
    print()
    
lost, won = False, False
board = [[None for i in range(18)] for j in range(15)]

board_visible = [[None for i in range(18)] for j in range(15)]

def populate_board(board, mines):
    coords = []
    for i in range(mines):
        r = random.randint(0,269)
        while r in coords:
            r = random.randint(0,269)
        coords.append(r)
    
    for i in coords:
        board[i//18][i%18] = "*"

def calculate_numbers(board):
    for i in range(15):
        for j in range(18):
            if board[i][j] == "*":
                continue
            surmines = 0
            surroundings = [(i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)]
            surroundings_adj = []
            for k in range(len(surroundings)):
                if not(-1 in surroundings[k] or 15 == surroundings[k][0] or 18 == surroundings[k][1]):
                    surroundings_adj.append(surroundings[k])
            for k in surroundings_adj:
                if board[k[0]][k[1]] == "*":
                    surmines+=1
            board[i][j] = surmines
            
def reveal(x,y):
    global lost

    board_visible[x][y] = board[x][y]
    if board_visible[x][y] == "*":
        lost = True
    if board_visible[x][y] == 0:
        
        surroundings = [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]
        surroundings_adj = []
        for k in range(len(surroundings)):
            if not(-1 in surroundings[k] or 15 == surroundings[k][0] or 18 == surroundings[k][1]):
                surroundings_adj.append(surroundings[k])
        
        to_search = surroundings_adj
        already_search = to_search.copy()
        while len(to_search) != 0:
            x = to_search[0][0]
            y = to_search[0][1]
            board_visible[x][y] = board[x][y]
            if board[x][y] == 0:
                surroundings = [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]
                surroundings_adj = []
                for k in range(len(surroundings)):
                    if not(-1 in surroundings[k] or 15 == surroundings[k][0] or 18 == surroundings[k][1]):
                        surroundings_adj.append(surroundings[k])
                for i in surroundings_adj:
                    if i not in already_search:
                        to_search.append(i)
                        already_search.append(i)
            to_search.pop(0)

def win_check(board):
    global won
    count = 0
    for i in board:
        for j in i:
            if type(j) == int and j > -1:
                count+=1
    if count==240:
        return True
    return False