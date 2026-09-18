/*
  Relogio DS1302 no Arduino Mega 2560.
  Primeira etapa da bancada de manutencao preditiva: carimbar cada
  medicao com data e hora, sem depender de rede.

  Ligacao:
    DS1302 VCC -> 5V
    DS1302 GND -> GND
    DS1302 CLK -> pino 5
    DS1302 DAT -> pino 4
    DS1302 RST -> pino 3

  Os pinos 0 e 1 ficam livres. Sao o RX e o TX, e qualquer fio
  neles impede a gravacao. Grave sempre com a placa sem fios.

  O DS1302 nao e I2C: usa tres fios e a biblioteca Rtc by Makuna,
  classe ThreeWire. A RTClib da Adafruit nao serve.

  Sem a bateria CR2032 no suporte, o relogio zera a cada vez que a
  alimentacao cai e volta para a hora da ultima gravacao.

  Pendencia conhecida: o modulo MH testado em 17/09/2026 contava
  cerca de seis vezes mais rapido que o tempo real. Ver
  perguntas-em-aberto.md.
*/

#include <ThreeWire.h>
#include <RtcDS1302.h>

// ordem dos pinos: DAT, CLK, RST
ThreeWire fios(4, 5, 3);
RtcDS1302<ThreeWire> rtc(fios);

void setup() {
  Serial.begin(9600);
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

  Serial.println("data_hora");
}

void loop() {
  delay(1000);

  RtcDateTime agora = rtc.GetDateTime();

  char data_hora[20];
  snprintf(data_hora, sizeof(data_hora), "%04u-%02u-%02u %02u:%02u:%02u",
           agora.Year(), agora.Month(), agora.Day(),
           agora.Hour(), agora.Minute(), agora.Second());

  Serial.println(data_hora);
}
