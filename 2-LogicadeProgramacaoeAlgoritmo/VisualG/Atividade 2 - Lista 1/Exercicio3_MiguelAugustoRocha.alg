algoritmo "Exercicio 3"
var
Idade: inteiro
inicio
escreval ("Insira sua idade: ")
leia (Idade)
se (Idade > 18) e (Idade <= 70) entao
   escreval ("Vote obrigatóriamente")
   senao
        se (Idade >= 16) e (Idade <= 18) ou (Idade > 70) entao
        escreval ("Vote se quiser")
        senao
             se (Idade < 16) entao
             escreval ("Proibido votar")
             fimse
        fimse
fimse
fimalgoritmo
