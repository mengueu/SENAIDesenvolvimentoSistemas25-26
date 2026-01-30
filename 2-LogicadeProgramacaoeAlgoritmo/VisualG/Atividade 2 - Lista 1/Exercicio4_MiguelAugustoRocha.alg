algoritmo "Exercicio 4"
var
Valor1, Valor2, Media: real
inicio
escreval ("Insira o valor da sua primeira nota: ")
leia (Valor1)
escreval ("Insira o valor da sua segunda nota: ")
leia (Valor2)
Media <- (Valor1+Valor2)/2
se (Media >= 6) entao
   escreval ("Sua média é", Media, " você está aprovado!")
   senao
   escreval ("Sua média é", Media, " você não está aprovado!")
fimse
fimalgoritmo
