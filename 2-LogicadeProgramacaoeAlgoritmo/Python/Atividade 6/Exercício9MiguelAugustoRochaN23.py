#9: Análise de Lista
'''
Dada a lista notas = [7.5, 8.0, 6.5, 9.0, 8.0, 7.5] :
1. Conte quantas vezes a nota 8.0 aparece.
2. Encontre a posição da primeira ocorrência de 7.5.
3. Identifique a menor e a maior nota da lista.
'''

notas = [7.5, 8.0, 6.5, 9.0, 8.0, 7.5]
print("A nota 8.0 aparece",notas.count(8.0),"vezes.")
print("A posição da primeira ocorrência de 7.5 foi o índice",notas.index(7.5))
print("A menor nota é",min(notas),"e a maior é",max(notas))

input("\nPressione ENTER para sair...")
