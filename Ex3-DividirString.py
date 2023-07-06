frase = input('Digite uma frase:')
tamanho_frase = len(frase)

frase_dividida = frase[:int(tamanho_frase / 2)]

print('Frase dividida: ', frase_dividida)
print('Os últimos 2 caracteres da frase dividida: ', frase_dividida[-2:])
