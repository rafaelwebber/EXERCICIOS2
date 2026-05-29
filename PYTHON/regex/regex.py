import re

# produto = input("Digite o nome do produto: ")
# produto_padronizado = produto.strip().lower()

# print(produto_padronizado)

"""Crie um programa que solicite o nome e a cidade de um cliente e exiba uma mensagem de boas-vindas personalizada.

Exemplo de Entrada:


Copiar
Digite o nome do cliente: Laura
Digite a cidade do cliente: Rio de Janeiro

Saída esperada:

Olá, Laura! Bem-vinda ao sistema da cidade de Rio de Janeiro."""

# nome = input("Digite seu nome: ")
# cidade = input("Digite o nome da sua cidade: ")

# print(f"Olá {nome}! Bem-vinda ao sistema da cidade de {cidade}")

# palavra = input("Digite a palavra: ")

# print(palavra[:3])
# print(palavra[3:6])

'''Como você escreveria um programa que peça ao usuário uma URL e informe se ela é válida ou inválida?

Exemplo de Entrada:

Digite a URL para validação: https://monitorrenan.com

Saída esperada:

URL válida!'''

# url = input("Digite a url: ")

# if url.startswith('https://') and url.endswith('.com'):
#     print("É uma URL valida!")
# else:
#     print("não é uma URL valida!")


"""Com base nesse cenário, crie um programa que receba um texto com uma descrição e exiba uma mensagem com o número encontrado.

Exemplo de Entrada:

Digite a descrição da receita: A receita 1087568 foi enviada pelo cliente.

Saída esperada:

O número da receita é: 1087568"""

# entrada = input("Digite a entrada: ")

# numero = re.findall(r'\d', entrada)[0] #\d Corresponde a qualquer dígito (0-9)
# print(f"O número da receita é: {numero}")

"""texto = input("Digite o texto: ")
remover = input("Digite a palavra que deseja remover: ")
nova_palavra = input("Digite a nova palavra que deseja substituir: ")

nova_frase = re.sub(rf'\b{remover}\b', nova_palavra, texto)"""

"indentificar se é CPF"

cpf = input("Digite um CPF para validar: ")
validar = r'\d{3}\.\d{3}\.\d{3}\-\d{2}'


if re.search(validar, cpf):
    print("é um CPF valido")

else:
    print ("não é um cpf valido")