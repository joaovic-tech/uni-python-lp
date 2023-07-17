print('''
==========================================================================================
               Seja bem-vindo(a) à sorveteria do João Victor Carvalho Alves               
==========================================================================================
''')
print('-' * 42 + 'Cardápio' + '-' * 42)
print('| Nº de bolas | Sabor Tradicional (tr) | Sabor Premium (pr) | Sabor Especial (es)  |')
print('|      1      |        R$ 6,00         |      R$ 7,00       |       R$ 8,00        |')
print('|      2      |        R$ 10,00        |      R$ 12,00      |       R$ 14,00       |')
print('|      3      |        R$ 14,00        |      R$ 17,00      |       R$ 20,00       |')
print('-' * 92)

total_amount = 0

def criar_pedido(flavor, quantity):
    flavors = {
        'tr': ['TRADICIONAL', [6, 10, 14]],
        'pr': ['PREMIUM', [7, 12, 17]],
        'es': ['ESPECIAL', [8, 14, 20]],
    }

    price = flavors[flavor][1][quantity - 1]
    if quantity == 1:
        print(f"Você pediu 1 bola de sorvete no sabor {flavors[flavor][0]}: R$ {price:.2f}")
    else:
        print(f"Você pediu {quantity} bolas de sorvete no sabor {flavors[flavor][0]}: R$ {price:.2f}")

    return price

while True:
    # Pergunte pelo sabor
    flavor = input("\nDigite o sabor (tr/pr/es): ")

    # Verificar se a resposta do sabor foi correta
    if flavor not in ['tr', 'pr', 'es']:
        print('Sabor inválido. Tente novamente!')
        continue

    # Pergunte pelo número de quantidade de bolas
    quantity = input("Digite o número de bolas (1/2/3): ")

    # Verificar se a resposta da quantidade foi correta
    if quantity not in ['1', '2', '3']:
        print('Número de bolas de sorvete inválido. Tente novamente!')
        continue

    quantity = int(quantity)

    total_amount += criar_pedido(flavor, quantity)

    # Perguntar se o cliente deseja fazer outro pedido
    order_again = input("\nDeseja fazer outro pedido? (S/N): ")

    # Verificar se o cliente deseja fazer outro pedido
    if order_again.lower() != "s":
        break

# Imprimir o valor total
print(f"\nValor total: R$ {total_amount:.2f}")
