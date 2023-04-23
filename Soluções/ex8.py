class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def VerNome(self):
        print(f'{self.nome}')
    
    def VerIdade(self):
        print(f'{self.idade}')

if __name__ == '__main__':
    jovem = Pessoa('Marcos', 22)
    jovem.VerIdade()
