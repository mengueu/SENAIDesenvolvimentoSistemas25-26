algoritmo "Exercício 3: Multiplicador 2"

var
numero: inteiro
numeromenos1: inteiro
numeromais1: inteiro
inicio
escreva("Digite um número inteiro: ")
leia (numero)

numeromais1 <- numero+1
numeromenos1 <- numero-1

se (numeromais1=0) ou (numeromenos1=0) ou (numero =0)entao
escreval ("Um dos números resultará em 0, resultando em falha.")
escreval ("Tente novamente com outra combinação.")
fimalgoritmo
fimse

escreval ("Te darei a tabuada dele, seu antecessor e sucessor:")
escreval (" ")
escreval (("A tabuada de"),numero,(" é:"))
para numero de numero ate numero*10 passo numero faca
escreva (numero)
fimpara

escreval (" ")
escreval (" ")
escreval ("A tabuada de seu sucessor de é: ")
para numeromais1 de numeromais1 ate numeromais1*10 passo numeromais1 faca
escreva (numeromais1)
fimpara

escreval (" ")
escreval (" ")
escreval ("A tabuada de seu antecessor de é: ")
para numeromenos1 de numeromenos1 ate numeromenos1*10 passo numeromenos1 faca
escreva (numeromenos1)
fimpara

fimalgoritmo
