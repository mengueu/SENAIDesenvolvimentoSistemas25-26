# Exercício 8: Escreva um programa que pergunte a quantidade de km percorrido por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.

qtdKM = float(input("Digite a quantidade de KM's que foram rodados após o carro ser alugado: "))
qtdDIA = int(input("Digite quantos dias se passaram após o carro ser alugado: "))
Preço = (qtdKM*0.15+qtdDIA*60)

print(" ")
print ("O preço total será de: R$",Preço)
print ("Sendo R$",qtdKM*0.15,"por KM e R$",qtdDIA*60,"por dia(s) usado(s).")

print(" ")
input("Pressione ENTER para sair...")
