#Outra maneira de interpolar string com variável.
#self: maneira de acessar os atributos dentro da classe, (acessamos os atributos pelo self)
#``pass`` serve para mostrar que algo está vazio propositalmente para não gerar erro.
#Class é em maiúsculo por padrão
# init é para iniciar a função.
# uma função para ser um método, precisa estar dentro de uma classe.

class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite 
        
#Declaração do métodos(funções)

    def extrato(self):
        print(f"Saldo: {self.saldo} do titular {self.titular}") 

    def depositar(self, valor):
        if(valor < 0):
            print(f'Não é possível depositar valores negativos')
        else:
            self.saldo += valor #saldo = saldo + valor

    def sacar(self, valor):
        if(self.saldo < valor):
            print(f'Não foi possível sacar este valor.')
        else: 
            self.saldo -= valor

