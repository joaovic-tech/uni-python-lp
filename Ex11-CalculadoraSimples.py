x = float(input("Digite o primeiro número: "))
y = float(input("Digite o segundo número: "))

print('''
Operadores:
    1 - Adição
    2 - Subtração
    3 - Multiplicação
    4 - Divisão
''')
operator = int(input('Escolha o operador através da sua numeração: '))

result = None

if operator == 1:
    result = x + y
elif operator == 2:
    result = x - y
elif operator == 3:
    result = x * y
elif operator == 4:
    result = x / y
else:
    print('Nenhuma operação válida foi escolhida!')

if result is not None:
    print('Resultado: {}'.format(result))
