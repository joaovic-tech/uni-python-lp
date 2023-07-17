game = {
    'name': 'Super Mario',
    'developer': 'Nintendo',
    'age': 1990
}

print(game) # {'name': 'Super Mario', 'developer': 'Nintendo', 'age': 1990}
print(game['name']) # Super Mario

print(game.values()) # dict_values(['Super Mario', 'Nintendo', 1990])
for i in game.values():
    print(i)

print(game.keys()) # dict_keys(['name', 'developer', 'age'])
for i in game.keys():
    print(i)

print(game.items()) # dict_items([('name', 'Super Mario'), ('developer', 'Nintendo'), ('age', 1990)])
for key,value in game.items():
    print('{} = {}'.format(key, value)) # name = Super Mario
