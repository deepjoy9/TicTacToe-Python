import os
clear = lambda: os.system("cls")

def tictactoe():
    clear()
    
    play_again = True
    print("Game is now starting:")
    while play_again:
        board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        x = 1  # for player counting 1/2
        print('PLAYER ', x, ':Enter your Marker')
        marker = input()
        player_1, player_2 = set_marker(marker)
        while True:
            if x > 2:
                x = 1
            print('PLAYER ', x, ':Enter your position')
            pos = int(input())
            # Checking whether the position is not previously filled
            if not check_pos(pos, board):
                continue

            if x == 1:
                set_board(board, player_1, pos)
            else:
                set_board(board, player_2, pos)

            dispboard(board)
            if x == 1:
                if check_win(board, player_1):
                    print('Player', x, 'Won the match')
                    break
            else:
                if check_win(board, player_2):
                    print('Player', x, 'Won the match')
                    break

            if not check_space(board):  # check if there is no space in board
                print('Draw!!!')
                break

            x = x + 1

        if not replay():
            play_again = False


def set_board(board, marker, pos):
    board[pos] = marker
    return board


def check_win(board, marker):
    return board[1] == marker and board[2] == marker and board[3] == marker or board[4] == marker and board[5] == marker and board[6] == marker or board[7] == marker and board[8] == marker and board[9] == marker or board[1] == marker and board[4] == marker and board[7] == marker or board[2] == marker and board[5] == marker and board[8] == marker or board[3] == marker and board[6] == marker and board[9] == marker or board[1] == marker and board[5] == marker and board[9] == marker or board[3] == marker and board[5] == marker and board[7] == marker


def dispboard(board):
    clear()
    print(f'  {board[7]} | {board[8]} | {board[9]}')
    print('-------------')
    print(f'  {board[4]} | {board[5]} | {board[6]}')
    print('-------------')
    print(f'  {board[1]} | {board[2]} | {board[3]}')


def replay():
    print('Do you want to play again Y/N ')
    ans = input('y/n')
    return ans == 'Y' or ans == 'y'


def set_marker(marker):
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def check_pos(pos, board):
    if board[pos] != ' ':
        print('Position is already filled')
        return False
    else:
        return True


def check_space(board):
    for i in range(1, 10):
        if board[i] == ' ':
            return True
    return False

tictactoe()
