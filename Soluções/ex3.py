def mais_de_tres(texto):
    separa = texto.split(' ')
    print(separa)
    maior = []

    for i in separa:
        if len(i) > 3:
            maior.append(i)

    print(maior)

if __name__ == '__main__':
    mais_de_tres('mira briga mais mal mi')
