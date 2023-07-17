valor  = float(input('Digite o valor do produto: '))
percentual  = float(input('Digite o percentual de desconto (0%-100%): '))

desconto = valor * percentual / 100
valor_final = valor - desconto

print('\n-------------------------------------------------------')

print('Valor do produto é R$ {:,.2f} e seu desconto de {}%'.format(valor, int(percentual)))

print('-------------------------------------------------------')

print('Valores finais:\n')

print('Valor do desconto: R$ {:,.2f}'.format(desconto))
print('Valor do produto: R$ {:,.2f}'.format(valor_final))
