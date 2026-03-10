#include <Arduino.h>

void setup() {
  pinMode(13, OUTPUT); // Porta saída
  Serial.begin(9600); // Inicializando comunicação serial
}

void loop() {
  if (Serial.available() > 0){ // Se tiver alguma interação com o serial...
    char comando = Serial.read(); // Lê a porta
    if (comando == 'l'){ // Aspas simples, se não não funciona
      digitalWrite(13, HIGH);
    }
    if (comando == 'd'){
      digitalWrite(13, LOW);
    }
  }
}

// Confaigurando a porta pelo cmd:
// Mostrar informações da porta: mode 'porta' (com3, no caso)
// Definindo parâmetros: mode com3 9600, n, 8

/* Transmitindo o comando pelo cmd: 
    - echo l > COM3 
    - echo d > COM3
*/ 