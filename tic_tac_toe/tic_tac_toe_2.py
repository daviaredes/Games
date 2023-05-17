def start():
    print('Welcome to \n _T_|_I_|_C_ \n _T_|_A_|_C_\n  T | O | E ')
    print("If you don't know how to play digit 3, But if not, choose your piece 1 == X or 2 == O")
    try:
        global scorer
        scorer = int(input('1 or 2: '))
        if scorer < 1 or scorer > 3:
            print('\nNo to this option, Choose 1 = X 2 = O or 3 = tutorial\n')
            start()
        elif scorer == 3:           
            print('\n  Well, basically the 9 positions of your choice win whoever has 3 X or 3 O in the same direction, horizontally, vertically or diagonally \n')
            print(' _1_|_2_|_3_ \n _4_|_5_|_6_\n  7 | 8 | 9 \n')
            start()
    except:
        print('\nNo to this option, Choose 1 = X 2 = O or 3 = tutorial\n')
        start()


def layout():
    print(f' {board[0]} || {board[1]} || {board[2]}')
    print(f' {board[3]} || {board[4]} || {board[5]}')
    print(f' {board[6]} || {board[7]} || {board[8]}')


def player_2():
    try:
        player_move_2 = int(input('What position player 2: '))
        if player_move_2 < 1 or player_move_2 > 9:
            print('\n   No to this option, the choice goes from 1 to 9 only1\n')
            player_2()

        checker_player_2 = len(board[player_move_2 - 1])
        if checker_player_2 == 1:
            print('\n   Has already been played in this house try another one\n')
            player_2()
        elif checker_player_2 == 0:
            board[player_move_2 - 1] = player_2_symbol
            layout()
            pass

    except:
        print('\n   No to this option, the choice goes from 1 to 9 only\n')
        player_2()       


def player():
    try:
        global player_move_1
        player_move_1 = int(input('what position Player 1: '))
        if player_move_1 < 1 or player_move_1 > 9 :
            print('\n   No to this option, the choice goes from 1 to 9 only1\n')
            player()

        checker_player_1 = len(board[player_move_1 - 1])
        if checker_player_1 == 1:
            print('\n   Has already been played in this house try another one\n')
            player()
    except:
        print('\n   No to this option, the choice goes from 1 to 9 only\n')
        player()



def main():
    global board
    board = [[], [], [], [], [], [], [], [], []]

    start()
  
    while True:
    
        player()

        global player_2_symbol
        if scorer == 1:
            board[player_move_1 - 1] = 'X'
            player_2_symbol = 'O'
        elif scorer == 2:
            board[player_move_1 - 1] = 'O'
            player_2_symbol = 'X'
        
        layout()
    
        player_2()

            # Horizontally
        if board[0] =='X' and board[3] =='X' and board[6] =='X' or board[1] =='X' and board[4] =='X' and board[7] =='X' or board[2] =='X' and board[5] =='X' and board[8] =='X':
            print('Congratulations X won, come back and play whenever you want')
            break
        elif board[0] =='O' and board[3] =='O' and board[6] =='O' or board[1] =='O' and board[4] =='O' and board[7] =='O' or board[2] =='O' and board[5] =='O' and board[8] =='O':
            print('Congratulations O won, come back and play whenever you want')
            break
            # Vertically
        if board[0] =='X' and board[1] =='X' and board[2] =='X' or board[3] =='X' and board[4] =='X' and board[5] =='X' or board[6] =='X' and board[7] =='X' and board[8] =='X':
            print('Congratulations X won, come back and play whenever you want')
            break
        elif board[0] =='O' and board[1] =='O' and board[2] =='O' or board[3] =='O' and board[4] =='O' and board[5] =='O' or board[6] =='O' and board[7] =='O' and board[8] =='O':
            print('Congratulations O won, come back and play whenever you want')
            break 
            # Diagonally
        if board[0] == 'X'  and  board[4] == 'X' and  board[8] == 'X' or  board[2] == 'X' and board[4] == 'X' and board[6] == 'X':
            print('Congratulations X won, come back and play whenever you want')
            break
        elif board[0] == 'O'  and  board[4] == 'O' and  board[8] == 'O' or  board[2] == 'O' and board[4] == 'O' and board[6] == 'O':
            print('Congratulations O won, come back and play whenever you want')
            break

main()
