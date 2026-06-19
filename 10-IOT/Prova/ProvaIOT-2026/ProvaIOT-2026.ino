#include <DHT11.h>

DHT11 dht11(A0);

const int ledVerde = 12;
const int ledVermelho = 11;
const int ledAr = 10;

unsigned long tempoAnterior = 0;
bool estadoAr = false;

void setup() {
    Serial.begin(9600);
    
    pinMode(ledVerde, OUTPUT);
    pinMode(ledVermelho, OUTPUT);
    pinMode(ledAr, OUTPUT);
}

void loop() {
    if (Serial.available() > 0) {
        char comando = Serial.read();
        // O site envia 'A'
        if (comando == 'A') {
            estadoAr = !estadoAr;
            digitalWrite(ledAr, estadoAr ? HIGH : LOW);
        }
    }

    unsigned long tempoAtual = millis();
    if (tempoAtual - tempoAnterior >= 500) {
        tempoAnterior = tempoAtual;

        float temperatura = dht11.readTemperature();

        if (temperatura != DHT11::ERROR_CHECKSUM && temperatura != DHT11::ERROR_TIMEOUT) {
            
            if (temperatura >= 22 && temperatura <= 26) {
                digitalWrite(ledVerde, HIGH);
                digitalWrite(ledVermelho, LOW);
                digitalWrite(ledAr, LOW);
            } else {
                digitalWrite(ledVerde, LOW);
                digitalWrite(ledVermelho, HIGH);
            }

            Serial.println(temperatura);
            
        } else {
            Serial.print("Erro no Sensor: ");
            Serial.println(DHT11::getErrorString(temperatura));
        }
    }
}