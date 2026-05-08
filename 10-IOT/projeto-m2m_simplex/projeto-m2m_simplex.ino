int led = 13;
char comando;

void setup() {
  pinMode(led, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()){
    comando = Serial.read();

    if (comando == 'l'){
      digitalWrite(led, HIGH);
    }
    else if(comando == 'd'){
      digitalWrite(led, LOW);
    }
  }
}
