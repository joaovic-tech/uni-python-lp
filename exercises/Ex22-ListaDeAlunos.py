# Algoritmo que
# Encontra quandos alunos tiraram nota 7
# Altera a última nota para 4
# Encontra o mair número
# Faz uma organização
# A média das notas

notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]

print('\nNotas iniciais: {}\n'.format(notas))

qtd_notas7 = notas.count(7)
print('{} alunos com nota 7'.format(qtd_notas7))

notas[-1] = 4
print('Valor alterado notas: {}'.format(notas))

mairNota = max(notas)
print('A maior nota é: {}'.format(mairNota))

notas.sort(key=int)
print('Notas ordenadas crescente: {}'.format(notas))

media = sum(notas) / len(notas)
print('Media: {}'.format(media))
