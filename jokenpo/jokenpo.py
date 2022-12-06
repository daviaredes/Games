from random import choice

vitoria = 0
derrota = 0
empate = 0

def contador(vitoria, derrota, empate):
    cont = str(input('Quer continuar jogando, Diguite sim para continuar e nao para sair:').lower().strip()[0])

    if cont == 's':
        main(vitoria, derrota, empate)  
    elif cont == 'n':
        rodadas = (vitoria + derrota) + empate
        print(f'Obrigado por jogar em nossa maquina Voce jogou {rodadas} rodadas Ganhou em {vitoria} delas Empatou em {empate} delas e Perdeu em {derrota} delas')
    elif contador(vitoria, derrota, empate) == 's' or 'n':
        pass
    else:
        contador(vitoria, derrota, empate)


def main(vitoria, derrota, empate):

    print('Bem vindo ao Jokenpo se divirtam-se\nAs opçoes são \nPedra 🌑\nPapel 📜\nTesoura ✂️')

    bot = choice(['papel', 'pedra', 'tesoura'])

    while True:
        
        player = str(input('Opçao escolha: ').lower().strip())
        if player == "papel" or "pedra" or "tesoura":
            pass

        if player == bot:
            print('Empate os dois ganharam:')
            empate += 1
            contador(vitoria, derrota, empate)

        elif player == "pedra" and bot == "tesoura" or player == "papel" and bot == "pedra" or player == "tesoura" and bot == "papel":
            print('Parabens voce ganhou')
            vitoria += 1
            contador(vitoria, derrota, empate)

        elif bot == "pedra" and player == "tesoura" or bot == "papel" and player == "pedra" or bot == "tesoura" and player == "papel":
            print('Voce perdeu ')
            derrota += 1
            contador(vitoria, derrota, empate)
        break

main(vitoria, derrota, empate)
