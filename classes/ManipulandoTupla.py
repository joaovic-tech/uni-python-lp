# tuple ou tupla tem o valor imutavél ou seja nunca será alterada

mochila = ('Machado', 'Camisa', 'Baicon', 'Abacate')

print(mochila[0]) # Machado
print(mochila[0:2]) # ('Machado', 'Camisa')
print(mochila[2:]) # ('Baicon', 'Abacate')
print(mochila[-1]) # Abacate

for item in mochila:
    print('Na minha mochila tem: {}'.format(item))

upgrade = ('Queijo', 'Canivete')

nova_mochila = mochila + upgrade

print(nova_mochila)
