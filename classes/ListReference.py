x = [5, 7, 9, 11]
y = x # Aqui o valor ele não é copiado e sim apontando pelo mesmo local na memória

print('x: ', x) # x: [5, 7, 9, 11]

print('y: ', y) # y: [5, 7, 9, 11]

y[0] = 2
print('x: ', x) # x: [5, 7, 9, 11]
print('y: ', y) # y: [2, 7, 9, 11]

# Para copiar uma lista para outra variavel, faça assim:

numbers = [54, 65, 22, 10, 2]
numbers2 = numbers[:]

numbers[0] = 2

print('Variavel numbers: {}'.format(numbers)) # Variavel numbers: [2, 65, 22, 10, 2]
print('Copia da variavel numbers2: {}'.format(numbers2)) #Copia da variavel numbers2: [54, 65, 22, 10, 2]
