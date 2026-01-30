int LEDVmC = 13;
int LEDAm = 12;
int LEDVdC = 11;
int LEDVmP = 2;
int LEDVdP = 3;
char teclado;

void setup()
{
  Serial.begin(9600);
  pinMode(LEDVmC, OUTPUT); // Vermelho
  pinMode(LEDAm, OUTPUT); // Amarelo
  pinMode(LEDVdC, OUTPUT);  // Verde 
  pinMode(LEDVdP, OUTPUT); // Verde Pedestre
  pinMode(LEDVmP, OUTPUT); // Vermelho Pedestre
}

void apagar()
{
  digitalWrite(LEDVmC, LOW);
  digitalWrite(LEDAm, LOW);
  digitalWrite(LEDVdC, LOW);
  digitalWrite(LEDVmP, LOW);
  digitalWrite(LEDVdP, LOW);
}
void loop()
{
  digitalWrite(LEDVdC, HIGH);
  if (Serial.available() > 0){
    teclado = Serial.read();
    if (teclado == 'L' or teclado == 'l'){
      apagar();
      digitalWrite(LEDVmC, HIGH);
      digitalWrite(LEDVdP, HIGH);
      delay(6000);
      digitalWrite(LEDVmC, LOW);
      digitalWrite(LEDVdP, LOW);
    }
  }
}