class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def definir_marca(self, marca):
        self.marca = marca

    def definir_modelo(self, modelo):
        self.modelo = modelo

    def definir_ano(self, ano):
        self.ano = ano

    def obter_marca(self):
        return self.marca

    def obter_modelo(self):
        return self.modelo

    def obter_ano(self):
        return self.ano

    def calcular_idade(self):
        from datetime import datetime

        ano_atual = datetime.now().year
        return ano_atual - self.ano
