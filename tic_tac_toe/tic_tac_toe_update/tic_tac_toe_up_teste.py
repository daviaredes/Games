import unittest
from io import StringIO
from unittest.mock import patch
def formataçao_tabela(tabuleiro):
    for linha in tabuleiro:
        print('|' + '|'.join(linha) + '|')

def jogada_bot(tabuleiro):
    from random import randint
    bot_random = randint(1, 9)
    
    linha = (bot_random - 1) // 3 
    coluna = (bot_random - 1) % 3 

    if tabuleiro[linha][coluna] == ' ':
        tabuleiro[linha][coluna] = 'O' 
        print('Seu adversario jogo na {} casa'.format(bot_random))
    else:
        return jogada_bot(tabuleiro)
    
def jogada_player(tabuleiro):
    try:
        posiçao = int(input('Em qual a posiçao no qual voce ira jogar : ')) 
        if posiçao > 9 or posiçao <= 0:
            print('So e permitido de 1 a 9:')
            return jogada_player(tabuleiro)
        else:
            linha = (posiçao - 1) // 3
            coluna = (posiçao - 1) % 3

            if tabuleiro[linha][coluna] == ' ':
                tabuleiro[linha][coluna] = 'X'  
            else:
                print('Aqui ja foi jogado ')
                return jogada_player(tabuleiro)
                
    except ValueError:
        print('So e permitido de 1 a 9:')
        return jogada_player(tabuleiro)

def verificar_ganhador(tabuleiro):
  
    for linha in tabuleiro:
        if linha[0] == linha[1] == linha[2] and linha[0] != ' ':
            return linha[0]
 
    for coluna in range(3):
        if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] and tabuleiro[0][coluna] != ' ':
            return tabuleiro[0][coluna]

    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[0][0] != ' ':
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] and tabuleiro[0][2] != ' ':
        return tabuleiro[0][2]

    return None

def main():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]

    print('BEM-VINDO ao JOGA A VELHA\nvocê sera o X')
    formataçao_tabela(tabuleiro)

    while True:
        jogada_player(tabuleiro)
        jogada_bot(tabuleiro)
        formataçao_tabela(tabuleiro)
      
        ganhador = verificar_ganhador(tabuleiro)
        if ganhador:
            print(f"O jogador {ganhador} ganhou!")
            break
 

main()

class TesteJogoDaVelha(unittest.TestCase):

    def teste_verificar_ganhador_linha(self):
        tabuleiro = [
            ['X', 'X', 'X'],
            [' ', 'O', ' '],
            [' ', ' ', 'O']
        ]
        self.assertEqual(verificar_ganhador(tabuleiro), 'X')

    def teste_verificar_ganhador_coluna(self):
        tabuleiro = [
            ['X', ' ', 'O'],
            ['X', 'O', ' '],
            ['X', ' ', ' ']
        ]
        self.assertEqual(verificar_ganhador(tabuleiro), 'X')

    def teste_verificar_ganhador_diagonal_principal(self):
        tabuleiro = [
            ['X', ' ', ' '],
            [' ', 'X', 'O'],
            ['O', ' ', 'X']
        ]
        self.assertEqual(verificar_ganhador(tabuleiro), 'X')

    def teste_verificar_ganhador_diagonal_secundaria(self):
        tabuleiro = [
            [' ', ' ', 'O'],
            [' ', 'O', 'X'],
            ['O', 'X', ' ']
        ]
        self.assertEqual(verificar_ganhador(tabuleiro), 'O')

    def teste_verificar_ganhador_nenhum(self):
        tabuleiro = [
            ['X', 'O', 'X'],
            ['X', 'O', 'O'],
            ['O', 'X', 'X']
        ]
        self.assertIsNone(verificar_ganhador(tabuleiro))

    @patch('builtins.input', side_effect=['1'])  # Simula a entrada do usuário como '1'
    def teste_jogada_valida(self, mock_input):
        tabuleiro = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        jogada_player(tabuleiro)
        self.assertEqual(tabuleiro[0][0], 'X')

    @patch('builtins.input', side_effect=['10', '1'])  # Simula entradas inválidas e depois uma válida
    def teste_jogada_invalida_e_valida(self, mock_input):
        tabuleiro = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        jogada_player(tabuleiro)
        self.assertEqual(tabuleiro[0][0], 'X')

    @patch('builtins.input', side_effect=['a', '1'])  # Simula entrada inválida (texto) e depois uma válida
    def teste_jogada_entrada_invalida(self, mock_input):
        tabuleiro = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        jogada_player(tabuleiro)
        self.assertEqual(tabuleiro[0][0], 'X')

if __name__ == '__main__':
    unittest.main()