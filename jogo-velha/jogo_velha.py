from PySimpleGUI import *

theme('DarkGrey14')

layout = [
    [Button(k='1'), Button(k='2'), Button(k='3')],
    [Button(k='4'), Button(k='5'), Button(k='6')],
    [Button(k='7'), Button(k='8'), Button(k='9')],
    [Txt('' * 10)],
    [Button(k='subm')]
]
Windo = FlexForm('Jogo', default_button_element_size=(5, 2),  auto_size_buttons=False, layout=layout)

while True:

    button, values = Windo.Read()

    if button == None:
        break
    if button == 'subm':



'''
    if button == '1':
        print('ansjhewdgegw')

    if button == 'subm':
        popup('FOI')
'''