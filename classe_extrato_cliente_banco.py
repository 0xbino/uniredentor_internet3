class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class Conta:
    def __init__(self, clientes, numero, saldo = 0):
        self.saldo = 0
        self.clientes = clientes
        self.numeros = numero
        self.operacoes = []
        self.deopsito(saldo)
    def resumo(self):
        print('CC N %s Saldo: %f' %(self.numero, self.saldo))
    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append (['Deposito', valor])
    def extrato(self):
        print('Extrato: %f' % (self.numeros))
        for op in self.operacoes:
            print('%s %f' % (op[0],op[1]))
        print('%s %f' % ('saldo=', self.saldo))
