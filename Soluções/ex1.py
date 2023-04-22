'''
Dica, usar a função embutida reduce
'''

def lista():
    from functools import reduce


    lista = []
    while True:
        lista.append(int(input('Insira um valor: ')))
        resp = str(input('Quer continuar[s/n]: '))
        if resp == 'n':
            break
    print(lista)
    soma = reduce(lambda a,b: a+b, lista)
    print(f'A média dessa lista é: {soma/len(lista)}')

lista()
