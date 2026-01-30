#Crie um sistema que leia vários números e informe quantos números entre 100 e 200 foram digitados, o programa deve possuir um limite de 100
#repetições, mas quando o valor 0 (zero) for lido o programa deve cessar sua execução.

print("Digite qualquer número (máximo 100 vezes).\nSe quiser saber quantos números entre 100 e 200 você digitou, clique 0.")
print(" ")


n = []
entrecem = 0

for i in range(100):
    numero = int(input("Digite um número: "))
    if numero >= 100 and numero <= 200:
        entrecem = entrecem+1
        n.append(numero)
    elif numero == 0:
        if entrecem == 1:
            print("\nVocê digitou %d número entre 100 e 200. E foi: %s" % (entrecem,n))
        elif entrecem == 0:
            print("\nVocê digitou 0 números entre 100 e 200.")
        else:
            print("\nVocê digitou %d números entre 100 e 200. E foram: %s" % (entrecem,n))
        break

input("\nPressione ENTER para sair...")
    
        
    
