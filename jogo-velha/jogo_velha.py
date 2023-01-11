from PySimpleGUI import *
from random import randint

theme('DarkGrey14')

layout = [
    [ReadFormButton('O', k='1'), ReadFormButton('', k='2'), ReadFormButton('', k='3')],
    [ReadFormButton('', k='4'), ReadFormButton('', k='5'), ReadFormButton('', k='6')],
    [ReadFormButton('', k='7'), ReadFormButton('', k='8'), ReadFormButton('', k='9')],
    [Txt('' * 10)],
    [Button(k='subm')]
]
Windo = FlexForm('Jogo', default_button_element_size=(5, 2),  auto_size_buttons=False, layout=layout)

rodadas = 0

while True:
    rodadas += 1

    button, values = Windo.Read()

    bot = randint(1, 9)

    if button == None:
        break

    elif button == 'subm':
        popup('O Adversario fez a sua jagada')
        rodadas = 0
        if bot:
            leitor = str(int(float(bot)))
            print(leitor)
            Windo.find_element(leitor).update('O')
            
    if button:
        if rodadas > 1:
            popup('nao pode mais jogar aprete no subit')
        else:
            Windo.find_element(button).update('X')
