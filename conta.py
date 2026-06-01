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
        self.__limite_especial = limite

    
    #Ao colocar 2 __ , significa que não é para ser alterado diretamente. 
    # Eles ficam privados para serem acessados pelos métodos.
    #Declaração dos métodos(funções)

    def extrato(self):
        print(f'Saldo: {self.__saldo} do titular {self.__titular}') 
        #Aqui é só um print, ou seja, uma mensagem.

    def depositar(self, valor):
        if(valor <= 0):
            print(f'Não é possível depositar valores negativos e nem nada.')
        else:
            self.__saldo += valor #saldo = saldo + valor

    def saque_permitido(self, valor_saque):
        valor_disponivel_saque = self.__saldo + self.__limite_especial
        return valor_saque <= valor_disponivel_saque

    def sacar(self, valor):
        if(self.saque_permitido(valor)):
            self.__saldo -= valor
        else: 
            print(f'O valor {valor} passou do limite.')

    def transferir(self, valor, conta_destino):
        if(self.__saldo < valor) or (valor < 0):
            print(f'Não é possível realizar a transferência.')
        else:
            self.sacar(valor)
            conta_destino.depositar(valor)

    # Métodos get para retornar apenas os valores das propriedades.
    # Get sempre tem um return.
    # Property serve para retornar um valor
    @property
    def numero(self):
        return self.__numero
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def saldo(self):
        return self.__saldo
    # Decorador: serve para transformar em uma função 
    # que não precisa ser chamada com parênteses.
    # E não precisa mais de get

    @property
    def limite(self):
        return self.__limite_especial
    
    # Método estático que é usado apenas pela classe
    # e não depende do objeto (conta)
    
    # Set não retorna algo, mas altera.
    # Métodos para manipular os valores das propiedades
    @limite.setter
    def limite(self, limite):
        self.__limite_especial = limite

    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    @staticmethod
    def codigo_banco():
        return '001'
    
    @staticmethod
    def codigos_banco():
        return {'Banco do Brasil':'001',
                'Caixa':'104', 
                'Bradesco':'37'}