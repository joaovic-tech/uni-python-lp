print('''
-*-*-*-*-*-*-*-*-Valores do ingresso-*-*-*-*-*-*-*-*-

Idade -> Menores de 3 anos valor =  Gratuito
Idade -> De 3 e 12 anos valor    =  R$ 15
Idade -> Maior que 12 anos valor =  R$ 30
''')

cinemaOpen = True
numberOfPeople = 0
revenue = 0
totalAge = 0

while cinemaOpen:
    numberOfPeople += 1
    age = input('Idade da {}ª pessoa: '.format(numberOfPeople))

    if age.lower() == 'sair':
        numberOfPeople -= 1
        break

    age = int(age)
    totalAge += age

    if 3 <= age <= 12:
        revenue += 15
    else:
        revenue += 30

averageAge = totalAge / numberOfPeople if numberOfPeople > 0 else 0

print('''
Total de pessoas: {}
Dinheiro arrecadado: R$ {}
Média de idade: {:.0f}
'''.format(numberOfPeople, revenue, averageAge))
