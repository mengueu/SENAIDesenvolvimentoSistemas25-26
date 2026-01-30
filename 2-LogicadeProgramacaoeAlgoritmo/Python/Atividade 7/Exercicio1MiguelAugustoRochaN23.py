#1. Criar um sistema simples de cadastro de alunos usando dicionários.
'''
a. Crie um dicionário vazio chamado alunos .
b. Peça ao usuário para digitar:
Nome
Idade
Nota
c. Adicione esses dados ao dicionário alunos .
d. Imprima o dicionário completo.
'''

alunos = {}
alunoNome = input("Insira o nome: ")
alunoIdade = input("Insira a idade: ")
alunoNota = input("Insira a nota: ")

alunos.update({'Nome':alunoNome})
alunos.update({'Idade':alunoIdade})
alunos.update({'Nota':alunoNota})

print("\nCadastro realizado com sucesso!\n",alunos)

input("\nPressione ENTER para fechar o programa...")