import random

directions = [(1,0), (0,1), (-1,0), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]
signal = None

# create board
board = []
bound = 15
for i in range(bound):
    row = []
    for s in range(bound):    
        row.append('.')
    board.append(row)

def display(grid: list[list[str]]):
    for i in range(len(grid)+ 1):
        print(f"{i:02d}", end=' ')
    print()
    board = ''
    for i in range(len(grid)):
        row = f"{i+1:02d}" + '  '
        for s in range(len(grid[i])):
            row += grid[i][s] + '  '
            
        # line break at the end of each line except the last one 
        if i != len(grid) - 1:
            row += '\n'

        board += row
    print(board)

def get_set(board, side):
    empty = []
    for y in range(bound):
        for x in range(bound):
            if board[y][x] == side:
                empty.append((y, x))
    return empty

def check_gameover(board):
    if not get_set(board, '.'):
        print('No one wins!')
        print("Game over.")
        return True
    else:
        return False
    
def check_win(board: list[list[str]]) -> bool:
    for y in range(bound):
        for x in range(bound):
            if board[y][x] == '.':
                continue

            for dx, dy in directions:              
                if all(0 <= y + i*dy < bound and 0 <= x + i*dx < bound and board[y + i*dy][x + i*dx] == 'X' for i in range(5)):
                    print('You win!')
                    return True
                elif all(0 <= y + i*dy < bound and 0 <= x + i*dx < bound and board[y + i*dy][x + i*dx] == 'O' for i in range(5)):
                    print('AI wins!')
                    return True
    return False

def block_three(board: list[list[str]]) -> bool:
    global signal
    for y in range(bound):
        for x in range(bound):
            for dx, dy in directions:    
                try:            
                    if all(board[y + i*dy][x + i*dx] == 'X' for i in range(3)):
                        before_x = x - dx
                        before_y = y - dy
                        after_x = x + 3*dx
                        after_y = y + 3*dy

                        options = []

                        if (0 <= before_x < bound and 0 <= before_y < bound and board[before_y][before_x] == 'O') or \
   (0 <= after_x < bound and 0 <= after_y < bound and board[after_y][after_x] == 'O'):
                            return False

                        if 0 <= before_x <= bound and 0 <= before_y <= bound:
                            if board[before_y][before_x] == '.':
                                options.append((before_y, before_x))

                        if 0 <= after_x <= bound and 0 <= after_y <= bound:
                            if board[after_y][after_x] == '.':
                                options.append((after_y, after_x))

                        if options:
                            final_y, final_x = random.choice(options)
                            if final_x == before_x and final_y == before_y:
                                signal = (after_y, after_x)
                            elif final_x == after_x and final_y == after_y:
                                signal = (before_y, before_x)
                            board[final_y][final_x] = 'O'
                            display(board)
                            return True
                except IndexError:
                    continue  
    signal = None
    return False

def need_to_block_four(board: list[list[str]]) -> bool:
    global signal
    print(signal)
    if signal is None:
        return False

    y = signal[0]
    x = signal[1]

    if (y < 0 or
        y > bound or
        x < 0 or
        x > bound):
        signal = None
        return False
    for dx, dy in directions:    
        try:            
            if all(board[y + i*dy][x + i*dx] == 'X' for i in range(4)):
                block_x = x - dx
                block_y = y - dy
                if 0 <= block_x < bound and 0 <= block_y < bound and board[block_y][block_x] == '.':
                    board[block_y][block_x] = 'O'
                    signal = None
                    display(board)
                    return True
        except IndexError:
            continue 
    signal = None
    return False

def ordinary_move(board):
    if not get_set(board, 'O'):
        y, x = random.choice(get_set(board, '.'))
        board[y][x] = 'O'
        display(board)
        return True
    else:
        while True:
            y, x = random.choice(get_set(board, 'O'))
            for dx, dy in directions:
                if 0 < y + dy < bound and 0 < x + dx < bound and board[y + dy][x + dx] == '.':
                    board[y + dy][x + dx] = 'O'
                    display(board)
                    return True

def ai_move(board):
    if need_to_block_four(board):
        return True
    if block_three(board):
        return True
    if ordinary_move(board):
        return True
    return False

if __name__ == '__main__':
    print(board)
    display(board)
