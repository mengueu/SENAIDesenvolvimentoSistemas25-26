#2. Verificação de Produtos em Estoque
'''
Verificar se um produto está disponível em um estoque usando dicionários.
a. Crie um dicionário chamado estoque com os seguintes produtos e
quantidades:
estoque = {
"mouse": 50,
"teclado": 30,
"monitor": 15,
"fone": 20
}
b. Peça ao usuário para digitar um produto.
c. Verifique se o produto existe no dicionário:
Se existir, mostre a quantidade disponível.
Se não existir, exiba: "Produto não encontrado!" .
'''

estoque = {"mouse": 50,"teclado": 30,"monitor": 15,"fone": 20}
while True:
    verificar = input("Digite o produto desejado: ")
    if verificar in estoque:
        print(f"Temos esse produto com {estoque[verificar]} unidades de estoque.")
        sair = input("\nDeseja sair? s/n: ")
        if sair == 's':
            break
    else:
        print("Não temos esse produto em estoque.")
        sair = input("\nDeseja sair? s/n: ")
        if sair == 's':
            break
input("\nPressione ENTER para fechar o programa..")
