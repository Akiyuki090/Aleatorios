class Pessoa:
    def __init__(self, nome):
        self.nome = nome


class ContaBancaria:
    def __init__(self, numero_conta, saldo, proprietario):
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.proprietario = proprietario


class Banco:
    def __init__(self):
        self.contas_bancarias = []

    def criar_conta(self, numero_conta, saldo, proprietario_nome):
        proprietario = Pessoa(proprietario_nome)
        nova_conta = ContaBancaria(numero_conta, saldo, proprietario)
        self.contas_bancarias.append(nova_conta)

    def depositar(self, numero_conta, valor):
        for conta in self.contas_bancarias:
            if conta.numero_conta == numero_conta:
                conta.saldo += valor
                break

    def sacar(self, numero_conta, valor):
        for conta in self.contas_bancarias:
            if conta.numero_conta == numero_conta:
                if conta.saldo >= valor:
                    conta.saldo -= valor
                    break
                else:
                    print("Saldo insuficiente!")
                    break

    def obter_saldo(self, numero_conta):
        for conta in self.contas_bancarias:
            if conta.numero_conta == numero_conta:
                return conta.saldo

        print("Conta bancária não encontrada!")


if __name__ == '__main__':
    banco = Banco()
    banco.criar_conta(123, 1000, "João")
