// Arduíno LED
int led = 2;

void setup() {
  pinMode(led, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char comando = Serial.read();

    if (comando == 'L') {
      digitalWrite(led, HIGH);
    }
    else if (comando == 'D') {
      digitalWrite(led, LOW);
    }
  }
}