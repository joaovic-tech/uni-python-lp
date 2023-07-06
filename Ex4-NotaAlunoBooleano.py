# Saber se o aluno passou nas 3 matérias

nome_aluno = input('Digite o nome do aluno: ')
nota_m1 = float(input('Digite a nota da 1º matéria: '))
nota_m2 = float(input('Digite a nota da 2º matéria: '))
nota_m3 = float(input('Digite a nota da 3º matéria: '))

condicao = nota_m1 >= 7 and nota_m2 >= 7 and nota_m3 >= 7

if (condicao):
    print('\nO aluno {} passou!'.format(nome_aluno))
else:
    print('\nO aluno {} reprovou!'.format(nome_aluno))
