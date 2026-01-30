#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa deve perguntar o valor da casa a comprar, o salário e a
#quantidade de anos a pagar. O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o valor da prestação como sendo o valor da casa a
#comprar dividido pelo número de meses a pagar.

vCasa = float(input("Você está passando pela avaliação do banco.\nApós isso diremos se seu empréstimo será ou não aprovado.\nDigite qual o valor total da casa a se comprar: "))
salario = float(input("Digite qual o seu salário: "))
qAnos = float(input("Digite em quantos anos você deseja pagar: "))
qMes = qAnos*12 #Quantidade de meses
vMes = vCasa/qMes #Valor por mês

if vMes > salario*0.3:
    print(" ")
    print("Seu empréstimo não foi aprovado!")
else:
    print(" ")
    print("Seu empréstimo foi aprovado!\nSeu imóvel custará R$",vCasa,"dividido em",qMes," meses. \nCada parcela custará R$",vMes)
print(" ")
input("Pressione ENTER para sair...")
