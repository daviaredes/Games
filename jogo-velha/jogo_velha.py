from random import randint

escolhidos = [ ]

def painel():
    player = int(input('Escolha: '))
    escolhidos.append(player)
global player


def main():
    print('Jogo da Velha')
    print('|1|2|3|\n|4|5|6|\n|7|8|9|') 
    print('O Numero no qual voce escolher ira ser marcar com um  X')
    while True:

        painel()

        bot = randint(1, 10)
        print(bot)
global bot

mecanicas()


def mecanicas():
   
    layout = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    if player or bot == escolhidos:
        if player:
            print('Opçao ja escolida esconha outro numero')
        if bot:
            bot = randint(1, 10)    
    if player:
        n = player - 1
        layout.append('X'[n])
        return print(f'|{layout[0]}|{layout[1]}|{layout[2]}|\n|{layout[3]}|{layout[4]}|{layout[5]}|\n|{layout[6]}|{layout[7]}|{layout[8]}|')

main()
# 753, 159, 258, 147, 258,369