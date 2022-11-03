import random
import time
import os



def main():

    rodadas = 0

    print(f'BEM VINDO AO DESCUBRA O NUMERO, TENTE DESCOBRIR QUAL NUMERO ESTOU PENSANDO')
    
    nome = str(input('COMO DESEJA SER CHAMADO: '))

    print(f' {nome} Você  PODE SAIR A QUALQUER MOMENTO BASTA DIGITAR, SAIR \n CASO ACERTE O NUMERO O JOGO IRA FECHAR AUTOMATICAMENTE')

    esc_bot = random.randint(1, 100)

    while True:
        try:
            esc_user = int(input(f'{nome} ESTOU PENSANDO EM UM NUMERO ENTRE 1 e 100 QUAL VOCE ACHA QUE E ? '))
            rodadas += 1
        except ValueError:
            print(f'ATE MAIS {nome}')
            break
        else:
            if esc_user > 100 or esc_user < 1:
                print('NAO ENTEDI, O NUMERO QUE ESTOU EM MENTE ESTA ENTRE 1 E 100 ')
            if esc_user < esc_bot:
                print(f'O NUMERO QUE ESTOU PENSANDO E MAIOR')
                time.sleep(5)
                os.system('cls')
            elif esc_user > esc_bot:
                print(f'O NUMERO QUE ESTOU PENSADNO E MENOR')
                time.sleep(5)
                os.system('cls')
            elif esc_user == esc_bot:
                print(f'PARABENS {nome} VOCE ACERTOU COM {rodadas} TENTATIVAS')
                break
main()
