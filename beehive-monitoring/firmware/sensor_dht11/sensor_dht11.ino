/*
  Leitura do DHT11 no Arduino Uno.
  Primeiro teste de bancada do projeto de monitoramento de colmeias.

  Ligacao:
    DHT11 VCC   -> 5V
    DHT11 DADOS -> pino 2
    DHT11 GND   -> GND
    resistor de 10 kOhm entre VCC e DADOS

  O DHT11 usado e o sensor puro de 4 pinos, sem resistor embutido.
*/

#include "DHT.h"

#define PINO_DHT 2
#define TIPO_DHT DHT11

DHT dht(PINO_DHT, TIPO_DHT);

void setup() {
  Serial.begin(9600);
  Serial.println("Lendo o DHT11...");
  dht.begin();
}

void loop() {
  delay(3000);

  float umidade = dht.readHumidity();
  float temperatura = dht.readTemperature();

  if (isnan(umidade) || isnan(temperatura)) {
    Serial.println("Nao consegui ler o sensor");
    return;
  }

  Serial.print("Temperatura: ");
  Serial.print(temperatura);
  Serial.print(" C   Umidade: ");
  Serial.print(umidade);
  Serial.println(" %");
}
