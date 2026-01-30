#Exercício 4: Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.

Salario = int(input("Digite seu salário: "))
PorcentagemAumento = int(input("Digite a porcentagem de aumento: "))
SalarioNovo = (Salario*PorcentagemAumento/100+Salario)
AumentoSalario = (SalarioNovo-Salario)

print(" ")
print("Seu salário novo é",SalarioNovo,"reais. Você obteve um aumento de",PorcentagemAumento,"porcento. \nResultando em",AumentoSalario,"reais de aumento.")

print(" ")
input("Pressione ENTER para sair...")
