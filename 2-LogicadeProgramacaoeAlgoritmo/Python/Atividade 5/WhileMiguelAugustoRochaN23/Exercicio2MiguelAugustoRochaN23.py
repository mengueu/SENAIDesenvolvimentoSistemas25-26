#Crie um sistema que realize o calculo da média de 5 números digitados pelo usuário.

print("Farei a média de 5 números para você.")

limitador = 1
numeroAnterior = 0

while limitador <= 5:
    proxNumero = float(input("Digite o %d° número: "%limitador))
    numeroAnterior = numeroAnterior+proxNumero
    limitador = limitador+1
media = numeroAnterior/5

print(" ")
print("A média dos números digitados é:", media)

print(" ")
input("Pressione ENTER para sair...")
