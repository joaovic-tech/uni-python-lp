items = ('Machado', 'Camisa', 'Baicon', 'Abacate')

for item in items:
    item = item.lower()
    found_vowels = []

    for letter in item:
        if letter in 'aeiou' and letter not in found_vowels:
            found_vowels.append(letter)

    print('As vogais da palavra "{}" são: {}'.format(item, ' '.join(found_vowels)))
