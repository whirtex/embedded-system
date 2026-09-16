/*
  DHT11 e relogio DS1302 no Arduino Uno.
  Gera na porta serial o CSV que a estacao vai gravar no cartao.

  Ligacao:
    DHT11 VCC   -> 5V
    DHT11 DADOS -> pino 2
    DHT11 GND   -> GND
    resistor de 10 kOhm entre VCC e DADOS

    DS1302 VCC -> 5V
    DS1302 GND -> GND
    DS1302 CLK -> pino 5
    DS1302 DAT -> pino 4
    DS1302 RST -> pino 3

  O DS1302 nao e I2C: usa tres fios e a biblioteca Rtc by Makuna.
  Sem a bateria CR2032 no suporte, o relogio zera a cada vez que a
  alimentacao cai e volta para a hora da ultima gravacao.
*/

#include "DHT.h"
#include <ThreeWire.h>
#include <RtcDS1302.h>

#define PINO_DHT 2
#define TIPO_DHT DHT11

DHT dht(PINO_DHT, TIPO_DHT);

// ordem dos pinos: DAT, CLK, RST
ThreeWire fios(4, 5, 3);
RtcDS1302<ThreeWire> rtc(fios);

void setup() {
  Serial.begin(9600);
  dht.begin();
  rtc.Begin();

  RtcDateTime compilado = RtcDateTime(__DATE__, __TIME__);

  if (rtc.GetIsWriteProtected()) {
    rtc.SetIsWriteProtected(false);
  }
  if (!rtc.GetIsRunning()) {
    rtc.SetIsRunning(true);
  }
  if (!rtc.IsDateTimeValid() || rtc.GetDateTime() < compilado) {
    rtc.SetDateTime(compilado);
  }

  Serial.println("data_hora,temperatura_c,umidade_pct");
}

void loop() {
  delay(3000);

  RtcDateTime agora = rtc.GetDateTime();
  float umidade = dht.readHumidity();
  float temperatura = dht.readTemperature();

  if (isnan(umidade) || isnan(temperatura)) {
    Serial.println("erro na leitura do sensor");
    return;
  }

  char data_hora[20];
  snprintf(data_hora, sizeof(data_hora), "%04u-%02u-%02u %02u:%02u:%02u",
           agora.Year(), agora.Month(), agora.Day(),
           agora.Hour(), agora.Minute(), agora.Second());

  Serial.print(data_hora);
  Serial.print(",");
  Serial.print(temperatura, 1);
  Serial.print(",");
  Serial.println(umidade, 1);
}
