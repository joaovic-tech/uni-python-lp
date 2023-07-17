# A media entre 23, 19 e 31

numbers = [23, 19, 31]
soma = 0
media = 0
tamanho = numbers.__len__()

for number in numbers:
    soma += number

media = soma / tamanho

print(media)
