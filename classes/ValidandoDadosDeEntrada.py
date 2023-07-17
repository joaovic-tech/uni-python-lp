# Algoritmo que recebe um valor do tipo inteiro via teclado
# No entanto,o programa só deve aceitar, obrigatoriamente, valores inteiros e positivos
# Qualquer valor negativo, ou igual a zero, deve ser rejeitado pelo programa e um novo deve ser solicitado

value = input('Digite um valor inteiro: ')

while (not value.isnumeric() or not value):
    value = input('Ops! "{}" não é um valor inteiro. Tente novamente: '.format(value))

print('{} é um valor inteiro!'.format(value))
