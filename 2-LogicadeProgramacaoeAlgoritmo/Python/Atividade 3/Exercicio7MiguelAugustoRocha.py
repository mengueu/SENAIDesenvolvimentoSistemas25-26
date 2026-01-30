#Exercício 7: Escreva um programa que converta uma temperatura digitada em oC para oF. A fórmula para essa conversão é: F = 9 / 5 x C + 32

tC = int(input("Digite a quantidade de temperatura em graus CELSIUS: "))
F = (9/5*tC+32)

print(" ")
print (tC,"graus celsius são ",F,"graus fahrenheit.")

print(" ")
input("Pressione ENTER para sair...")
