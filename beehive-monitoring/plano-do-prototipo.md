# Plano do protótipo e materiais

O que vamos montar, em que ordem, o que já existe no laboratório e o que precisa
ser comprado.

Os nomes em maiúsculas são as etiquetas das gavetas do laboratório.

## O que vamos montar

A AC5 e a AC6 pedem a montagem do protótipo com os componentes do laboratório e o
registro fotográfico para a avaliação qualitativa. O sistema completo está descrito
em `decisoes-do-projeto.md`, e o resumo é este:

Uma estação instalada na colmeia, com uma câmera apontada para a entrada e dois
sensores de temperatura e umidade, um dentro e um fora. A câmera captura sequências
curtas de imagens em horário fixo, e os sensores medem a cada três minutos. Tudo é
gravado num cartão microSD na própria placa, com data e hora vindas de um relógio de
tempo real. **O sistema não usa rede:** o cartão é recolhido uma vez por semana e as
imagens são analisadas depois, num computador, por um modelo que conta as abelhas
visíveis em cada janela. A alimentação é por painel solar com bateria.

## Etapas da montagem

Cinco etapas, da bancada até a colmeia:

1. **ESP32-WROVER-DEV gravando imagens JPEG no cartão**, alimentada por USB na bancada.
   É o núcleo do sistema e é onde a montagem costuma travar.
2. **Sensores e relógio ligados**, gravando o CSV no mesmo cartão. A foto da
   avaliação qualitativa da AC5 e da AC6 pode sair aqui.
3. **Agendamento e modo de baixo consumo**, com medição da corrente em cada estado
   para dimensionar o painel e a bateria.
4. **Painel solar, bateria e caixa vedada.**
5. **Instalação na colmeia** e início dos ensaios.

**Situação em 15 de setembro de 2026.** A etapa 2 foi cumprida em versão reduzida,
no Arduino Uno: o DHT11 e o DS1302 funcionam e geram o CSV na porta serial, com data,
hora, temperatura e umidade. O código está em `firmware/sensor_dht11_rtc/` e as fotos
em `assets/`.

O que essa versão ainda não faz é gravar no cartão, porque não há cartão nem leitor, e
usar a ESP32-WROVER-DEV, porque falta o cabo micro-USB. A etapa 1, que é a câmera
gravando imagens, continua bloqueada pelos mesmos três itens.

O Arduino Uno segue na lista justamente por isso: com ele dá para validar sensores,
relógio e formato do CSV em paralelo, sem depender da placa definitiva.

## Essencial

| Qtd | Item | Onde | Para quê |
|---|---|---|---|
| 1 | Placa ESP32-WROVER-DEV v1.6, com câmera OV2640 | Gaveta `ESP 32 CAM` | Placa principal do sistema. A câmera liga no conector flat |
| 1 | Arduino Uno R3 compatível, conversor CH340, com cabo USB-B | Caixa das placas azuis | Testar os sensores antes da ESP32-WROVER-DEV |
| 1 | Sensor DHT11 de 4 pinos, sem placa de módulo | Gaveta `MÓDULO DHT 11` | Temperatura e umidade, ponto interno. Exige o resistor de pull-up |
| 1 | Módulo MH-Real-Time Clock Modules-2, chip DS1302, sem bateria | Gaveta `MÓDULO REAL TIME CLOCK` | Data e hora nas medições |
| 1 | Display LCD 1602, pente de 16 pinos | Gaveta `LCD 1602` | Acompanhar as leituras durante a montagem |
| 1 | Módulo conversor I2C para LCD, chip PCF8574 | Gaveta `MÓDULO CONVERSOR P/ LCD 1602` | Ligar o display usando só dois pinos |
| 1 | Protoboard HIKARI HK-P100 | Caixa das protoboards | Montagem, e bornes para medir consumo depois |
| ~15 | Jumpers macho-fêmea | Caixa `MACHO-FÊMEA` | Ligar os módulos à placa |
| ~10 | Jumpers macho-macho | Caixa `MACHO-MACHO` | Ligações na protoboard |
| ~10 | Jumpers fêmea-fêmea | Caixa `FÊMEA-FÊMEA` | Reserva |

## Levar também

| Qtd | Item | Onde | Para quê |
|---|---|---|---|
| 4 | Resistores de 10 kΩ, faixas marrom, preto e laranja | Gaveteiro laranja, gaveta `10 KΩ` | Pull-up do DHT11, entre o VCC e a linha de dados |
| 1 | Barra de pinos macho/fêmea | Gaveta `BARRA DE PINOS MACHO/FÊMEA` | Adaptar conexões |

## O que o hardware na mão revelou

Três surpresas em relação ao plano inicial, todas verificadas com as peças na mão.

**A placa não é uma ESP32-CAM.** É uma **ESP32-WROVER-DEV v1.6**, com a câmera
OV2640 separada, que entra no conector flat. Ela tem micro-USB e conversor CH340C
embutidos, então grava firmware direto pelo cabo. Sai da lista de compras a base
ESP32-CAM-MB e o adaptador FTDI. A placa **não tem slot de cartão**, então entra um
módulo leitor de microSD avulso.

**O relógio é DS1302, não DS3231.** O módulo é o `MH-Real-Time Clock Modules-2`,
com pinos VCC, GND, CLK, DAT e RST. Ele não é I2C: usa três fios e três pinos
digitais. A biblioteca é a `Rtc by Makuna`, com a classe `ThreeWire`, e não a
`RTClib`. Esses módulos costumam trazer circuito de carga para bateria recarregável
LIR2032; com uma CR2032 comum, convém desligar a carga por software.

**O DHT11 é o sensor puro de 4 pinos**, não o módulo de 3 pinos. O módulo já vem
com resistor de pull-up embutido; o sensor puro não vem. É preciso um resistor de
10 kΩ entre o VCC e a linha de dados.

Falta conferir se o pente de 16 pinos do conversor I2C encaixa direto no LCD. Se
não encaixar, o display precisa ser soldado, e sem o conversor ele consome seis
pinos digitais em vez de dois.

## Precisa ser comprado

Nenhum destes itens foi encontrado nas gavetas.

### Libera a montagem de bancada

| Qtd | Item | Especificação | Por que |
|---|---|---|---|
| 1 | Cartão microSD | 32 GB, classe 10 | Todo o armazenamento é local. Sem ele a placa não grava imagem nem medição. Bloqueia a etapa 1. |
| 1 | Módulo leitor de microSD | SPI ou SD_MMC | A ESP32-WROVER-DEV não tem slot de cartão, só os pinos no header. Bloqueia a etapa 1. |
| 1 | Cabo micro-USB | com linhas de dados | Os cabos do laboratório são USB-B, dos Arduino, e não encaixam na placa. |
| 1 | Sensor de temperatura e umidade | DHT11, DHT22 ou equivalente | O método compara interior e exterior, o que exige dois pontos. Há só um módulo no laboratório. |
| 1 | Bateria CR2032 | moeda de lítio, 3 V | O suporte do módulo DS1302 veio vazio. Sem ela o relógio zera a cada vez que a energia cai, e a estação perde a hora no campo. |

### Permite instalar na colmeia

| Qtd | Item | Especificação | Por que |
|---|---|---|---|
| 1 | Painel solar | cerca de 3 W | A estação fica no apiário sem tomada. Os suportes de pilha do laboratório não sustentam operação prolongada. |
| 1 | Bateria 18650 | cerca de 2600 mAh, com proteção BMS | Mantém a captura entre as recargas e nos dias nublados. |
| 1 | Controlador de carga solar | para célula de lítio | Liga o painel à bateria sem danificar a célula. |
| 1 | Regulador de tensão | saída 5 V | Entrega tensão estável à placa e aos sensores. |
| 1 | Caixa vedada com prensa-cabo | uso externo | Protege a eletrônica da chuva e veda a passagem do cabo do sensor interno. |
| 1 | Suporte articulado | fixação da câmera | A câmera precisa ficar firme acima e à frente da entrada, com ângulo ajustável. |
| 1 | Capa ventilada | para o sensor interno | Deixa o ar passar e mantém as abelhas longe da eletrônica. |
| 1 | Cabo de quatro vias | para o sensor interno | Leva alimentação e dados do interior da colmeia até a placa do lado de fora. |

Ordem de urgência: os quatro primeiros são o que impede a montagem hoje. Do painel
solar em diante só é necessário quando a bancada estiver funcionando.

## Pinos da ESP32-WROVER-DEV

A troca de placa resolveu boa parte do aperto de pinos, mas três grupos continuam
indisponíveis.

A câmera, no mapeamento do WROVER-KIT, ocupa os GPIOs 4, 5, 18, 19, 21, 22, 23, 25,
26, 27, 34, 35, 36 e 39. Os pinos 16 e 17 são da PSRAM do módulo WROVER e não podem
ser usados. Os pinos `SD0`, `SD1`, `SD2`, `SD3`, `CMD` e `CLK` que aparecem no header
**não servem para o cartão**: são a interface da memória flash interna.

Sobram 2, 12, 13, 14, 15, 32 e 33, o que é suficiente:

| Função | Pino |
|---|---|
| Cartão microSD, modo 1-bit: CLK, CMD, D0 | 14, 15, 2 |
| DS1302: CLK, DAT, RST | 12, 13, 32 |
| DHT11: linha de dados | 33 |

Atenção ao GPIO 12: é pino de strapping e precisa estar em nível baixo no boot.
Se a linha ligada nele tiver resistor de pull-up, a placa não liga.

No código, o modelo da câmera é `CAMERA_MODEL_WROVER_KIT`, e não
`CAMERA_MODEL_AI_THINKER`, que é o que quase todo tutorial usa. Com o mapeamento
errado a câmera não inicializa.

## Não pegar

Estão no laboratório e parecem úteis, mas ficaram fora do escopo da primeira
versão, segundo `decisoes-do-projeto.md`:

- `MÓDULO SENSOR DE SOM KY-038`, porque áudio não entra nesta versão
- Célula de carga e `MÓDULO HX711`, porque o peso da colmeia está fora do escopo
- `SHIELD LORAWAN` e `SHIELD ETHERNET W5500`, porque o sistema é offline
- `ESP8266`, que não tem câmera
