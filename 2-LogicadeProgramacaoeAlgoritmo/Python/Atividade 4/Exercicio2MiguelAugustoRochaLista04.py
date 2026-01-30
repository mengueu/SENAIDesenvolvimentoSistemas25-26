#Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
#Para os inferiores ou iguais, de 15%.

salario = float(input("Parabéns! Você ganhará um aumento de salário.\nDigite qual é seu salário: "))

if (salario > 1250):
    print("Seu salário teve um aumento de 10%.\nA partir de agora será R$", (salario*0.1)+salario)
else:
    print("Seu salário teve um aumento de 15%.\nA partir de agora será R$", (salario*0.15)+salario)
    
print(" ")
input("Pressione ENTER para sair...")
