#10: Manipulação Avançada
'''
Dadas as listas:
frutas = ["Maçã", "Banana"]
hortifruti = ["Cenoura", "Abacaxi"]
1. Combine frutas e hortifruti em uma única lista.
2. Remova o último item da lista resultante e armazene-o em uma variável.
3. Ordene a lista final em ordem alfabética.
4. Imprima a lista ordenada e o item removido.
'''

frutas = ['Maçã', 'Banana']
hortifruti = ['Cenoura', 'Abacaxi']

listafinal = frutas+hortifruti
itemremovido = listafinal.pop(3)
listafinal.sort()
print("Esta é sua lista final:",listafinal,"\nE seu item removido é:",itemremovido)

input("\nPressione ENTER para sair...")

