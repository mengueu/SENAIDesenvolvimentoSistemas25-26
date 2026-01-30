algoritmo "Exercício 1: Times de futebol"

var
time1,time2,time3: caractere
v1,em1,d1: inteiro
v2,em2,d2: inteiro
v3,em3,d3: inteiro
total1,total2,total3: inteiro
Npt1,Npt2,Npt3: inteiro

inicio
Escreva ("Qual o nome do time 1? ")
leia (time1)
Escreva ("Qual o nome do time 2? ")
leia (time2)
Escreva ("Qual o nome do time 3? ")
leia (time3)

escreval (" ")
Escreva ("Quantas vitórias o ",time1, " teve até agora? ")
leia (v1)
Escreva ("Quantos empates o ", time1, " teve até agora? ")
leia (em1)
Escreva ("Quantas derrotas o ", time1, " teve até agora? ")
leia (d1)
se ((v1+em1+d1) > 10) entao
escreval ("Só foram realizados 10 jogos.")
escreval ("Por favor tente novamente com a quantidade de jogos certa.")
fimalgoritmo
fimse

escreval (" ")
Escreva ("Quantas vitórias o ",time2, " teve até agora? ")
leia (v2)
Escreva ("Quantos empates o ", time2, " teve até agora? ")
leia (em2)
Escreva ("Quantas derrotas o ", time2, " teve até agora? ")
leia (d2)
se ((v2+em2+d2) > 10) entao
escreval ("Só foram realizados 10 jogos.")
escreval ("Por favor tente novamente com a quantidade de jogos certa.")
fimalgoritmo
fimse

escreval (" ")
Escreva ("Quantas vitórias o ",time3, " teve até agora? ")
leia (v3)
Escreva ("Quantos empates o ", time3, " teve até agora? ")
leia (em3)
Escreva ("Quantas derrotas o ", time3, " teve até agora? ")
leia (d3)
se ((v3+em3+d3) > 10) entao
escreval ("Só foram realizados 10 jogos.")
escreval ("Por favor tente novamente com a quantidade de jogos certa.")
fimalgoritmo
fimse


v1 <- (v1*3)
em1 <- (em1*1)
d1 <- (d1*0)
total1 <- (v1+em1+d1)

v2 <- (v2*3)
em2 <- (em2*1)
d2 <- (d2*0)
total2<- (v2+em2+d2)

v3 <- (v3*3)
em3 <- (em3*1)
d3 <- (d3*0)
total3 <- (v3+em3+d3)

escreval (" ")
Escreval ("Pontuação:")
escreval ((time1),":",(total1))
escreval ((time2),":",(total2))
escreval ((time3),":",(total3))

se ((total1 = total2) ou (total1 = total3) ou (total2 = total3)) entao
escreval ("Se dois ou mais times obtiverem a mesma pontuação, não há código para resolver isso")
escreval ("no momento.")
escreval ("Tente novamente.")
fimse

se ((total1 > total2) e (total1 > total3)) e ((total2 < total1) e (total2 > total3))entao
escreval (" ")
escreval ("Colocação:")
escreval (("1°lugar: "),time1)
escreval (("2°lugar: "),time2)
escreval (("3°lugar: "),time3)
senao
     se ((total1 > total2) e (total1 > total3)) e ((total3 < total1) e (total3 > total2))entao
     escreval (" ")
     escreval ("Colocação:")
     escreval (("1°lugar: "),time1)
     escreval (("2°lugar: "),time3)
     escreval (("3°lugar: "),time2)
     senao
          se ((total2 > total1) e (total2 > total3)) e ((total1 < total2) e (total1 > total3))entao
          escreval (" ")
          escreval ("Colocação:")
          escreval (("1°lugar: "),time2)
          escreval (("2°lugar: "),time1)
          escreval (("3°lugar: "),time3)
          senao
               se ((total2 > total1) e (total2 > total3)) e ((total3 < total2) e (total3 > total1))entao
               escreval (" ")
               escreval ("Colocação:")
               escreval (("1°lugar: "),time2)
               escreval (("2°lugar: "),time3)
               escreval (("3°lugar: "),time1)
               senao
                    se ((total3 > total1) e (total3 > total2)) e ((total2 < total3) e (total2 > total1))entao
                    escreval (" ")
                    escreval ("Colocação:")
                    escreval (("1°lugar: "),time3)
                    escreval (("2°lugar: "),time2)
                    escreval (("3°lugar: "),time1)
                    senao
                         se ((total3 > total1) e (total3 > total2)) e ((total1 < total3) e (total1 > total2))entao
                         escreval (" ")
                         escreval ("Colocação:")
                         escreval (("1°lugar: "),time3)
                         escreval (("2°lugar: "),time1)
                         escreval (("3°lugar: "),time2)
                         senao

                         fimse
                    fimse
                fimse
           fimse
     fimse
fimse
fimalgoritmo
