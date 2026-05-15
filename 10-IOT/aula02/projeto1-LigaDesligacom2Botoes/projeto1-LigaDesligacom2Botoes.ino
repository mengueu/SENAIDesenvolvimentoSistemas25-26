int botao01 = 6;
int botao02 = 7;
int led = 2;

void setup()
{
  pinMode(botao01, INPUT_PULLUP);
  pinMode(botao02, INPUT_PULLUP);
  pinMode(led, OUTPUT);
 
  digitalWrite(led, LOW);
  Serial.begin(9600);
}

void loop()
{
  int Liga = digitalRead(botao01);
  int Desliga = digitalRead(botao02);
  if (Liga == LOW) {
    digitalWrite(led, HIGH);
  }
  if (Desliga == LOW) {
    digitalWrite(led, LOW);
  }
}