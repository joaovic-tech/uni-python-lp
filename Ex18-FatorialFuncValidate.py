def validateNumber(num):
    try:
        num = int(num)
        if num >= 0:
            return num
        else:
            print('Erro! O número deve ser positivo.')
            return False
    except ValueError:
        print('Erro! {} não é um número válido.'.format(num))
        return False


def calculate_factorial(num):
    """
    Calcula a fatorial
    :param num:
    :return:
    """

    num = validateNumber(num)

    if (num == 0):
        return 1

    if (not num):
        return False

    for count in range(1, num):
        num *= count

    return num

x = input('Digite um valor para calcular a fatorial: ')
print('{}!: {}'.format(x, calculate_factorial(x)))
