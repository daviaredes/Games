from PySimpleGUI import *

def layout_main():
    theme('DarkGrey14')
    layout = [
        [Txt('' * 10)],
        [Txt('', size=(4, 0)), Text('  BEM VINDO')],
        [Txt('', size=(7, 0)), Text(' AO')],
        [Txt('', size=(3, 0)), Text('JOGO DA VELHA')],
        [Txt('' * 10)],
        [Text('ESCOLHA O MODO DE JOGO')],
        [Txt('', size=(3, 0)), Button('1 player'), Button('2 player')],
        [Txt('' * 10)]
    ]
    return Window('INiCIO', layout=layout, font=('italic'), finalize=True, resizable=True)


def player_vs_bot():
    theme('DarkGrey14')
    layout = [
        [Txt('' * 10)],
        [Button('', k='1'), Button('', k='2'), Button('', k='3')], 
        [Button('', k='4'), Button('', k='5'), Button('', k='6')],
        [Button('', k='7'), Button('', k='8'), Button('', k='9')], 
        [Txt('' * 10)]
    ]
    return Window('Jogo', layout=layout, default_button_element_size=(10, 3),  auto_size_buttons=False, finalize=True, resizable=True)


def player_vs_player(): # test
    theme('DarkGrey14')
    layout = [
        [Txt('' * 10)],
        [Button('1', k='1'), Button('4', k='2'), Button('7', k='3')], 
        [Button('2', k='4'), Button('5', k='5'), Button('8', k='6')],
        [Button('3', k='7'), Button('6', k='8'), Button('9', k='9')], 
        [Txt('' * 10)]
    ]
    return Window('Jogo2', layout=layout, default_button_element_size=(10, 3),  auto_size_buttons=False, finalize=True, resizable=True)


Window1, Window2, Window3 = layout_main(), None, None

while True:
    window, event, values  = read_all_windows()

    if event == WIN_CLOSED or event == 'Exit':
        break

    if window == Window1 and event == '1 player':
        Window2 == player_vs_bot()
        Window1.hide()
    elif window == Window1 and event == '2 player':
        Window3 == player_vs_player()
        Window1.hide()
    