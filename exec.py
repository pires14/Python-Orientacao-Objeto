from conta import Conta

conta = Conta(535, "Ricardo", 55.0, 1000.0)
conta1 = Conta(555, "Luana", 100.0, 1000.0)

#Não é possível sacar se não tem o dinheiro necessário

conta1.depositar(-10)
conta1.extrato()


#Ao printar, o PY mostra o endereço no computador onde está sendo salvo
#Classes também recebem parâmetros