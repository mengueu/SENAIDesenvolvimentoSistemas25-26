#include <IRremoteESP8266.h>
#include <IRsend.h>
#include <IRrecv.h>
#include <IRutils.h>

const uint16_t PINO_EMISSOR = 4;
const uint16_t PINO_RECEPTOR = 18;

IRsend irsend(PINO_EMISSOR);
IRrecv irrecv(PINO_RECEPTOR);
decode_results results;

void setup() {
  Serial.begin(9600);
  delay(1000);
  pinMode(19, OUTPUT); // LED1
  pinMode(21, OUTPUT); // LED2

  irsend.begin();
  irrecv.enableIRIn();

  Serial.println("Pronto para emitir IR");
}

void loop() {
  if (Serial.available() > 0) {
    char comando = Serial.read();

    // Emitir LIGAR
    if (comando == 'L' || comando == 'l') {
      irsend.sendNEC(0x1FE48B7, 32);
      Serial.println("AR-CONDICIONADO LIGADO");
      delay(2000);

      if (irrecv.decode(&results)) {
        Serial.println("Código IR recebido!");
        Serial.print("Código (HEX): 0x");
        Serial.println(results.value, HEX);
        Serial.print("Protocolo: ");
        switch (results.decode_type) {
          case decode_type_t::NEC:
            Serial.println("NEC");
            break;
          case decode_type_t::SONY:
            Serial.println("SONY");
            break;
          case decode_type_t::SAMSUNG:
            Serial.println("SAMSUNG");
            break;
          case decode_type_t::UNKNOWN:
            Serial.println("DESCONHECIDO");
            break;
          default:
            Serial.println("OUTRO");
            break;
        }

        // Verifica se é o código de DESLIGAR para simular
        if (results.decode_type == NEC && results.value == 0x1FE48B7) {
          digitalWrite(21, HIGH); // LED receptor desligando
          digitalWrite(19, LOW);
        }

        irrecv.resume();  // Pronto para próximo sinal
      }
    }

    // Emitir DESLIGAR
    if (comando == 'D' || comando == 'd') {
      irsend.sendNEC(0x1FE58A7, 32);
      Serial.println("AR-CONDICIONADO DESLIGADO");
      delay(2000);

      if (irrecv.decode(&results)) {
        Serial.println("Código IR recebido!");
        Serial.print("Código (HEX): 0x");
        Serial.println(results.value, HEX);
        Serial.print("Protocolo: ");
        switch (results.decode_type) {
          case decode_type_t::NEC:
            Serial.println("NEC");
            break;
          case decode_type_t::SONY:
            Serial.println("SONY");
            break;
          case decode_type_t::SAMSUNG:
            Serial.println("SAMSUNG");
            break;
          case decode_type_t::UNKNOWN:
            Serial.println("DESCONHECIDO");
            break;
          default:
            Serial.println("OUTRO");
            break;
        }

        // Verifica se é o código de DESLIGAR para simular
        if (results.decode_type == NEC && results.value == 0x1FE58A7) {
          digitalWrite(19, HIGH); // LED receptor desligando
          digitalWrite(21, LOW);
        }

        irrecv.resume();  // Pronto para próximo sinal
      }
    }
  }
}
