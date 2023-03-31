rounds = 0

def start():
    global scorer
    print('Welcome to Tic Tac Toe\n ___|___|___ \n ___|___|___\n    |   |   ')
    print('If you don t know how to play, type 3\nBut first choose your marking 1 == X or 2 == O')
    try:
        scorer = int(input('1 or 2: '))
        if scorer > 3:
            print('\nNo to this option, Choose 1 = X 2 = O or 3 = tutorial\n')
            start()
    except:
        print('\nNo to this option, Choose 1 = X 2 = O or 3 = tutorial\n')
        start()


def bot(board, board_bot, bot_option):
    from random import randint
    bot = randint(1, 9)
    l = len(board[bot - 1])
    if l == 1:
        bot = randint(1, 9)
    else:
        board_bot[bot - 1] = bot_option
        pass


def main():
    board = [[], [], [], [], [], [], [], [], []]
    board_bot = [[], [], [], [], [], [], [], [], []]

    start()

    while True:

        if scorer == 3:           
            print('\n  Well, basically the 9 positions of your choice win whoever has 3 X or 3 O in the same direction, horizontally, vertically or diagonally \n')
            print(' _1_|_2_|_3_ \n _4_|_5_|_6_\n  7 | 8 | 9 \n')
            start()
            continue
        else:
            try:
                player_move = int(input('what position: '))
                
                if scorer == 1:
                    board[player_move - 1] = 'X'
                    bot_option = 'O'
                elif scorer == 2:
                    board[player_move - 1] = 'O'
                    bot_option = 'X'
                    
                if board[0] and board[1] and board[2] == 'X' or board[3] and board[4] and board[5] == 'X' or board[6] and board[7] and board[8] == 'X':
                    print('X ganhou')
                    break
                elif board[0] and board[1] and board[2] == 'O' or board[3] and board[4] and board[5] == 'O' or board[6] and board[7] and board[8] == 'O':
                    print('O ganhou')
                    break
            except:
                print('\n   No to this option, the choice goes from 1 to 9 only\n')
                continue

        bot(board, board_bot, bot_option)
        board = board_bot
        print(board)

main()
