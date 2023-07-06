nome = 'João'

print(nome)

def mudarNome():
    global nome
    nome = 'mudou'

mudarNome()
print(nome)
