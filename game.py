import create_board
from create_board import board
from time import sleep

bound = 10
def main():
    print('Let\'s start the game!')
    # waiting 1s
    print('Round 1')
    player = 'Y'

    while True:
        if player == 'Y':
            print('It\'s your turn!')
            sleep(0.5)
            print('...') 
            sleep(0.5) 
            coordinate = input('Enter (x y)(1-10): ').split()

            if len(coordinate) != 2:
                print('Error: expected <x> <y>')
                continue
        
            x = int(coordinate[0]) - 1
            y = int(coordinate[1]) - 1
            if x < 0 or x > bound or y < 0 or y > bound:
                print('Error: out of bounds')
            elif board[y][x] != '.':
                print(f'Error: ({x}, {y}) occupied by \'{board[y][x]}\'')
            else:
                board[y][x] = 'X'
                create_board.display(board)
                if create_board.check_win(board) or create_board.check_gameover(board):
                    break
                player = 'N'
        else:
            print('Waiting for AI ...')
            sleep(0.5)
            print('...') 
            sleep(0.5) 
            print('...') 
            sleep(0.5) 
            create_board.ai_move(board)
            if create_board.check_win(board) or create_board.check_gameover(board):
                break
            player = 'Y'

if __name__ == '__main__':
    main()
