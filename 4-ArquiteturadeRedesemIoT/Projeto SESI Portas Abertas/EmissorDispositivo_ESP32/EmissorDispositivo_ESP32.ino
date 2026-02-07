// USB Direita: COM8
// USB Esquerda: 

#include <IRremoteESP8266.h>
#include <IRsend.h>

IRsend irsend(4); //Emissor IR

void setup() {
  pinMode(5, INPUT_PULLUP); //Botão ligar
  pinMode(18, INPUT_PULLUP); //Botão desligar
  Serial.begin(9600);
  irsend.begin(); //Inicia o emissor
  delay(2000);
}

void loop() {
  if (Serial.available()) {
    char comando = Serial.read();
    
    // Emitir LIGAR
    if (comando == 'L' || comando == 'l') {
      irsend.sendNEC(0x1FE48B7, 32);
      Serial.println("AR-CONDICIONADO LIGADO");
      delay(2000);
    }

    // Emitir DESLIGAR
    if (comando == 'D' || comando == 'd') {
      irsend.sendNEC(0x1FE58A7, 32);
      Serial.println("AR-CONDICIONADO DESLIGADO");
      delay(2000);
    }
  }

  //liga com botão
  if (digitalRead(5) == LOW) {
    irsend.sendNEC(0x1FE48B7, 32);
    Serial.println("AR-CONDICIONADO LIGADO");
    delay(2000);
  }

  //desliga com botão
  if (digitalRead(18) == LOW) {
    irsend.sendNEC(0x1FE58A7, 32);
    Serial.println("AR-CONDICIONADO DESLIGADO");
    delay(2000);
}