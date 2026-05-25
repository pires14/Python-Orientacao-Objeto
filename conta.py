#Outra maneira de interpolar string com variável.
#self: maneira de acessar os atributos dentro da classe, (acessamos os atributos pelo self)
#``pass`` serve para mostrar que algo está vazio propositalmente para não gerar erro.
#Class é em maiúsculo por padrão
# init é para iniciar a função.
# função: fora da classe
# Método: dentro da classe

class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite 
    
    #Ao colocar 2 __ , significa que não é para ser alterado diretamente. 
    # Eles ficam privados para serem acessados pelos métodos.
    #Declaração dos métodos(funções)

    def extrato(self):
        print(f'Saldo: {self.__saldo} do titular {self.__titular}') 

    def depositar(self, valor):
        if(valor < 0):
            print(f'Não é possível depositar valores negativos')
        else:
            self.__saldo += valor #saldo = saldo + valor

    def sacar(self, valor):
        if(self.__saldo < valor):
            print(f'Não foi possível sacar este valor.')
        else: 
            self.__saldo -= valor

    def transferir(self, valor, conta_destino):
        if(self.__saldo < valor) or (valor < 0):
            print(f'Não é possível realizar a transferência.')
        else:
            self.sacar(valor)
            conta_destino.depositar(valor)
        
    def inadimplentes(self, cliente):
        pass