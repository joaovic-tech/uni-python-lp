# Algoritmo que calcula a média dos números pares de 1 até 100 (1 e 100 inclusos). - USANDO O LAÇO FOR

soma = 0
qtd = 0

for i in range(1,101):
    if (i % 2 == 0 or i == 1):
        soma += i
        qtd += 1

media = soma / qtd
print('A média dos pares de 1 até 100 é: {}'.format(media))
