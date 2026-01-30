#3: Acesso a Listas Aninhadas
'''
Dada a lista dados = ["Python", [10, 20, 30], "Academy"] , faça:
1. Acesse e imprima o segundo elemento da lista interna [10, 20, 30] .
2. Substitua "Academy" por "Programming" na lista principal.
3. Imprima a lista final.
'''

dados = ['Python',[10,20,30],'Academy']
print("O segundo elemento da lista interna [10,20,30] é:",dados[1][1])
dados[0] = 'Academy'
dados[2] = 'Python'
print("Após as modificações dos índices a lista final é:",dados)

input("\nPressione ENTER para sair...")
