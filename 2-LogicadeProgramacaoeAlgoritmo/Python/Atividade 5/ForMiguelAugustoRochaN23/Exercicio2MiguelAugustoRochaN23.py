#Desenvolva um sistema que leia vários números positivos e imprima a média dos números digitados.

print("Digite a quantidade de números que quiser e então saiba a média.")

qtdNumeros = 0
resultado = 0

for i in range(10**20):
    numeros = int(input("Digite um número: "))
    resultado = resultado+numeros
    qtdNumeros = qtdNumeros+1
    continuar = str(input("Deseja saber a média? (s/n): "))
    if continuar == 's':
        media = resultado/qtdNumeros
        break
print("Sua média é:",media)

input("\nDigite ENTER para sair...")
        
