# crie uma rotina que recebe um palavra e mostre ela dentro de uma caixa de texto
# use caracteres especiais como: |+--+|
# essa caixa de texto tem que ser adaptável de acordo com o tamanho da palavra
# faça uma validação

def realcer(palavra: str):
    if (palavra):
        print('+' + '-' * len(palavra) + '+')
        print('|' + palavra + '|')
        print('+' + '-' * len(palavra) + '+')

realcer('Olá, mundo!')


# +-----------+
# |Olá, mundo!|
# +-----------+
