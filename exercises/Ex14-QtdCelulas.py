# algoritmo que irar ler um valor e monstrar quantas celulás irar possuir até chegara esse valor
# Exemplo: valor = 250: duas notas de R$ 100 e um de R$ 50

value = int(input('Digite o valor em R$: '))

while True:
    if (value >= 100):
        moneyBill100 = value // 100
        value -= moneyBill100 * 100
        print('Cédulas de 100: {}'.format(moneyBill100))
        if (not value):
            break
    if (value >= 50):
        moneyBill50 = value // 50
        value -= moneyBill50 * 50
        print('Cédulas de 50: {}'.format(moneyBill50))
        if (not value):
            break
    if (value >= 20):
        moneyBill20 = value // 20
        value -= moneyBill20 * 20
        print('Cédulas de 20: {}'.format(moneyBill20))
        if (not value):
            break
    if (value >= 10):
        moneyBill10 = value // 10
        value -= moneyBill10 * 10
        print('Cédulas de 10: {}'.format(moneyBill10))
        if (not value):
            break
    if (value >= 5):
        moneyBill5 = value // 5
        value -= moneyBill5 * 5
        print('Cédulas de 5: {}'.format(moneyBill5))
        if (not value):
            break
    if (value >= 1):
        moneyBill1 = value // 1
        value -= moneyBill1 * 1
        print('Cédulas de 1: {}'.format(moneyBill1))
        if (not value):
            break
