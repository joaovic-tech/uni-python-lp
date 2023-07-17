mochila = ['Machado', 'Caneta', 'Caderno', 'Maçã']

print(mochila[0][0]) # M
print(mochila[0][:3]) # Mac

for item in mochila:
    for letra in item:
        print(letra, end='')
    print()

