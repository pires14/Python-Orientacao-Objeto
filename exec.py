from conta import Conta

conta1= Conta(535, "Ricardo", 55.0, 1000.0)
conta2 = Conta(555, "Luana", 100.0, 1000.0)

#Não apresenta erro:
#conta.extrato()
#Apresenta erro:
#conta1.__saldo

conta1.depositar(0)
conta1.extrato
#Ao printar, o PY mostra o endereço no computador onde está sendo salvo
#Classes também recebem parâmetros