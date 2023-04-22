profissoes = []
pessoas = []
temp = {}

while True:
    temp['Nome'] = str(input('Informe o nome: '))
    temp['Idade'] = int(input('Informe a idade: '))
    temp['Profissão'] = str(input('Informe a profissão: '))
    profissoes.append(temp['Profissão'])

    pessoas.append(temp.copy())
    temp.clear()

    resp = str(input('Novo cadastro[s/n]: '))
    if resp == 'n':
        break

print(pessoas)
print(profissoes)

iguais = []

for i in range(len(profissoes)):
    for j in range(i+1, len(profissoes)):
        if profissoes[j] == profissoes[i]:
            iguais.append(profissoes[j])

print(f"Profissões iguais: {iguais}")
