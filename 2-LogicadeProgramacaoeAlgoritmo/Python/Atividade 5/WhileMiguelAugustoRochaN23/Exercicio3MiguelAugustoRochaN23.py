#Crie um sistema que fique em looping solicitando números, o sistema deve criar um totalizador de números pares, quando o usuário digitar um numero
#negativo o sistema deve encerrar(break) e exibir o totalizador de números pares.

print("Digite qualquer número que farei a soma de todos os que são pares.\nQuando quiser saber o resultado, digite um número negativo.")
print(" ")

totalizador = 0

while True:
    numero = int(input("Digite um número: "))
    if numero < 0:
        break
    elif numero%2 == 0:
        totalizador = numero+totalizador
    elif numero%2 == 1:
        totalizador = totalizador+0
        
print("Sua soma de números pares é igual a:", totalizador)

print(" ")
input("Pressione ENTER para sair...")
        
    
