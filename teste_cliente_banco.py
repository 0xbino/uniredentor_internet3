from classe_cliente_banco import Cliente
from classe_cliente_banco import Conta

grug = Cliente ('Grug Down', '12000')

conta1 = Conta([grug], 1, 1000)
conta1.extrato()
conta1.saque(50)
conta1.deposito(300)
