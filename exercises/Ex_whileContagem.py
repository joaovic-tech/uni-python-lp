# Escreva um algoritmo que imprima na tela somente valores dentro de um intervalo
# especificado pelo usuário e que sejam números pares

inicial = int(input('Qual valor seja iniciar a contagem: '))
final = int(input('Qual valor seja encerrar a contagem: '))
x = inicial

while (x <= final):
    if (x % 2 == 0):
        print(x)
    x += 1
