# calculadora que só termina quando o usuário encerra

while True:
    x = int(input('Digite o primeiro número: '))
    y = int(input('Digite o segundo número: '))
    result = None

    print('''
Operadores:
    (+) - Adição
    (-) - Subtração
    (*) - Multiplicação
    (/) - Divisão
    ''')

    op = input('\nEscolha o operador através do seu símbolo: ')

    if op == '+':
        result = x + y
        continue
    elif op == '-':
        result = x - y
        continue
    elif op == '*':
        result = x * y
        continue
    elif op == '/':
        result = x / y
        continue
    elif op == 's':
        break
    else:
        print('\nNenhuma operação válida foi escolhida!\n')

    if result is not None:
        print('\nResultado: {}\n'.format(result))

print('Encerrando o programa...')
