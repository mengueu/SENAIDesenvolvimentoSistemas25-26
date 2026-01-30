#3. Criar um sistema de agenda telefônica.
'''
a. Crie um dicionário agenda vazio.
b. Implemente opções para:
Adicionar contato, apenas o nome e telefone, sendo agenda[nome] = telefone
Buscar contato pelo nome.
Remover contato.
Listar todos os contatos.
'''

agenda = {}

print("\n\n--- AGENDA ---")
print("1. Adicionar contatos")
print("2. Buscar contatos")
print("3. Remover contatos")
print("4. Listar contatos")
print("5. Sair")

while True:
    
    opcao = input("\nDigite a opção que deseja: ")

    if opcao == '1':
        nome = input("Digite o nome: ")
        telefone = input("Digite o telefone: ")
        agenda[nome]=telefone

    elif opcao == '2':
        buscar = input("Digite qual contato deseja localizar: ")
        if buscar in agenda:
            print(f'\nNome : {buscar} // Telefone : {agenda[buscar]}')
        else:
            print("O contato digitado não existe. Tente localizar algum existente.")
        
    elif opcao == '3':
        remover = input("Digite qual contato deseja remover: ")
        if remover in agenda:
            del agenda[remover]
        else:
            print("Este contato não existe")
            
    elif opcao == '4':
        print("--CONTATOS ADICIONADOS--")
        for i in agenda.keys():
            print(f'Nome : {i} // Telefone : {agenda[i]}')
                  
    elif opcao == '5':
        break

    else:
        print("Insira uma opção válida. Escolha entre 1 e 5.")
    
input("\nPressione ENTER para fechar o programa...")
