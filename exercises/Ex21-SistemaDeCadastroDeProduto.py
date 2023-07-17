products = []
options = '''
---------------(Sistema de compras)---------------
Opções:
    1 - Cadastrar novo produto
    2 - Listar jogos
    3 - Sair
'''

def is_number(value):
    try:
        int(value)
    except ValueError:
        return False
    return True

print(options)
print('Nota: digite "3" para encerrar o programa\n')

while True:
    x = input('\nEscolha a opção que deseja fazer: ')

    if is_number(x):
        x = int(x)
    else:
        print('Desculpe, não entendi!')
        print(options)
        continue

    if x == 1:
        product = input('\nDigite o nome do(a) produto: ')
        productQuantity = int(input('Digite a quantidade do {}: '.format(product)))
        productValue = float(input('Digite o valor unitário do {} sem R$: '.format(product)))
        products.append([product, productQuantity, productValue])
    elif x == 2:
        if len(products) > 0:
            for infoProduct in products:
                print('\n-' * 30)
                print('Nome do produto: {}'.format(infoProduct[0]))
                print('Quantidade: {}'.format(infoProduct[1]))
                print('Valor unitário: R$ {:,.2f}'.format(infoProduct[2]))
                print('Valor total: R$ {:,.2f}'.format(infoProduct[2] * infoProduct[1]))
                print('\n-' * 30)
        else:
            print('Nenhum produto cadastrado')

    elif x == 3:
        print('\nEncerrando programa...')
        break
    else:
        print('Desculpe, não entendi!')
        print(options)
        continue

print(products)
