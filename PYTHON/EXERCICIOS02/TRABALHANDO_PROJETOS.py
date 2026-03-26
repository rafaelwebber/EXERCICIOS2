"""João trabalha como garçom em um restaurante e precisa calcular a gorjeta que os clientes deixam ao pagar a conta. 
O restaurante sugere uma gorjeta de 10%, mas alguns clientes podem escolher dar mais ou menos.
Para agilizar o processo, João quer um programa que receba o valor total da conta e a porcentagem de gorjeta desejada e exiba o valor final que o cliente deverá pagar.
Crie um programa que peça ao usuário o valor da conta e a porcentagem de gorjeta. O programa deve calcular e exibir o valor da gorjeta e o total a ser pago."""

'''def gorjeta(valor, porcentagem):
    return valor * (porcentagem / 100)

try:
    valor=float(input("Digite o valor da conta:"))
    porcentagem=float(input("Digite a porcentagem de gorjeta:"))
    garcom = gorjeta(valor, porcentagem)
    resultado = valor + garcom

    print(f"O valor total a ser pago é: {resultado}. \n O valor da gorjeta é: {garcom} e o valor da conta é {valor}")

except ValueError:
    print("Digite um valor valido")


"""Carlos trabalha em um cartório e precisa validar se um CPF informado pelo cliente tem o formato correto antes de prosseguir com o atendimento. 
O CPF deve conter exatamente 11 dígitos numéricos. Se a entrada contiver letras ou qualquer outro caractere que não seja um número, o programa deve exibir uma mensagem de erro.
Crie um programa que peça ao usuário um número de CPF e verifique se ele tem 11 dígitos e contém apenas números."""

def validar(numero):
    try:
        if numero !=11:
            return print ("CPF invalido")

        if not numero.isdigit(): #isdigit verifica se o numero é um digito
            return print ("CPF invalido")
        return print ("CPF valido")
    except ValueError:
        return False

print(validar("12345678901"))'''

''' Mariana é professora de língua portuguesa e quer um programa que conte quantas vogais há em um texto digitado pelos alunos. Isso ajudará a analisar a estrutura das palavras utilizadas.

Crie um programa que peça um texto e exiba quantas vogais (a, e, i, o, u) ele contém.'''

"""def contar_vogais(texto):
    vogais = ['a','e','i','o','u']
    contador = 0
    texto_minusculo = texto.lower()  # aplica .lower() na string, não na lista

    for letra in texto_minusculo:    # percorre cada caractere do texto
        if letra in vogais:
            contador += 1
    print(f"O texto contém {contador} vogais")

print(contar_vogais("Oi, como vai?"))"""

'''Sofia é revisora de textos e precisa identificar palavras muito longas em um parágrafo. Textos mais fáceis de ler costumam ter palavras curtas, 
então ela quer um programa que encontre palavras que tenham mais de 10 letras e as exiba em destaque.

Crie um programa que receba um texto e exiba todas as palavras que possuem mais de 10 letras. Caso nenhuma palavra longa seja encontrada, 
o programa deve avisar o usuário.'''

"""def identificador_palavras_longas(texto):
    palavras = texto.split()
    listaMaiores = []
    listaMenores = []
    for palavra in palavras:
        if len(palavra)> 10:
            listaMaiores.append(palavra)
        
        if len(palavra) < 10:
            listaMenores.append(palavra)

    if listaMaiores: 
        return (f"As palavras grandes são {listaMaiores}")
    
    else:
        return "Não existe palavras que possuem mais de 10 letras"
    
print(identificador_palavras_longas("A programação estruturada facilitou o desenvolvimento de grandes sistemas computacionais"))"""

"""Pedro está desenvolvendo um sistema de cadastro e precisa gerar senhas seguras para os usuários. 
Ele quer um programa que crie senhas aleatórias com letras maiúsculas, minúsculas, números e caracteres especiais.

Crie um programa que gere uma senha aleatória de 12 caracteres, contendo pelo menos uma letra maiúscula, uma minúscula, um número e um caractere especial. Exiba a senha gerada."""
"""import random

def senha_aleatoria():
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    numeros = "0123456789"
    especial = "!@#$%&*"
    maiusculo = alfabeto.upper()
    minusculo = alfabeto.lower()

    senha = [
        random.choice(numeros), #choice retorna um único elemento (string).
        random.choice(especial),
        random.choice(maiusculo),
        random.choice(minusculo)
    ]
    print(senha)

    todos = maiusculo + minusculo + numeros + especial
    senha += random.choices(todos , k = 12 - len(senha)) #choices  retorna uma lista com N elementos.
    print(senha)
    random.shuffle(senha)

    return "".join(senha) # join serve para juntar os elementos de uma lista (ou outra sequência) em uma única string, usando como separador a string que você chama. aqui é vaziu então vai emendar tudo

print(senha_aleatoria())"""

'''Lucas quer criar um jogo de pedra, papel e tesoura para jogar contra o computador. Ele precisa de um programa que permita ao usuário escolher uma opção e depois exiba o resultado da partida.

Crie um programa que permita ao usuário escolher entre pedra, papel ou tesoura. O computador escolherá aleatoriamente uma opção. O programa deve exibir quem venceu a partida. Lembrando que:

Pedra ganha de Tesoura (Pedra quebra Tesoura);
Tesoura ganha de Papel (Tesoura corta Papel);
Papel ganha de Pedra (Papel cobre Pedra);
Se ambos escolherem a mesma opção, é um empate.'''
'''

from ast import main
import random

def jogo (escolha):
    lista = ['pedra', 'papel', 'tesoura']

    if escolha not in lista and escolha!= 'sair':
        print ("Escolha itens validos!")
        return None

    sorteado = random.choice(lista)
    
    if (escolha == 'pedra' and sorteado == "tesoura") or\
        (escolha == 'tesoura' and sorteado == 'papel') or\
        (escolha == 'papel' and sorteado == 'pedra'):
        print(f'O escolhido pelo computador foi: {sorteado}')
        return True
    
    if escolha == sorteado:
        print(f'O escolhido pelo computador foi: {sorteado}')
        return "empate"

    
    return False


def main():
    while True:
        print('------------------------------\n')
        escolha_usuario = input(str('     Escolha \n ------------------------------\n  Pedra, Papel ou Tesoura \n ------------------------------\n  Para sair digite: sair \n ------------------------------\n')).lower()

        
        if escolha_usuario == 'sair':
            print("Encerrando jogo")
            break

        resultado = jogo(escolha_usuario)

        if resultado == True:
            print("Voce venceu")

        if resultado == "empate":
            print("empate")
    
        if resultado == False:
            print("voce perdeu")

main()'''

'''Maria está criando um jogo para seus alunos praticarem lógica e pensamento rápido. Ela quer um programa onde o computador escolhe um número aleatório entre 1 e 100, e o jogador tem que adivinhar qual é.
Além de garantir a jogabilidade, Maria deseja que o programa trate erros de entrada, impedindo que o usuário forneça valores inválidos, como letras ou números fora do intervalo permitido.
Sua tarefa é criar um programa que gere um número aleatório entre 1 e 100 e permita que o usuário tente adivinhar o número. 
O programa deve informar se o palpite é maior ou menor que o número correto, até que o usuário acerte. Se o usuário digitar um valor inválido ou um número fora do intervalo, uma exceção ValueError deve ser lançada .'''

import random 

def jogo_numero_aleatorio():
    numeros = list(range(1,101))
    sorteado = random.choice(numeros)

    
    while True:
        try:
            numero = int(input("Digite um numero de 1 a 100: "))
            if numero < 1 or numero > 100:
                print ("Digite numeros de 1 a 100")
                continue

            if numero > sorteado:
                print("Numero muito alto! Tente novamente")

            if numero < sorteado:
                print("Numero muito baixo! Tente novamente")

            if numero == sorteado:
                print("Parabens voce acertou!")
                break

        except ValueError:
            print("Digite numeros validos!")


def achar_sorteado():
    numeros = list(range(1,101))
    sorteado = random.choice(numeros)

    baixo = 1
    alto = 100
    tentativas = 0

    while True:
        tentativas += 1
        palpite = (alto + baixo)//2

        if palpite == sorteado:
            return print (f"Voce acertou! O numero sorteado foi: {sorteado} \n Em {tentativas} tentativas e o palpite foi: {palpite}")
            break

        if palpite < sorteado:
            baixo = palpite + 1

        if palpite > sorteado:
            alto = palpite - 1
            

'''Carlos está criando uma calculadora simples, mas quer garantir que o programa não quebre se o usuário digitar valores inválidos, ele precisa tratar os erros.

Crie uma calculadora que permita ao usuário escolher entre soma, subtração, multiplicação e divisão. Além de modularizar o código em funções, use try-except para tratar erros de entrada inválida, que consiste em:

Caso digite um caractere em vez de número | exceção a ser lançada: ValueError;
Caso tente fazer uma divisão por 0 | exceção a ser lançada: ZeroDivisionError.'''

def calculadora():
    opcoes = ['+', '-', '*', '/', 'sair']

    while True:
        try:
            print("-----------------------------")
            print("Bem-Vindo a calculado master")
            print("-----------------------------")
            print("Digite 'sair' para sair da calculadora")
            print("-----------------------------")
            opcao = input("Digite a operação que deseja (+, -, *, /): ").lower()

            

            if opcao not in opcoes:
                print("Digite operacoes validas")
            print("-----------------------------")

            if opcao == '+':
                print("-----------------------------")
                print("Somar")
                print("-----------------------------")
                numero1 = float(input("Digite o numero 1 : "))
                numero2 = float(input("Digite o numero 2 : "))
                resultado = numero1 + numero2
                print (f"O resultado é: {resultado}!")

            if opcao == '-':
                print("-----------------------------")
                print("Subtracao")
                print("-----------------------------")
                numero1 = float(input("Digite o numero 1 : "))
                numero2 = float(input("Digite o numero 2 : "))
                resultado = numero1 - numero2
                print (f"O resultado é: {resultado}!")

            if opcao == '*':
                print("-----------------------------")
                print("Multiplicacao")
                print("-----------------------------")
                numero1 = float(input("Digite o numero 1 : "))
                numero2 = float(input("Digite o numero 2 : "))
                resultado = numero1 * numero2
                print (f"O resultado é: {resultado}!")

            if opcao == '/':
                try:
                    print("-----------------------------")
                    print("Divisão")
                    print("-----------------------------")
                    numero1 = float(input("Digite o numero 1 : "))
                    numero2 = float(input("Digite o numero 2 : "))
                    
                    
                    resultado = numero1 / numero2
                    print (f"O resultado é: {resultado}!")
                except ZeroDivisionError:
                    print("Erro: não é possível dividir por zero!")              


            if opcao == "sair":
                print("Saindo...")
                break

        except ValueError:
            print("Digite numeros validos!")

'''Ana precisa de um programa simples para gerenciar suas tarefas diárias. Ela quer poder adicionar, visualizar e remover tarefas de uma lista.

Crie um programa com um menu interativo que permita ao usuário adicionar, visualizar e remover tarefas. Use uma lista para armazenar as tarefas.'''

def gerenciador_tarefas():
    lista = []

    while True:
        opcoes = ['1', '2', '3', '4', 'sair']

        print("-----------------------------")
        print("Bem vindo a suas tarefas!")
        print("-----------------------------")
        print("1. Adicionar tarefa")
        print("2. Visualizar tarefas")
        print("3. Remover tarefa")
        print("4. Sair")
        print("-----------------------------")
        print("\n")
        escolha = str(input("Escolha uma das opcoes: "))

        if escolha not in opcoes:
            print("Escolha de 1 a 4")

        if escolha == "1":
            print("-----------------------------")
            tarefa = input("Digite sua tarefa: ")
            print("-----------------------------")
            lista.append(tarefa)

        elif escolha =='2':
            print("-----------------------------")
            print(lista)
            print("-----------------------------")

        elif escolha == '3':
            print("-----------------------------")
            remover = int(input("Qual tarefa voce quer remover: "))
            del lista[remover]

        elif escolha == '4':
            print("Saindo...")
            break


'''Um banco está desenvolvendo um sistema para caixas eletrônicos e precisa de um programa que simule o saque de dinheiro. O caixa deve entregar o valor solicitado pelo usuário usando a 
menor quantidade possível de cédulas. As cédulas disponíveis são: R$ 100, R$ 50, R$ 20, R$ 10, R$ 5 e R$ 2.
Crie um programa que solicite ao usuário o valor do saque e calcule quantas cédulas de cada tipo serão necessárias para entregar o valor. 
O programa deve garantir que o valor solicitado seja válido (múltiplo de 2, já que não há cédulas de R$ 1) e tratar erros de entrada caso não seja digitado um valor numérico válido.'''
def caixa_eletronico():
    disponivel = [100, 50, 20, 10, 5, 2]
    try:
        valor_solicitado = int(input("Digite o valor desejado: "))

        if valor_solicitado % 2 != 0 or valor_solicitado <= 0:
            print("Valor invalido")
            return

        for cedula in disponivel:
            qtd = valor_solicitado//cedula
            valor_solicitado = valor_solicitado % cedula 
            if qtd > 0: 
                print(f"{qtd} cédula(s) de R$ {cedula}")
                
    except ValueError:
        print("Entrada inválida! Digite apenas números inteiros.")

caixa_eletronico()