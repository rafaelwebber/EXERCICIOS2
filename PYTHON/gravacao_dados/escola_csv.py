import csv

while True:
    print("---------------------------- ")
    print("##### Controle Escolar ####")
    print("\n Digite a opção desejada:")
    print("     1- Salvar notas dos alunos ")
    print("     2- Ler notas ")
    print("     3- Sair ")
    print("----------------------------")
    resposta = int(input("Digite a opção desejada: \n"))
    
    if resposta == 1:
        while True:
            print("Digite (voltar) para retornar ao Menu Escolar")

            nome = input("Digite o nome do aluno: ")           
            if nome.upper() == "VOLTAR":
                break

            nota = float(input("Digite a nota do aluno: "))
            
            with open("PYTHON/gravacao_dados/alunos.csv", 'a', encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow([nome, nota]) 

    if resposta == 2:
        print("----------------------------")
        print ("Alunos | Notas \n")

        with open("PYTHON/gravacao_dados/alunos.csv", "r") as f:
            for linha in f:
                print(linha)
        
    if resposta == 3:
        break