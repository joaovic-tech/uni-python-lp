def somarNumeros(*numbers):
    res = 0
    for number in numbers:
        res += number

    return res

print('Resultado: {}'.format(somarNumeros(54, 656, 6,3, 2)))