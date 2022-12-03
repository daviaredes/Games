from random import choice

contador_vitoria = 0
contador_derrota = 0
contador_empate = 0

def main():

    print('Bem vindo ao Jokenpo se divirtam-se\nAs opçoes são \nPedra 🌑\nPapel 📜\nTesoura ✂️')

    bot = choice(['papel', 'pedra', 'tesoura'])


    def contador():
        cont = str(input('Quer continuar jogando, Diguite sim para continuar e nao para sair:').lower().strip()[0])
        if cont == 's':
            main()
        elif cont == 'n':
            rodadas = contador_vitoria + contador_derrota + contador_empate
            print(f'Obrigado por jogar em nossa maquina Voce jogou {rodadas} rodadas Ganhou em {contador_vitoria} delas e Perdeu em {contador_derrota} delas')


    while True:
        
        player = str(input('Opçao escolha: ').lower().strip())
              
        if player == bot:
            print('Empate os doi ganharam:')
            contador_empate + 1
            contador()

        elif player == "pedra" and bot == "tesoura" or player == "papel" and bot == "pedra" or player == "tesoura" and bot == "papel":
            print('Parabens voce ganhou')
            contador_vitoria + 1
            contador()

        elif bot == "pedra" and player == "tesoura" or bot == "papel" and player == "pedra, " or bot == "tesoura" and player == "papel":
            print('Voce perdeu ')
            contador_derrota + 1
            contador()

        elif player != "papel" or "pedra" or "tesoura":
            print('Erro 404')
            break

main()
