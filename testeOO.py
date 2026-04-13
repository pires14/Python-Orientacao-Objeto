#numero = 123456789
#titular = "Joãozinho"
#saldo = 400.0
#limite = 2000.0

#contas = {
    #"numero":123456789,
    #"titular": "Joaozinho",
    #"saldo": 400.0,
    #"limite": 2000.0
#}
#print(contas["titular"])
#print(contas["limite"])

def criar_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular,"saldo": saldo,"limite": limite
    }
    return conta

conta = criar_conta(345,"Lucas",200.0,1000.0)
#print(conta["limite"])

def depositar(conta, valor):
    conta["saldo"] += valor #saldo = saldo + valor

def sacar(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print(f'O seu saldo atual e: {conta["saldo"]}')

depositar(conta, 400.0)
extrato(conta)
sacar(conta, 200.0)
extrato(conta)

