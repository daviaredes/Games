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


Window1, Window2 = layout_main(), None

while True:
    window, event, values  = read_all_windows()

    if window == Window1 and event == WIN_CLOSED:
        break

    if window == Window1 and event == '1 player':
        Window2 == player_vs_bot()
        Window1.hide()
