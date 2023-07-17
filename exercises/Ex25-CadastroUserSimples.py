from datetime import date

users = [{
    "nome": 'João Victor',
    "year": 2004,
    "sex": 'M',
}]

print('Cadastro de usuários')

def display_options():
    print('Enter - Cadastrar')
    print('0 - Encerrar')

def average(users):
    years = 0

    for user in users:
        years += int(user['year'])

    return int(years / len(users))


def women_over_30(users):
    list = []
    current_date = date.today().year

    for user in users:
        calcYear = current_date - user['year']
        if (user['sex'] == 'f' and calcYear > 30):
            list.append(user)

    return list

def get_men_above_average_age(users):
    list = []
    current_date = date.today().year

    for user in users:
        if (user['sex'] == 'm'):
            calcYear = current_date - user['year']
            if (calcYear > average(users)):
                list.append(user)

    return list

while True:
    display_options()
    option = input('\nEscolha o que deseja fazer: ')

    if (option == '0'):
        break

    print('\n------------------Cadastrar------------------')
    name = input('Nome: ')
    year = int(input('Ano do nascimento: '))
    sex = input('Sexo (M ou F): ')

    users.append({
        "nome": name,
        "year": year,
        "sex": sex.lower(),
    })

print('Tatal de usuários cadastrados: {}'.format(len(users)))
print('A média dos usuários são: {}'.format(average(users)))
print('Lista de mulheres com mais de 30 anos: {}'.format(women_over_30(users)))
print('Lista de homens com idade acima da média: {}'.format(get_men_above_average_age(users)))
