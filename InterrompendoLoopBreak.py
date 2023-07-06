# Algoritmo que fica recevendo frases ou palabras digitadas pelo usuário
# E encerra quando esse valor de entrada for "sair"

print('''
    Digite uma mensagem que irei repetir para você!
     Para encerrar digite "sair" e precione Enter!
-------------------------------------------------------
\n''')

text = input('Digite: ')

while (text.lower() != 'sair'):
    print('\nVocê digitou: {}'.format(text))
    text = input('Digite novamente: ')
    if text == 'sair':
        break

print('Encerrando o programa...')

