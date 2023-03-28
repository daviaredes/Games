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


def bot(board, bot_option):
    from random import randint
    bot = randint(1, 9)
    board[bot - 1] = bot_option


def main():
    board = [[], [], [], [], [], [], [], [], []]
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
            except:
                print('\n   No to this option, the choice goes from 1 to 9 only\n')
                continue

        bot(board, bot_option)
        print(f' _{board[0]}_|_{board[1]}_|_{board[2]}_ \n _{board[3]}_|_{board[4]}_|_{board[5]}_\n  {board[6]} | {board[7]} | {board[8]} \n')
    
main()
 