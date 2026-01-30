#7: Lista de Compras Simples
'''
Crie uma lista chamada compras que represente uma lista de compras de
supermercado. A lista deve conter os seguintes itens:
"Maçã"
"Leite"
"Pão"
"Ovos"
Em seguida:
1. Imprima a lista completa.
2. Adicione o item "Arroz" no final da lista.
3. Remova o item "Pão" da lista.
4. Imprima a lista atualizada.
'''

lista = ['Maçã','Leite','Pão','Ovos']
print("A lista completa é:",lista)
lista.append('Arroz')
del lista[2]
print("Essa é a lista completa após as modificações:",lista)

input("\nPressione ENTER para sair...")
