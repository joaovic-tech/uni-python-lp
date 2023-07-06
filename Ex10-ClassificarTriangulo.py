# Receber três valores representando so lados do triãngulo fornecidos pelo usuário.
# para a verificação nenhum dos lados pode ser maior que a soma dos dois e nenhum pode ser menor ou igual a zero
# Classificar o triângulo seguindo os valores para:
# Equilátero -> 3 lados iguais
# Isósceles -> 2 lados iguais
# Escaleno -> 3 lados diferentes

ladoA = int(input('Digite o primeiro lado do triãngulo: '))
ladoB = int(input('Digite o segundo lado do triãngulo: '))
ladoC = int(input('Digite o terceiro lado do triãngulo: '))

equilatero = (ladoA == ladoB) and (ladoA == ladoC) and (ladoB == ladoC)
isosceles = (ladoA == ladoB) or (ladoB == ladoC) or (ladoA == ladoC)
escaleno = (ladoA != ladoB) and (ladoA != ladoC) and (ladoB != ladoC)
existZero = (ladoA <= 0) or (ladoB <= 0) or (ladoC <= 0)
ladoMaiorQueASoma = (ladoA + ladoB > ladoC) and (ladoA + ladoC > ladoB) and (ladoB +ladoC > ladoA)

if (existZero or not ladoMaiorQueASoma):
    print('Opá! Verifique os lados do triângulo.')
elif (equilatero):
    print('\nÉ um triângulo equilátero!')
elif (isosceles):
    print('\nÉ um triângulo isosceles!')
elif (escaleno):
    print('\nÉ um triângulo escaleno!')
else:
    print('\nNão é um triângulo equilátero, isosceles ou escaleno!')
