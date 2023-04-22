def chave_maior_valor(dicionario):
    chave_maxima = None
    valor_maximo = float('-inf')
    for chave, valor in dicionario.items():
        if valor > valor_maximo:
            chave_maxima = chave
            valor_maximo = valor
    return chave_maxima

if __name__ == '__main__':
    dicionario = {'a': 1, 'b': 5, 'c': 2, 'd': 9}
    chave = chave_maior_valor(dicionario)
    print(chave) 
