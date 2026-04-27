#Exercício 1: alterar o limite de contas especiais.
class Conta:
    def __init__(self, numero, titular, saldo, limite=1000.0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

from conta import Conta

conta = Conta(535, "Ricardo", 55.0)
conta1 = Conta(555, "Luana", 100.0, 1000.0)
print(conta.saldo)
print(conta1)

#Execício 2: crie uma classe que represente um vídeo com os atributos
#título, duração e views.
class Video:
    def __init__(self, titulo, duracao, views):
        self.titulo = titulo
        self.duracao = duracao
        self.views = views

video = Video()
Video("Lucas, um estranho no formigueiro", 10.0, 125.0)
print(Video)

#Exercício 3: livro
class Livro:
    def __init__(self, titulo, autor, data_public):
        self.titulo = titulo
        self.autor = autor
        self.data_public =  data_public
    
livro = Livro()
