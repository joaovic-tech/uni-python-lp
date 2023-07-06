# O somatório dos 5 primeros números

# o professor fez -> 1 + 2 + 3 + 4 + 5


# Eu entendi isso:
def somarotio(value):
    numbers = str(value)
    soma = 0

    for index in range(int(numbers)):
        soma += int(numbers[index])

        if index == 4:
            return soma

somar = somarotio(989898946354135869)
print(somar)