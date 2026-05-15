// Arduíno Botão

int botao01 = 6;
int botao02 = 7;

void setup() {
  pinMode(botao01, INPUT_PULLUP);
  pinMode(botao02, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop() {
  if (digitalRead(botao01) == LOW) {
    Serial.print('L');
    delay(200);
  }

  if (digitalRead(botao02) == LOW) {
    Serial.print('D');
    delay(200);
  }
}