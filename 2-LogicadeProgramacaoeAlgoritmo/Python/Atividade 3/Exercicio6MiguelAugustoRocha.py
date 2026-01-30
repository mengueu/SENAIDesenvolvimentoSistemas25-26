#Exercício 6: Escreva um programa que calcule o tempo de viagem de carro. Pergunte a distância a percorrer e a velocidade média para a viagem.

Distancia = float(input("Digite a distância, em KM, que você irá viajar: "))
VM = int(input("Digite a velocidade média que você pretende viajar: "))
Tempo = (Distancia/VM)

print(" ")
print ("Você viajará por",Tempo,"hora(s).")

print(" ")
input("Pressione ENTER para sair...")

