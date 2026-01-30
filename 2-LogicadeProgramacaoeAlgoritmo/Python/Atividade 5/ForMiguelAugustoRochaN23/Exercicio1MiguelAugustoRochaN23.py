#Desenvolva um programa que solicite o sexo de 10 pessoas e imprima quantas pessoas são do sexo masculino e quantas são do sexo feminino(considerar m, M, f e F).

print("Precisamos saber qual é o sexo dos indivíduos.")

fem = 0
masc = 0

for i in range(10):
    sexo = str(input("Digite o sexo(m ou M para masculino e f ou F para feminino): "))
    if sexo == ('f') or sexo == ('F'):
        fem = fem+1
    elif sexo == ('m') or sexo == ('M'):
        masc = masc+1
if masc == 1:
    print("\nHá %d homem e %d mulheres." %(masc,fem))
elif fem == 1:
    print("\nHá %d homens e %d mulher." %(masc,fem))
else:
    print("\nHá %d homens e %d mulheres." % (masc,fem))

input("\nPressione ENTER para sair...")
