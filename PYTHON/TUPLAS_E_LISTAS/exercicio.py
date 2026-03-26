"""01 - Roberto está organizando sua despensa e quer verificar se determinados itens já estão armazenados antes de adicioná-los à lista de compras.
Ajude Roberto a criar um programa que pergunte o item desejado e verifique se ele está na lista de itens disponíveis na despensa. Caso o item não esteja na lista, 
o programa deve informar que ele precisa ser comprado."""

'''itens_disponiveis = ['banana', 'arroz', 'queijo', 'cerveja']

produto = input("Digite o item desejado: ")

if produto in itens_disponiveis:
    print(f'O item: {produto} está disponivel!')

    
if produto not in itens_disponiveis:
    print(f'O item: {produto} não está disponivel, compre!')
        '''

'''02 - escola realizou um concurso de redação, e o próximo passo é organizar as notas dos participantes para definir a ordem de premiação. 
Para garantir transparência, as notas precisam ser classificadas em ordem crescente, do menor para o maior valor.
Com base nisso, desenvolva um programa que receba como entrada uma lista contendo as notas de todos os participantes e exiba, ao final, essa lista ordenada em ordem crescente.

Exemplo de Entrada:

Notas: [85, 70, 90, 60, 75]

Saída esperada:

Notas ordenadas: [60, 70, 75, 85, 90]'''

'''notas = []


participantes = int(input("Digite a quantidade de aulos participante: "))

for i in range(participantes):
        
    nota = int(input(f"Digite a nota da redação do aluno {i+1}: "))
    notas.append(nota)

notas.sort()
print(notas)'''

'''03- Uma ONG está organizando uma campanha de arrecadação de alimentos e precisa registrar os nomes dos voluntários que vão ajudar na ação. 
À medida que os voluntários se inscrevem, seus nomes devem ser adicionados à lista e quando for digitado a palavra sair o programa deve encerrar.

Ajude a ONG a criar um programa que permita registrar os voluntários e exiba a lista completa no final.

Exemplo de Entrada:

Digite o nome do voluntário (ou 'sair' para encerrar): Ana
Digite o nome do voluntário (ou 'sair' para encerrar): João
Digite o nome do voluntário (ou 'sair' para encerrar): Mariana
Digite o nome do voluntário (ou 'sair' para encerrar): sair

povo = []
while True:
    
    voluntarios = input("Digite o nome do voluntário (ou 'sair' para encerrar): ")

    if voluntarios != 'sair':
        povo.append(voluntarios)
        print(povo)

    else:
        print(povo)
        break
'''

''' 04- Armano trabalha com a gestão de dois estoques de mercadorias que são representados como tuplas. Agora, ele precisa criar um relatório unificado com os 
produtos dos dois estoques juntos.

Para ajudá-lo, como você criaria um programa que ler as informações dos estoques e gera um relatório com todos os produtos juntos?

Exemplo de Entrada:

Produtos do estoque 1 (separados por vírgula): Arroz, Feijão, Macarrão
Produtos do estoque 2 (separados por vírgula): Óleo, Sal, Açúcar
Copiar código
Saída esperada:

Estoque combinado:
('Arroz', 'Feijão', 'Macarrão', 'Óleo', 'Sal', 'Açúcar')'''

'''estoque1 = tuple(input("Produtos do estoque 1 (separados por vírgula): ").split(", "))
estoque2 = tuple(input("Produtos do estoque 2 (separados por vírgula): ").split(", "))
estoque_combinado = estoque1 + estoque2  
print(f"Estoque combinado:\n{estoque_combinado}")'''

''' 05 -Camila adora receber amigos para jantares temáticos. Para o próximo encontro, ela quer garantir que a ordem de chegada seja respeitada, mas ainda precisa fazer ajustes na lista de convidados. 
Camila quer adicionar novos nomes e organizá-los em posições específicas.

Como você criaria um programa que mostre a lista inicial, permita a inserção de um novo nome em uma posição escolhida e exiba a lista atualizada?

Exemplo de Entrada:

Lista atual de convidados: ['Ana', 'Pedro', 'Carlos']
Digite o nome do novo convidado: João
Digite a posição na qual deseja inserir o convidado: 2
Copiar código
Saída esperada:

Lista atualizada de convidados: ['Ana', 'João', 'Pedro', 'Carlos']'''

'''lista_convidados = ['Ana', 'Pedro', 'Carlos']

print(lista_convidados)

convidado = input("Digite o nome do novo convidado: ")
posicao = int(input('Digite a posição na qual deseja inserir o convidado: '))

lista_convidados.insert(posicao - 1, convidado)

print(lista_convidados)'''

''' 06 -A Futuro Eventos, uma empresa especializada em organização de conferências, cometeu um erro ao registrar a sequência dos eventos de uma conferência importante. 
Os eventos foram registrados na ordem inversa à que deveriam acontecer. Agora, a equipe precisa corrigir a ordem dos eventos para garantir que a conferência aconteça conforme o planejamento original.

Considerando a lista inicial de eventos, crie um programa que permita ao organizador ordená-los, de forma que a lista final siga a sequência correta.

eventos_registrados = ['Encerramento', 'Palestra 3', 'Palestra 2', 'Abertura']
Copiar código
Saída esperada:

Ordem corrigida: ['Abertura', 'Palestra 2', 'Palestra 3', 'Encerramento']'''

'''eventos_registrados = ['Encerramento', 'Palestra 3', 'Palestra 2', 'Abertura']

eventos_registrados.reverse()
print(eventos_registrados)'''




'''07- O clube de atletismo Alura Runners organizou uma corrida e divulgou a lista com a classificação final dos participantes. 
Mas, um erro foi identificado: um dos nomes está incorreto. O organizador precisa de um programa que permita localizar o nome errado e substituí-lo pelo correto.

Como você escreveria um programa que solicite o nome errado, o nome correto e atualize a lista exibindo a nova classificação ao final?

Exemplo de Entrada:

Digite o nome incorreto: Carlos
Digite o nome correto: João
Copiar código
Saída esperada:

O nome Carlos foi substituído por João.
Lista atualizada: ['Ana', 'João', 'Pedro']'''

'''
nomes = ['Ana', 'Carlos', 'Pedro']  
nome_errado = input("Digite o nome incorreto: ")
nome_certo = input("Digite o nome correto: ")

if nome_errado in nomes:
    index = nomes.index(nome_errado)
    nomes[index] = nome_certo
    print(f"O nome {nome_errado} foi substituído por {nome_certo}.")
    print(f"Lista atualizada: {nomes}")
else:
    print("Nome incorreto não encontrado na lista.")'''

'''08- Paulo está criando uma lista de pedidos para a lanchonete. Ele já tem todos os pedidos, mas percebeu que o último foi inserido por engano e precisa removê-lo.
Diante deste problema, ajude Paulo criando um programa que automatize essa operação, permitindo listar os pedidos e remover o último item automaticamente.

Exemplo de Entrada:

Pedidos feitos (separados por vírgula): Sanduíche, Suco, Sobremesa

Saída esperada: Pedidos finais: ['Sanduíche', 'Suco']'''

'''

pedidos_feitos = ("Sanduíche", "Suco", "Sobremesa")
pedidos = tuple(input("Digite os pedidos: ").split(", "))
pedido_completo = pedidos_feitos + pedidos
print (f"Pedido antes da remoção: {pedido_completo}")

pedido_completo = pedido_completo[:-1]

print (pedido_completo)'''


'''09 - A professora Helena quer facilitar sua rotina na hora de calcular a média das notas finais da turma. Ela sempre anota as notas dos alunos ao longo do semestre e, 
no final, precisa de um relatório para saber se a turma está indo bem.

Para isso, ajude a professora a criar um programa que receba as notas finais de todos os alunos e calcule a média da turma.

Exemplo de Entrada:

Digite as notas dos alunos separadas por vírgula: 8.5, 7.0, 9.2, 6.8

Saída esperada:

Média final da turma: 7.88'''



'''notas = input("Digite as notas dos alunos separadas por vírgula: ").split(", ")
notas = [float(nota) for nota in notas]

media = sum(notas)/len(notas)

print (media)'''



'''Uma escola está organizando os dados dos alunos para criar um relatório resumido. Cada aluno tem seus dados registrados em uma única entrada, 
incluindo nome, idade e nota final no semestre. Esses dados devem ser exibidos separadamente para cada aluno no formato abaixo:

Aluno: Nome
Idade: Idade
Nota: Nota
Copiar código
Ajude a escola a desenvolver um programa que registre as informações dos alunos, organize os dados e exiba um relatório detalhado com as informações separadamente.

Exemplo de Entrada:

Digite os dados do aluno no formato Nome, Idade, Nota separados por vírgula: João, 16, 8.5, Maria, 17, 9.2, Pedro, 15, 7.8
Copiar código
Saída esperada:

Aluno: João
Idade: 16
Nota: 8.5

Aluno: Maria
Idade: 17
Nota: 9.2

Aluno: Pedro
Idade: 15
Nota: 7.8'''

alunos = []

while True:
    entrada = input("Digite nome, idade e nota (ex: Ana, 18, 9.5) ou Enter para sair: ").strip()
    if entrada == "":
        break

    partes = [p.strip() for p in entrada.split(",")]
    if len(partes) != 3:
        print("Formato inválido. Use: nome, idade, nota")
        continue

    nome, idade, nota = partes
    alunos.append((nome, int(idade), float(nota)))

for nome, idade, nota in alunos:
    print("=================")
    print(f"Aluno: {nome}")
    print(f"Idade: {idade}")
    print(f"Nota: {nota}\n")