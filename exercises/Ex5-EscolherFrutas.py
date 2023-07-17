# Escolher 3 tipos de frutas: 1 maçã, 2 laranja, 3 banana

print('----------------------------------')
print('              Frutas')
print('1 - maçã')
print('2 - laranja')
print('3 - banana')
print('----------------------------------')

fruta_escolhida = int(input('Qual fruta deseja? '))

preco_maca = 2.30
preco_laranja = 3.60
preco_banana = 1.85

if fruta_escolhida == 1:
    qtd_frutas = int(input('Quantas maçãs deseja comprar: '))
    preco_final = qtd_frutas * preco_maca
    print('\nVocê comprou {} maçã(s)!'.format(qtd_frutas))
    print('Valor total a pagar R$ {:,.2f}'.format(preco_final))
elif fruta_escolhida == 2:
    qtd_frutas = int(input('Quantas laranjas deseja comprar: '))
    preco_final = qtd_frutas * preco_laranja
    print('\nVocê comprou {} laranja(s)!'.format(qtd_frutas))
    print('Valor total a pagar R$ {:,.2f}'.format(preco_final))
elif fruta_escolhida == 3:
    qtd_frutas = int(input('Quantas bananas deseja comprar: '))
    preco_final = qtd_frutas * preco_banana
    print('\nVocê comprou {} banana(s)!'.format(qtd_frutas))
    print('Valor total a pagar R$ {:,.2f}'.format(preco_final))
else:
    print('Nenhuma fruta escolhida!')
