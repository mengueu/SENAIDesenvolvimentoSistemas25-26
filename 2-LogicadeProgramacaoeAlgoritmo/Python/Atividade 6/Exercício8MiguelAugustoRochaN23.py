#8: Gerenciamento de Lista
'''
Crie uma lista chamada biblioteca inicialmente com os livros:
"Dom Casmurro"
"1984"
Em seguida:
1. Adicione "O Senhor dos Anéis" no final da lista.
2. Insira "Orgulho e Preconceito" na primeira posição.
3. Remova o livro "1984".
4. Imprima a lista final.
'''

biblioteca = ['Dom Casmurro','1984']
biblioteca.append('O Senhor dos Anéis')
biblioteca.insert(0,'Orgulho e Preconceito')
biblioteca.remove('1984')
print("Sua biblioteca final está assim:",biblioteca)

input("\nPressione ENTER para sair...")
