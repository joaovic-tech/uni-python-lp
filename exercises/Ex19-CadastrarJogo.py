games = []
file_path = "games.txt"
options = '''
---------------(Cadastro de jogos)---------------
Opções:
    1 - Cadastrar novo jogo
    2 - Listar jogos
    3 - Sair
'''

def is_number(value):
    try:
        int(value)
    except ValueError:
        return False
    return True

def listar_jogos():
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            if content:
                print("\nJogos cadastrados:")
                print(content)
            else:
                print('Nenhum jogo cadastrado!')
    except FileNotFoundError:
        print('Arquivo de jogos não encontrado!')

print(options)

while True:
    x = input('\nEscolha a opção que deseja fazer: ')

    if is_number(x):
        x = int(x)
    else:
        print('Desculpe, não entendi!')
        print(options)
        continue

    if x == 1:
        game = input('\nDigite o nome do jogo: ')
        device = input('Digite o nome do videogame em que {} é jogado: '.format(game))
        games.append({
            'game': game,
            'device': device
        })

        with open(file_path, 'a') as file:
            file.write('''
Jogo: {}\nDispositivo: {}
--------------------------------------
            '''.format(game, device))
    elif x == 2:
        listar_jogos()
    elif x == 3:
        print('Encerrando programa...')
        break
    else:
        print('Desculpe, não entendi!')
        print(options)
        continue
