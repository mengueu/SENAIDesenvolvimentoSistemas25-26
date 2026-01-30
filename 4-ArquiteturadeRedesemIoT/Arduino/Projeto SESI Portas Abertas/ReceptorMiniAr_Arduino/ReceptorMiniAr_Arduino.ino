#include <IRremote.h>

IRrecv irrecv(4); //Receptor IR
decode_results results;

void setup() {
  Serial.begin(9600);
  pinMode(2, OUTPUT); // Vermelho
  pinMode(3, OUTPUT); // Verde
  pinMode(10, OUTPUT); //Ventoinha
  digitalWrite(2, LOW);
  digitalWrite(3, LOW);
  digitalWrite(10, LOW);

  irrecv.enableIRIn(); // Inicia o receptor IR
  Serial.println("Receptor IR iniciado.");
}

void loop() {
  if (irrecv.decode(&results)) {
    Serial.print("Código recebido: 0x");
    Serial.println(results.value, HEX);

    // Receber DESLIGAR
    if (results.value == 0x1FE48B7) 
    {
      digitalWrite(10, HIGH);
      digitalWrite(3, HIGH);
      digitalWrite(2, LOW);
      Serial.println("AR-CONDICIONADO LIGADO");
    }
    
    // Receber LIGAR
    if (results.value == 0x1FE58A7) 
    {
      digitalWrite(10, LOW);
      digitalWrite(3, LOW);
      digitalWrite(2, HIGH);
      Serial.println("AR-CONDICIONADO DESLIGADO");
    }

    irrecv.resume(); // Espera novo comando
  }
}

