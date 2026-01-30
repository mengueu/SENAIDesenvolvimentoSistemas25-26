#Crie um sistema que exiba a tabuada simples de um número digitado pelo usuário.

tabuada = int(input("Digite o número que deseja saber a tabuada: "))
multiplicador = 0

print(" ")
while multiplicador <= 10:
    resultado = tabuada*multiplicador
    print("%d*%d = %d" %(tabuada, multiplicador, resultado))
    multiplicador = multiplicador+1

print(" ")
input("Pressione ENTER para sair...")
