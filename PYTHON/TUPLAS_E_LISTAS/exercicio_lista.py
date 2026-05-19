''' 001 - Ana está organizando uma festa de aniversário e precisa de uma lista de convidados que não tenha repetições , pois algumas pessoas foram convidadas mais de uma vez por engano. 
Ela gostaria que o programa solicitasse o nome dos convidados e, ao final, exibisse a lista organizada sem repetições.
Escreva um programa que receba os nomes dos convidados até que o usuário digite 'sair', e ao final mostre a lista de convidados sem repetições.

lista_convidados = []

while True:
    convidado = input('Digite o nome do convidado ou "sair" para encerrar o programa: ')
    if convidado != 'sair':
        if convidado not in lista_convidados:
            lista_convidados.append(convidado)

    else:
        print('Encerrando...')
        break

print (lista_convidados)'''


'''002 - Clara é editora de uma revista e deseja comparar dois artigos para identificar quais palavras aparecem em ambos. 
Sua tarefa é criar um programa que receba dois textos e exiba o conjunto de palavras comuns entre eles.
#set transforma lista em um conjiunto, coniuntos nao permite palavras repetidas 
texto1=set(input("Digite o primeiro texto: ").lower().split())
texto2=set(input("Digite o segundo texto: ").lower().split())

comum = texto1.intersection(texto2)

print(f'Palavras iguais são: {comum}') '''

'''003 - Laura e Ana resolveram fazer compras juntas, mas criaram duas listas diferentes. Elas querem um programa que mostre:

Quais itens apareceram nas duas listas

Quais foram exclusivos de Laura

Quais foram exclusivos da Ana

Escreva um programa que solicite as listas e mostre os resultados dessas comparações.

lista1 = set(input("Digite a lista 1: ").lower().split(','))
lista2 = set(input("Digite a lista 2: ").lower().split(','))

lista_interseccao = lista1.intersection(lista2)

listaLaura = []
for i in lista1:
    if i not in lista2:
        listaLaura.append(i)

listaAna = []
for i in lista2:
    if i not in lista1:
        listaAna.append(i)

print(f'Itens que apararecem nas duas listas {lista_interseccao}, Lista de Laura: {listaLaura} \n Lista de Ana: {listaAna}')

'''

'''004- Marina trabalha no setor de segurança de uma empresa e precisa verificar se um determinado conjunto de permissões 
faz parte das permissões principais de um sistema. 
Sua tarefa é desenvolver um programa que receba duas listas de permissões e verifique se a segunda lista está contida na primeira.

permissoes = ["leitura", "escrita", "execução", "compartilhamento" ]

solicitada = input("Digite as solicitações para analise: ").lower().split(", ")

for i in solicitada:
    if i in permissoes:
        print ("As permissões solicitadas fazem parte das permissões principais.")

    else:
        print ("As permissões solicitadas não fazem parte das permissões principais.")'''

''' 005 - Joana é gerente de projetos e precisa consolidar as listas de tarefas de duas equipes distintas.
 Após unir as listas, ela quer remover uma tarefa específica informada pelo usuário. Sua tarefa é criar um programa que realize essa operação.

lista1 = {t.strip().lower() for t in input("Equipe A: ").split(",")}
lista2 = {t.strip().lower() for t in input("Equipe B: ").split(",")}

completa = lista1.union(lista2)

remover = input("Digite o item que deseja remover: ").lower()

completa.discard(remover)

print(completa)'''

'''006 - Ana é responsável pelo controle de estoque de uma loja de artigos para papelaria. Ela precisa de um programa que 
permita cadastrar produtos em forma de dados estruturados. O sistema deve solicitar o nome e a quantidade de três produtos 
e, ao final, exibir as informações cadastradas em um dicionário, onde cada produto será uma chave e a quantidade correspondente será o valor.

dicionario_produtos = {}

for i in range (3):
    produto = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade do produto: "))
    dicionario_produtos[produto] = quantidade

print(f"Dicionário de produtos: {dicionario_produtos}")
'''


''' 007- Ana percebeu que, após o cadastro inicial dos produtos, precisa atualizar a quantidade de um item específico no estoque. 
Sua tarefa é criar um programa que solicite o nome do produto e a nova quantidade, atualizando essa informação no dicionário de estoque.


estoque = { 

    "Caderno universitário": 50, 

    "Caneta azul": 120, 

    "Borracha branca": 30 

} 

produto = input("Digite o produto a ser atualizado: ")
nova_quantidade = int(input("Digite a nova quantidade: ")) 

if produto in estoque:
    estoque[produto] = nova_quantidade
    print(f"Quantidade atualizada com sucesso!\n Nova quantidade {nova_quantidade}")

else:
    print("Produto nao existe em estoque")


print(estoque[produto])'''

'''008- Lucas é voluntário na organização de uma maratona e recebeu a lista de participantes com suas respectivas idades. 
Agora, ele precisa de um programa que apresente três informações:

Os nomes de todos os participantes.

As idades de todos os participantes.

Uma relação completa com o nome e a idade de cada um.

Sua tarefa é criar esse programa com base nas informações fornecidas.


participantes = { 

    "Mariana": 25, 

    "Carlos": 32, 

    "Beatriz": 28, 

    "Rafael": 35 

} 

print(f'Os nomes dos participantes são: {', '.join(participantes.keys())}')
print(f'Suas idades são: {', '.join(str(idade) for idade in participantes.values())}')

for nome, idade in participantes.items():
    print(f'nome: {nome}, idade: {idade}')
'''

'''009- Laura está organizando um workshop sobre tecnologia e precisa de um programa que permita remover participantes que desistiram do evento. 
O sistema armazena os participantes em um dicionário, onde cada chave é o nome e o valor é um conjunto com os dados do participante. 
O programa deve solicitar o nome de um participante e remover esse nome da lista de participantes registrados, caso exista.


participantes = { 

    "Workshop 1": {"Alice", "Bruno", "Carla", "Diego"}, 

    "Workshop 2": {"Fernanda", "Gustavo", "Helena"} 

} 

participante_remover = input("Digite o nome do participante que deseja remover: ")

for workshop, nome in participantes.items():
    print(workshop)
    nome.discard(participante_remover)
    print("Lista atualizada")

for workshop, nome in participantes.items():
    print(f"{workshop}: {nome}")'''

'''010-Nathalia é gerente de uma loja virtual e precisa de um sistema que receba os registros de vendas organizados por categoria de produto. 
Cada categoria contém uma lista de dicionários representando as vendas individuais, com informações sobre o produto, a quantidade vendida 
e o valor unitário.
Sua tarefa é criar um programa que exiba o total de vendas por categoria. teste'''


vendas = { 

    "Eletrônicos": [ 

        {"produto": "Smartphone", "quantidade": 5, "valor_unitario": 2000}, 

        {"produto": "Tablet", "quantidade": 3, "valor_unitario": 1500} 

    ], 

    "Eletrodomésticos": [ 

        {"produto": "Geladeira", "quantidade": 2, "valor_unitario": 3000}, 

        {"produto": "Micro-ondas", "quantidade": 4, "valor_unitario": 800} 

    ], 

    "Livros": [ 

        {"produto": "Livro A", "quantidade": 10, "valor_unitario": 50}, 

        {"produto": "Livro B", "quantidade": 5, "valor_unitario": 100} 

    ] 

} 
print("Total de vendas por categoria: ")
for categoria, produto in vendas.items():
    valor_total = 0
    for item in produto:
        quantidade = item["quantidade"]
        valor_unitario = item["valor_unitario"]
        valor_total += quantidade * valor_unitario
    
    print(f'{categoria} : R$ {valor_total}')
            
