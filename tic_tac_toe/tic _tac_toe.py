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


def bot(bot_option):
    from random import randint
    opponent_bot = randint(1, 9)
    checker_bot = len(board[opponent_bot - 1])
    if checker_bot == 1:
        bot(bot_option)
    elif checker_bot == 0:
        board[opponent_bot- 1] = bot_option
        pass


def player():
    try:
        global player_move
        player_move = int(input('what position: '))
        if player_move < 1 or player_move > 9 :
            print('\n   No to this option, the choice goes from 1 to 9 only1\n')
            player()
        checker_player = len(board[player_move - 1])
        if checker_player == 1:
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

        if scorer == 1:
            board[player_move - 1] = 'X'
            bot_option = 'O'
        elif scorer == 2:
            board[player_move - 1] = 'O'
            bot_option = 'X'
            
        try:     
            bot(bot_option)
        except RecursionError:
            print('Tie, neither O won nor X won, try again and defeat me')
            break

        print(f' {board[0]}||{board[1]}||{board[2]}')
        print(f' {board[3]}||{board[4]}||{board[5]}')
        print(f' {board[6]}||{board[7]}||{board[8]}')
       
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
