distancia = int(input('Digite a distância em KM percorrida pelo carro: '))
dias = int(input('Digite quantos dias você andou no carro: '))

print("____________________________________________")

print('Custo em diária: R$ 60.00')
print('Custo em km: R$ 0.15\n')

preco_diaria = 60 * dias
preco_distancia = 0.15 * distancia
custo_total = preco_distancia + preco_diaria

print('Você percorreu uma distância de {} Km em {} dias.\n'.format(distancia, dias))

print('Custo por quilometragem: R$ {:,.2f}'.format(preco_distancia))
print('Custo por diária: R$ {:,.2f}'.format(preco_diaria))
print('Custo Total: R$ {:,.2f}'.format(custo_total))
