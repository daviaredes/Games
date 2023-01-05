from PySimpleGUI import *
from random import randint

theme('DarkGrey14')

layout = [
    [ReadFormButton('', k='1'), ReadFormButton('', k='2'), ReadFormButton('', k='3')],
    [ReadFormButton('', k='4'), ReadFormButton('', k='5'), ReadFormButton('', k='6')],
    [ReadFormButton('', k='7'), ReadFormButton('', k='8'), ReadFormButton('', k='9')],
    [Txt('' * 10)],
    [Button(k='subm')]
]
Windo = FlexForm('Jogo', default_button_element_size=(5, 2),  auto_size_buttons=False, layout=layout)

bot = random.randint(1, 9)
   
while True:
    button, values = Windo.Read()


    if button == None:
        break

    if button == 'subm':
        popup('O Adversario fez a sua jagada')

#    if bot:
#        Windo.find_element(bot).update('O'),  Em teste

    if button:
        Windo.find_element(button).update('X')
