from PySimpleGUI import *
from random import randint

theme('DarkGrey14')

layout = [
    [Txt('' * 10)],
    [Button('', k='1'), Button('', k='2'), Button('', k='3')],
    [Button('', k='4'), Button('', k='5'), Button('', k='6')],
    [Button('', k='7'), Button('', k='8'), Button('', k='9')],
    [Txt('' * 10)],
    [Button('jogar', k='subm')]
]
Windo = FlexForm('Jogo', default_button_element_size=(5, 2),  auto_size_buttons=False, layout=layout)

# ideia 
historico_player = [] 
historico_bot = []
# ^^^^^^^^^^^^
rodadas = 0

while True:
    rodadas += 1

    button, values = Windo.Read()


    if button == None:
        break

    elif button == 'subm':
        bot = randint(1, 9)
        # historico_bot.append(bot)
        rodadas = 0
        if bot:
            leitor = str(int(float(bot)))
            print(leitor)
            Windo.find_element(leitor).update('O')
    
    if button:
        if rodadas > 1:
            popup('nao pode mais jogar aperte em jogar ')
        else:
            # historico_player.append(button)
            Windo.find_element(button).update('X')
            Windo.find_element('subm').update('jogar')
