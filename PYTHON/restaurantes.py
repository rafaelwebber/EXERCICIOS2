class Restaurante:
    lista = []

    def __init__(self, nome, categoria):
        self.nome= nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.lista.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria}'

    def listar_restaurantes():
        for restaurante in Restaurante.lista:
            print(f'{restaurante.nome} | {restaurante.categoria}')

restaurante_praca = Restaurante('pizza', 'italiana')

restaurante_pizza = Restaurante('hamburguer', 'Americano')

Restaurante.listar_restaurantes()


class Musica: 

    musicas = []
    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.musicas.append(self)

    def __str__(self):
        return f'{self.nome} | {self.artista} | {self.duracao}'

    

    def listar_musicas():
        for musica in Musica.musicas:
            print (f'{musica.nome} | {musica.duracao} | {musica.artista}')
        

musica1 = Musica('test', 'rafa', 35)

Musica.listar_musicas()

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
        return f'{Carro.modelo} | {Carro.cor} | {Carro.ano}'

    def todos_carros():
        for carro in Carro.carros:
            print (f'{carro.modelo} | {carro.cor} | {carro.ano}')

carro1 = Carro('toyta', 'civic', 2014)

Carro.todos_carros()

#Crie uma classe chamada Cliente e pense em 4 atributos. 
# Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.

class Cliente:
    clientes = []

    def __init__(self, nome, endereco, país, idade):
        self.nome = nome 
        self.endereco = endereco
        self.país = país
        self.idade = idade
        Cliente.clientes.append(self)

    def __str__(self):
        return f'{Cliente.nome} | {Cliente.endereco} | {Cliente.país} | {Cliente.idade}'

    def listar_clientes():
        for cliente in Cliente.clientes:
            print (f'{cliente.nome} | {cliente.endereco} | {cliente.país} | {cliente.idade}')

cliente1 = Cliente('rafa', 'test', 'Brasil', 25)
cliente2 = Cliente('bruno', 'test', 'Brasil', 33)
Cliente.listar_clientes()