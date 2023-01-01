from PySimpleGUI import *

theme('DarkGrey14')


def opçao():
    layout = [
        [Button('X'), Text('OU'), Button('O')]
    ]

    return Window('Opçao', layout=layout, default_button_element_size=(5, 2), auto_size_buttons=False) 


Window_popup = opçao()


layout = [
    [Button(), Button(), Button()],
    [Button(), Button(), Button()],
    [Button(), Button(), Button()],
    [Submit('Jogar', key='continuar')],
]


Jan = FlexForm('', layout=layout, default_button_element_size=(5, 2), auto_size_buttons=False)

Valor = ''

while True:

    button, values = Jan.Read()
           
    if Valor == 'continuar':
        Window_popup()

    if button == None:
        break
    else:
        Valor += button
        
