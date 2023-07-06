# Verificar se o nome digitado é João
# Se for True mostrar o nome
# Se não perguntará a idade e verificar se é 18
# Caso seja menor que 18 -> De menor
# Caso seja maior que 100 -> Esta pessoa possivelmente não existe

nome = input("Nome: ")
idade = int(input('Qual é a idade dessa pessoa? '))

if (nome == 'João'):
    print('Olá {}!'.format(nome))
elif (idade < 18):
    print('Voê não é o {}! E é de menor!'.format(nome))
elif (idade > 100):
    print('Esta pessoa possivelmente não existe!')
