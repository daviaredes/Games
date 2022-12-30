from PySimpleGUI import *

theme('DarkGrey14')

layout = [
    [Checkbox('X'), Txt('OU'), Checkbox('O')],
    [Button(), Button(), Button()],
    [Button(), Button(), Button()],
    [Button(), Button(), Button()],
    [Button('Jogar')],
]

Jan = FlexForm('', layout=layout, default_button_element_size=(5, 2), auto_size_buttons=False)

Valor= ''
while True:

    button, values = Jan.Read()

    # teste
    if Valor == '':
        print('ola')
    if button == None:
        break
    else:
        Valor += button
        print(Valor)
