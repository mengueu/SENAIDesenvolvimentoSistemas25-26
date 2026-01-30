#Exercício 5: Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.

Mercadoria = float(input("Digite o valor da mercadoria: "))
Desconto = int(input("Digite a porcentagem de desconto: "))
desconto = (Mercadoria*Desconto/100)
PreçoFinal = (Mercadoria-desconto)

print(" ")
print ("Sua mercadoria custará: R$",PreçoFinal)
print ("O desconto é: R$",desconto)

print(" ")
input("Pressione ENTER para sair...")
