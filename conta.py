class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite #Outra maneira de interpolar string com variável.
#self: maneira de acessar os atributos dentro da classe.
#``pass`` serve para mostrar que algo está vazio propositalmente para não gerar erro.
#Class é em maiúsculo por padrão
