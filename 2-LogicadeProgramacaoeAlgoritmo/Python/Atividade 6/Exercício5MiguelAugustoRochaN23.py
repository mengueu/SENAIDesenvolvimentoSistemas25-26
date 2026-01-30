#5: Percorrendo Listas com for e enumerate()
'''
Dada a lista frutas = ["Maçã", "Banana", "Morango"] , use um loop for com enumerate() para
imprimir cada fruta seguida de seu índice, no formato:
Índice X: Fruta Y .
'''

frutas = ["Maçã", "Banana", "Morango"]
for indice,listadefrutas in enumerate(frutas):
    print(f'Índice: {indice}, Fruta: {listadefrutas}')

input("\nPressione ENTER para sair...")
