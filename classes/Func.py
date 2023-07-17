# simples
def realce():
    #corpo da função
    print('|','_' * 10, '|')
    print('|','_' * 10, '|'),

realce()

# com parametros
def sub2(x, y):
    res = x - y
    print(res)

sub2(5, 7)
sub2(y = 40, x = 38)

# adicionando valores padões
def soma3(x = 0, y = 0, z = 0):
    res = x + y + z
    print(res)

soma3(10, 15, 5)
soma3(10, 15)    # z foi omitido
soma3(10)        # y e z foram omitidos
soma3()        # todos os parâmetros foram omitidos
