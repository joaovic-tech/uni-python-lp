print('''
==========================================================================================
             Seja bem vindo(a) ao app do desconto do João Victor Carvalho Alves             
==========================================================================================
''')

# tabela de desconto
print("Tabela de Descontos:")
print("-----------------------------------")
print("Quantidade              |  Desconto")
print("-----------------------------------")
print(" Menor que 200          |     0%   ")
print(" 200 até 999            |     5%   ")
print(" 1000 até 1999          |    10%   ")
print(" Maior ou igual à 2000  |    15%   ")
print("-----------------------------------")

unit_price = float(input("Entre com valor unitário do produto em R$: "))
quantity = int(input("Entre com a quantidade do produto: "))

# Cálculo do valor total sem desconto
total_without_discount = unit_price * quantity

# Cálculo do desconto
if quantity < 200:
    discount = 0
elif quantity < 1000:
    discount = 5
elif quantity < 2000:
    discount = 10
else:
    discount = 15

# Cálculo do valor total com desconto
discount_value = total_without_discount * discount / 100
total_with_discount = total_without_discount - discount_value

# Exibição dos resultados
print("-----------------------------------")
print("Valor total sem desconto: R$ {:,.2f}".format(total_without_discount))
print("Valor do desconto: R$ {:,.2f}".format(discount_value))
print("Valor total com desconto: R$ {:,.2f}".format(total_with_discount))
