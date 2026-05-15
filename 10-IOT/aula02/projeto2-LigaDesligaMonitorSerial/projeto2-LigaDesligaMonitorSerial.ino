int led = 2;

void setup() {
  pinMode(led, OUTPUT);
  digitalWrite(led, LOW);
  Serial.begin(9600);
}

void loop() {
 
  if (Serial.available() > 0) {
    char comando = Serial.read();

    if (comando == 'L' || comando == 'l') {
      digitalWrite(led, HIGH);
      Serial.println("LED Ligado");
    }
   
    else if (comando == 'D' || comando == 'd') {
      digitalWrite(led, LOW);
      Serial.println("LED Desligado");
    }
  }
}