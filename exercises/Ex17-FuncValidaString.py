# Escreva uma função que irar receber uma pergunta e irar retorna True caso
# o tamanho do valor dessa pergunta esteja no tamanho min e max que também vem como parâmetro
# e retirn False caso contrário

def valida_string(quest: str, min: int, max: int):
    newQuest = input(quest)
    lengthQuest = len(newQuest)

    while ((lengthQuest < min) or (lengthQuest > max)):
        newQuest = input(quest)
        lengthQuest = len(newQuest)
    return newQuest

quest = valida_string('Digite uma string: ', 10, 30)
print('Você digitou a string: {}. \nDado válido. Encerrando o programa...'.format(quest))
