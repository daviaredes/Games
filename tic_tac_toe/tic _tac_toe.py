rounds = 0

def start():
    global scorer
    print('Welcome to Tic Tac Toe\n ___|___|___ \n ___|___|___\n    |   |   ')
    print('If you don t know how to play, type 3\nBut first choose your marking 1 == X or 2 == O')
    try:
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


def bot(board, bot_option):
    from random import randint
    opponent_bot = randint(1, 9)
    checker_bot = len(board[opponent_bot - 1])
    if checker_bot == 1:
       print('bot e igaul')
       pass
    else:
        board[opponent_bot- 1] = bot_option
        pass


def main():
    board = [[], [], [], [], [], [], [], [], []]

    start()

    while True:
        try:
            player_move = int(input('what position: '))
            if player_move < 1 or player_move > 9:
                print('No to this option, the choice goes from 1 to 9 only')
                continue
            checker_player = len(board[player_move - 1])
            if checker_player == 1:
                print('Has already been played in this house try another one')
                continue
            
            if scorer == 1:
                board[player_move - 1] = 'X'
                bot_option = 'O'
            elif scorer == 2:
                board[player_move - 1] = 'O'
                bot_option = 'X'
                
            if board[0] and board[1] and board[2] == 'X' or board[3] and board[4] and board[5] == 'X' or board[6] and board[7] and board[8] == 'X':
                print('X ganhou')
                break
            elif board[0] == 'O' and board[1] == 'O' and board[2] == 'O' or board[3] == 'O' and board[4] == 'O' and board[5] == 'O' or board[6] == 'O' and board[7] == 'O' and board[8] == 'O':
                print('O ganhou')
                break

        except:
            print('\n   No to this option, the choice goes from 1 to 9 only\n')
            continue

        bot(board, bot_option)
        print(board)

main()
