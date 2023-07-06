# Voltando ao inicio do laço usando continue

loginUser = 'joaovic'
passwordUser = '123'

while True:
    login = input('Login: ')
    if (login != loginUser):
        continue
    password = input('Senha: ')
    if (password == passwordUser):
        break

print('''\n
==================Acesso autorizado!====================

        Seja bem vindo João!
''')

