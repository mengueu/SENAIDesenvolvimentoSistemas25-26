# Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou.
#Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total em dias.

CigDia = int(input("Digite a quantidade de cigarros que você fuma por dia: "))
Anos = int(input("Digite há quantos anos você fuma: "))
Vida = (CigDia*(10/1440)*(Anos*365))

print(" ")
print ("Você perdeu cerca de",Vida,"dias de vida.")

print (" ")
input("Pressione ENTER para sair...")
