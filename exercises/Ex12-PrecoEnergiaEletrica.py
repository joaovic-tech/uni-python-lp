# calcular o preço a pagar pelo fornecimento de energia elétrica.
# Pergunte a quantidade de kWh consumida e o tipo de instalação:
# R -> para residências
# I -> para indústrias
# C -> para comércios

kwh = float(input("Qual a quantidade de kWh consumida: "))
tipo = input('''
Escolha o tipo de instalação:
R -> para Residências
I -> para Indústrias 
C -> para Comércios
''')

preco = None

if (tipo == 'R'):
    if (kwh <= 500):
        preco = 0.40
    else:
        preco = 0.65
elif (tipo == 'C'):
    if (kwh <= 100):
        preco = 0.55
    else:
        preco = 0.60
elif (tipo == 'I'):
    if (kwh <= 5000):
        preco = 0.55
    else:
        preco = 0.60
else:
    print('\nInstalação inválida\nNenhum calculo será realizado!')

if (preco is not None):
    print('\nTotal a pagar: R$ {:,.2f}'.format(kwh * preco))
