import random


def display_options():
    print("1 - Pedra")
    print("2 - Papel")
    print("3 - Tesoura")
    print("0 - Sair")

while True:
    display_options()
    player = int(input('Digite sua escolha: '))
    computer = random.randint(1, 3)
    wins = 0
    losses = 0
    ties = 0

    if (player < 0 or player > 3):
        print("Opção inválida. Tente novamente.")
        continue

    if (player == 0):
        break
    elif (player == computer):
        print('Empate!')
        ties += 1
        continue
    elif ((player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2)):
        print('Você ganhou!')
        wins += 1
        continue
    else:
        print('Você perdeu!')
        losses += 1

print("\nEstatísticas:")
print('Vitórias: {}'.format(wins))
print('Derrotas: {}'.format(losses))
print('Empate: {}'.format(ties))
