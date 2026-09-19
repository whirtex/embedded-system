/*
  Cadeia de aquisicao na ESP32-WROVER-DEV.
  Substitui a bancada do Arduino Mega: a hora vem da internet por NTP,
  entao o modulo DS1302 sai do projeto. O DS1302 MH testado em 17 e 18
  de setembro de 2026 contava exatamente seis vezes mais rapido que o
  tempo real, e sem bateria voltava para a hora da compilacao a cada
  religamento.

  Este sketch ja emite o CSV no formato final. Os sensores que ainda
  nao chegaram saem como campo vazio, e cada um vai substituindo o
  proprio campo conforme for montado, numa cadeia que ja roda.

  Ligacao prevista:
    DHT11 DADOS      -> GPIO 4    (provisorio, sai quando o DS18B20 chegar)
    DS18B20 DADOS    -> GPIO 5    (1-Wire, com resistor de 4,7 kOhm para 3,3 V)
    ADXL345 e INA219 -> GPIO 21 SDA, GPIO 22 SCL
    Tacometro cooler -> GPIO 18   (com resistor de 10 kOhm para 3,3 V)

  O tacometro entrega DOIS pulsos por volta, padrao de cooler de PC.

  Rotulagem pela porta serial, durante o ensaio:
    u B          troca a unidade para B
    c atrito     troca a condicao para atrito
    ?            mostra o estado atual

  Sem isso os dados nao servem para classificar: cada linha precisa
  saber de qual cooler veio e sob qual falha foi gravada.
*/

#include <WiFi.h>
#include <time.h>
#include "DHT.h"

// ---------- preencher antes de gravar ----------
const char* WIFI_SSID  = "COLOQUE_A_REDE_AQUI";
const char* WIFI_SENHA = "COLOQUE_A_SENHA_AQUI";
// -----------------------------------------------

#define PINO_DHT 4
#define TIPO_DHT DHT11
DHT dht(PINO_DHT, TIPO_DHT);

// fuso de Brasilia, sem horario de verao
const long  FUSO_SEGUNDOS = -3 * 3600;
const char* SERVIDOR_NTP  = "pool.ntp.org";

const unsigned long INTERVALO_MS = 3000;
unsigned long ultimaLeitura = 0;

bool horaValida = false;

char unidade[8]  = "A";
char condicao[24] = "normal";

void conectarWiFi() {
  Serial.print("conectando em ");
  Serial.println(WIFI_SSID);

  WiFi.mode(WIFI_STA);
  WiFi.begin(WIFI_SSID, WIFI_SENHA);

  unsigned long limite = millis() + 15000;
  while (WiFi.status() != WL_CONNECTED && millis() < limite) {
    delay(300);
    Serial.print(".");
  }
  Serial.println();

  if (WiFi.status() != WL_CONNECTED) {
    Serial.println("# sem Wi-Fi: o carimbo vai contar a partir do boot");
    return;
  }

  Serial.print("# Wi-Fi ok, IP ");
  Serial.println(WiFi.localIP());

  configTime(FUSO_SEGUNDOS, 0, SERVIDOR_NTP);

  struct tm agora;
  if (getLocalTime(&agora, 10000)) {
    horaValida = true;
    Serial.println("# hora sincronizada por NTP");
  } else {
    Serial.println("# NTP nao respondeu: o carimbo vai contar a partir do boot");
  }
}

// Devolve o carimbo. Com NTP, data e hora reais. Sem NTP, segundos
// desde o boot, marcados com o prefixo boot+ para nao se passarem
// por hora real dentro do CSV.
void carimbo(char* destino, size_t tamanho) {
  if (horaValida) {
    struct tm agora;
    if (getLocalTime(&agora, 100)) {
      strftime(destino, tamanho, "%Y-%m-%d %H:%M:%S", &agora);
      return;
    }
  }
  snprintf(destino, tamanho, "boot+%lu", millis() / 1000);
}

void lerComandos() {
  if (!Serial.available()) return;

  String linha = Serial.readStringUntil('\n');
  linha.trim();
  if (linha.length() == 0) return;

  if (linha == "?") {
    Serial.print("# unidade=");
    Serial.print(unidade);
    Serial.print(" condicao=");
    Serial.println(condicao);
    return;
  }

  if (linha.startsWith("u ")) {
    linha.substring(2).toCharArray(unidade, sizeof(unidade));
    Serial.print("# unidade agora e ");
    Serial.println(unidade);
    return;
  }

  if (linha.startsWith("c ")) {
    linha.substring(2).toCharArray(condicao, sizeof(condicao));
    Serial.print("# condicao agora e ");
    Serial.println(condicao);
    return;
  }

  Serial.println("# comandos: 'u <unidade>', 'c <condicao>', '?'");
}

void setup() {
  Serial.begin(115200);
  delay(300);

  dht.begin();
  conectarWiFi();

  // As linhas de comentario comecam com # para o pandas ignorar
  // com comment='#' na hora de ler o CSV.
  Serial.println("data_hora,unidade,condicao,temp_ar_c,temp_amb_c,delta_t_c,"
                 "corrente_ma,rpm,vib_rms_x,vib_rms_y,vib_rms_z");
}

void loop() {
  lerComandos();

  if (millis() - ultimaLeitura < INTERVALO_MS) return;
  ultimaLeitura = millis();

  char data_hora[32];
  carimbo(data_hora, sizeof(data_hora));

  // Provisorio: o DHT11 ocupa a coluna do ar ambiente ate os dois
  // DS18B20 chegarem. Ele tem resolucao de 1 grau, o que e grosseiro
  // demais para a diferenca que o metodo mede, entao e so andaime.
  float temp_amb = dht.readTemperature();

  Serial.print(data_hora);
  Serial.print(",");
  Serial.print(unidade);
  Serial.print(",");
  Serial.print(condicao);
  Serial.print(",");
  Serial.print("");                          // temp_ar_c    DS18B20
  Serial.print(",");
  if (!isnan(temp_amb)) Serial.print(temp_amb, 1);
  Serial.print(",");
  Serial.print("");                          // delta_t_c    calculado
  Serial.print(",");
  Serial.print("");                          // corrente_ma  INA219
  Serial.print(",");
  Serial.print("");                          // rpm          tacometro
  Serial.print(",");
  Serial.print("");                          // vib_rms_x    ADXL345
  Serial.print(",");
  Serial.print("");                          // vib_rms_y    ADXL345
  Serial.print(",");
  Serial.println("");                        // vib_rms_z    ADXL345
}
