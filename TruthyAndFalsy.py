# valores truthy e falsy

name = ''

while(not name):
    name = input('Digite seu nome:')

value = int(input('Digite um número qualquer:'))

if (value):
    print('Você digitou um valor diferente de zero.')
else:
    print('Você digitou zero.')