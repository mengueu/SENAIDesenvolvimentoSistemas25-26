#Exercício 3: Escreva um programa que leia a quantidade de dias, horas, minutos e segundo do usuário. Calcule o total em segundos.

#1 dia = 86400 segundos
#1 horas = 3600 segundos
#1 minuto = 60 segundos
#1 segundo = 1 segundo

Dias = int(input("Digite a quantidade de dias do usuário: "))
Horas = int(input("Digite a quantidade de horas do usuário: "))
Minutos = int(input("Digite a quantidade de minutos do usuário: "))
Segundos = int(input("Digite a quantidade de segundos do usuário: "))
Total = Dias*86400+Horas*3600+Minutos*60+Segundos

print(" ")
print ("Você teve um total de:",Total,"segundos.")

print(" ")
input("Pressione ENTER para sair...")
