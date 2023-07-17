# List ou Lista tem oum valor dinâmico ou seja pode ser alterado

peoples = ['João', 'Renata', 'txutxucão', 'Thomas']

print(peoples) # ['João', 'Renata', 'txutxucão', 'Thomas']
print(peoples[0]) # João
print(peoples[:2]) # ['João', 'Renata']
print(peoples[1:3]) # ['Renata', 'txutxucão']
print(peoples[-2]) # txutxucão

# Alterar os dados da list

peoples[2] = 'Livia'
print(peoples) # ['João', 'Renata', 'Livia', 'Thomas']

# Adicionando valor
peoples.append('Gabriel')
print(peoples) # ['João', 'Renata', 'Livia', 'Thomas', 'Gabriel']

# Inserir em um index específico sem apagar nada
peoples.insert(1, 'José') # ['João', 'José', 'Renata', 'Livia', 'Thomas', 'Gabriel']
print(peoples)

# Deletando/Removendo
del peoples[5]
peoples.remove('Thomas')
print(peoples) # ['João', 'José', 'Renata', 'Livia']
