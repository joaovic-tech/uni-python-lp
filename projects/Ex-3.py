def dog_weight():
    while True:
        try:
            weight = float(input(f"\nDigite o peso do cão: "))
            if weight < 3:
                return 40
            elif 3 <= weight < 10:
                return 50
            elif 10 <= weight < 30:
                return 60
            elif 30 <= weight < 50:
                return 70
            elif weight >= 50:
                print("Peso acima de 50kg. Digite um peso válido.")
        except ValueError:
            print("Valor não numérico. Digite um peso válido.")


def display_extra():
    print('\nEsses são os serviços adicionais:')
    print('1 - Cortas unhas')
    print('2 - Escovar dentes')
    print('3 - Limpar orelhas')
    print('0 - Nenhum')

    return input('Qual sua escolha? ')


def display_coat_type():
    print(f'\nQual o tipo de pelo do cão')
    print('c - Curto')
    print('m - Médio')
    print('l - Longo')

    return input('Tipo: ')

def dog_coat_type():
    while True:
        coat = display_coat_type()
        if coat == 'c':
            return 1
        elif coat == 'm':
            return 1.5
        elif coat == 'l':
            return 2
        else:
            print("Opção inválida. Digite uma opção válida.")

def dog_extra_services():
    extras = 0
    while True:
        additional = display_extra()
        if additional == '1':
            extras += 10
        elif additional == '2':
            extras += 12
        elif additional == '3':
            extras += 15
        elif additional == '0':
            return extras
        else:
            print("Opção inválida. Digite uma opção válida.")

def calculate_total(base, multiplier, extra):
    total = base * multiplier + extra
    return total

# Programa principal
print('-----------------------( Seja bem-vindo(a) ao sistema de cobrança do João Victor Carvalho Alves )-----------------------')

base_price = dog_weight()
multiplier = dog_coat_type()
extra = dog_extra_services()

total_amount = calculate_total(base_price, multiplier, extra)
print(f"\nValor total a pagar: R$ {total_amount:.2f} (Peso: {base_price} * Pelo {multiplier} + adicional(is): {extra}).")
