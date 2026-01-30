#Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar: soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba o
#resultado da operação solicitada.

numero = float(input("CALCULADORA\nDigite um número: "))
operacao = str(input("Digite qual operação deseja realizar: "))
numero2 = float(input("Digite outro número: "))

if operacao == "Divisão" or operacao =="divisão" or operacao =="/" and numero2==0:
    print("Erro. Não há como o divisor ser 0. Tente novamente com outro número.")
    input("Pressione ENTER para sair...")
    exit()
if operacao == "Adição" or operacao =="adição" or operacao =="Mais" or operacao =="mais" or operacao =="+":
    print("Seu resultado é",(numero + numero2))
elif operacao == "Subtração" or operacao =="subtração" or operacao =="Menos" or operacao =="menos" or operacao =="-":
    print("Seu resultado é",(numero - numero2))
elif operacao == "Multiplicação" or operacao =="multiplicação" or operacao =="Vezes" or operacao =="vezes" or operacao =="*":
    print("Seu resultado é",(numero * numero2))
elif operacao == "Divisão" or operacao =="divisão" or operacao =="/":
    print("Seu resultado é",(numero / numero2))

print(" ")
input("Pressione ENTER para sair...")
