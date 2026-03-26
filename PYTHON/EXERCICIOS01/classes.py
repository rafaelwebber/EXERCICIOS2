class Restaurante:
    lista = []

    def __init__(self, nome, categoria):
        self.nome= nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.lista.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria}'

    @classmethod
    def listar_restaurantes(cls):
        for restaurante in Restaurante.lista:
            print(f'{restaurante.nome} | {restaurante.categoria}')

restaurante_praca = Restaurante('pizza', 'italiana')

restaurante_pizza = Restaurante('hamburguer', 'Americano')

#Restaurante.listar_restaurantes()


class Musica: 

    musicas = []
    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.musicas.append(self)

    def __str__(self):
        return f'{self.nome} | {self.artista} | {self.duracao}'

    
    @classmethod
    def listar_musicas(cls):
        for musica in Musica.musicas:
            print (f'{musica.nome} | {musica.duracao} | {musica.artista}')
        

musica1 = Musica('test', 'rafa', 35)

#Musica.listar_musicas()

#1 Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. 
# Crie uma instância dessa classe e atribua valores aos seus atributos.

class Carro:
    carros = []
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        Carro.carros.append(self)

    def __str__(self):
        return f'{self.modelo} | {self.cor} | {self.ano}'

    @classmethod
    def todos_carros(cls):
        for carro in Carro.carros:
            print (f'{carro.modelo} | {carro.cor} | {carro.ano}')

carro1 = Carro('toyta', 'civic', 2014)

#Carro.todos_carros()

#Crie uma classe chamada Cliente e pense em 4 atributos. 
# Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.

class Cliente:
    clientes = []

    def __init__(self, nome, endereco, país, idade):
        self.nome = nome 
        self.endereco = endereco
        self.país = país
        self.idade = idade
        self._ativo = False
        Cliente.clientes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.endereco} | {self.país} | {self.idade}'

    @classmethod
    def listar_clientes(cls):
        for cliente in Cliente.clientes:
            print (f'{cliente.nome} | {cliente.endereco} | {cliente.país} | {cliente.idade} | {cliente.ativo}')

    @property
    def ativo(self):
        return "verdadeiro" if self._ativo else "falso"

    def alterar_estado(self):
        self._ativo = not self._ativo


cliente1 = Cliente('rafa', 'test', 'Brasil', 25)

cliente1.alterar_estado()

cliente2 = Cliente('bruno', 'test', 'Brasil', 33)

#Cliente.listar_clientes()

#Crie uma nova classe chamada Pessoa com atributos como nome, idade e profissão. Adicione um método especial __str__ para imprimir uma representação em string da pessoa. 
# Implemente também um método de instância chamado aniversario que aumenta a idade da pessoa em um ano. Por fim, adicione uma propriedade chamada saudacao que retorna uma 
# mensagem de saudação personalizada com base na profissão da pessoa.

class Pessoa:
    lista = []
    def __init__(self, nome, idade, profissao):
        self.nome      = nome
        self.idade     = idade 
        self.profissao = profissao
        Pessoa.lista.append(self)

    def __str__(self):
        return f'{self.nome} | {self.idade} | {self.profissao}'

    def aniversario (self):
        self.idade += 1

    @property
    def saudacao(self):
        return f'Olá {self.nome}! Voce tem {self.idade} anos e trabalha com a profissao {self.profissao}'

    @classmethod
    def listar_todos(cls):
        for pessoa in Pessoa.lista:
            print(f"{pessoa.nome} | {pessoa.idade} | {pessoa.profissao}")


pessoa1 = Pessoa('Sofia', 23, 'Dentista')

#pessoa1.listar_todos()

#print(pessoa1.saudacao)
pessoa1.aniversario()

#pessoa1.listar_todos()

#1 Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.
from avaliacao import Avaliacao

class ContaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False
        self._avaliacao = []

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return "ativa" if self._ativo else "inativa"

    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return "Nenhuma avaliação"

        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_notas, 1)
        return media

# 2 Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.
    def __str__(self):
        return f'Olá {self.titular} seu saldo é R$ {self.saldo}. Sua conta está: {self.ativo}. Sua avaliação é: {self.media_avaliacao}'

# 3 Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.
    def ativar_conta(self):
        self._ativo = True

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

# 4 Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.

# 5 Crie uma instância da classe e imprima o valor da propriedade titular.

conta1 = ContaBancaria("test", 100)
conta2 = ContaBancaria("teste2", 200)

conta1.receber_avaliacao('gui', 8)
conta1.receber_avaliacao('rafa', 6)
conta1.receber_avaliacao('sofia', 10)
print(conta1)
conta1.ativar_conta()
print(conta1)
print(conta1.titular)  # 5 - imprimir a propriedade titular