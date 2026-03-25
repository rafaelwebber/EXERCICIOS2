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

estoque1 = tuple(input("Produtos do estoque 1 (separados por vírgula): ").split(", "))
estoque2 = tuple(input("Produtos do estoque 2 (separados por vírgula): ").split(", "))
estoque_combinado = estoque1 + estoque2  
print(f"Estoque combinado:\n{estoque_combinado}")