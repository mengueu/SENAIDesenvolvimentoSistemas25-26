#DESAFIO
'''
Criar um programa em Python que simule uma lista de compras, usando apenas os métodos básicos de listas.
Funcionalidades:
1. Adicionar Item.
2. Listar Itens.
3. Remover um Item.
4. Ver quantidade de Itens.
5. Sair
'''

nome = input("Digite seu nome: ")
print("Bem vindo Sr(a)",nome,"!")
print("Aqui está um guia personalizado para você usufruir ao máximo de nosso sistema!")
print("\nGUIA LISTA DE COMPRAS:")
print("- Insira um item por vez.")
print("- Em caso de remoção, digite extamente como o item foi adicionado.")
print("- Ao escolher a opção não digite letras ou caracteres especiais, apenas o número correspondente.")
print("- Ao escrever o item não utilize números ou caracteres especiais, apenas letras.")


item = []
quantidade = 0
print("\n\n--- LISTA DE COMPRAS ---")
print("1. Adicionar item")
print("2. Ver lista")
print("3. Remover um item")
print("4. Quantidade de itens")
print("5. Sair")

while True:
    opcao = int(input("\nEscolha a opção desejada: "))
    if opcao == 5:
        break
    
    elif opcao == 1:
        item.append(input(str("\nDigite o item que deseja: ")))
        quantidade = quantidade+1
        
    elif opcao == 2:
        print("ITENS SELECIONADOS:")
        for itens in item:
            print("-",itens)
            
    elif opcao == 3:
        item.remove(input("\nDigite o item que deseja REMOVER: "))
        quantidade = quantidade-1
        
    elif opcao == 4:
        if quantidade > 1 or quantidade == 0:
            print("\nVocê têm",quantidade,"itens adicionados.")
        else:
            print("\nVocê tem",quantidade,"item adicionado.")
        
if quantidade > 1:
    print("\nRESUMO LISTA DE COMPRAS:\nVocê selecionou",quantidade,"itens e foram:")
    for itens in item:
            print("-",itens)
elif quantidade == 1:
    print("\nRESUMO LISTA DE COMPRAS:\nVocê selecionou",quantidade,"item e foi:")
    for itens in item:
            print("-",itens)
elif quantidade == 0:
    print("\nRESUMO LISTA DE COMPRAS:\nVocê selecionou",quantidade,"itens")

input("\nPressione ENTER para sair...")