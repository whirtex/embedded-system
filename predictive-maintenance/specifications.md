# Especificações técnicas

Estas são as especificações preliminares para o protótipo de manutenção preditiva. Os pontos que ainda dependem do enunciado ou da orientação do professor estão indicados no texto.

## 1. Controlador e comunicação

- A placa principal recomendada é um ESP8266 ou um ESP32-CAM.
- Também há Arduino Uno e Arduino Mega disponíveis, mas essas placas têm menos recursos de comunicação.
- O modelo exato da placa deve ser confirmado antes da montagem.
- A comunicação pode usar Wi-Fi, Ethernet ou LoRa.
- Para a primeira versão, recomenda-se usar Wi-Fi, pois essa opção simplifica o protótipo.

## 2. Atuador ou máquina de teste

- O motor de passo disponível está identificado como modelo 28BYJ-48. O modelo deve ser confirmado.
- Também há um driver para acionar o motor.
- O servomotor SG90 pode ser usado como alternativa.
- Antes da montagem, ainda é preciso definir:
  - como o motor será fixado;
  - qual carga será aplicada;
  - como será simulada uma condição de falha;
  - qual componente será monitorado;
  - qual procedimento será usado nos testes.

## 3. Sensores disponíveis

- DHT11 para temperatura e umidade;
- célula de carga de 50 kg;
- HX711, que faz a amplificação do sinal da célula de carga;
- KY-038 para detecção de som;
- sensor ultrassônico;
- sensor de inclinação SW-520D;
- sensor de luz LDR;
- sensor infravermelho;
- sensor PIR;
- módulos RF;
- módulo de relógio de tempo real;
- potenciômetros e botões.

## 4. Sensores e itens ainda não identificados

Os itens abaixo não foram identificados entre os componentes disponíveis na faculdade. A necessidade de cada um deve ser confirmada com o professor:

- acelerômetro para medir vibração, como MPU6050, ADXL345 ou um sensor industrial;
- sensor de corrente, como ACS712 ou INA219;
- fonte regulada de 5 V;
- suporte mecânico para o motor;
- elemento de carga ou transmissão mecânica;
- gabinete ou caixa de proteção;
- instrumento para calibrar e validar as medições.

O KY-038 pode servir como indicador experimental de ruído, mas não substitui um acelerômetro para medir vibração de forma confiável.

## 5. Saídas e alertas

Os componentes disponíveis incluem:

- display LCD 1602;
- LEDs comuns e LEDs RGB;
- buzzer;
- módulo relé;
- displays de sete segmentos.

Ainda é preciso decidir se o sistema deverá:

- apenas emitir um alerta;
- desligar automaticamente o motor;
- mostrar os valores no LCD;
- enviar os dados para um dashboard;
- enviar uma mensagem para um celular ou computador.

## 6. Alimentação elétrica

- Há conectores e suportes para pilhas AA entre os componentes disponíveis na faculdade.
- Ainda não foi confirmada uma fonte regulada capaz de alimentar a placa, os sensores e o motor.
- A tensão de alimentação de cada componente precisa ser definida.
- A alimentação do motor deve ser separada ou dimensionada corretamente para evitar que o controlador seja reiniciado.
- O protótipo não deve usar tensão da rede elétrica sem proteção e autorização do professor.

## 7. Montagem elétrica

Para a montagem, estão disponíveis:

- protoboards;
- jumpers e fios;
- resistores;
- capacitores;
- transistores;
- diodos;
- conectores;
- módulos de expansão.

O projeto deverá registrar o esquema elétrico, a pinagem e a identificação dos cabos.

## 8. Software

O repositório ainda não possui código. As seguintes decisões precisam ser tomadas:

- ambiente de desenvolvimento: Arduino IDE ou PlatformIO;
- linguagem de programação;
- frequência de amostragem dos sensores;
- método de filtragem dos sinais;
- cálculo de médias, picos, RMS ou outras características;
- método de identificação de anomalias;
- uso de limites fixos ou aprendizado de máquina;
- protocolo de comunicação: MQTT ou HTTP;
- local de armazenamento dos dados;
- dashboard ou outra interface de acompanhamento;
- formato dos registros;
- procedimento de treinamento e validação do modelo.

Como ponto de partida experimental, a literatura selecionada sugere calcular características no domínio do tempo e da frequência, como RMS e FFT, e comparar uma abordagem por limites com um método leve de detecção de anomalias. Essa escolha ainda depende do sensor de vibração, da capacidade do controlador e da quantidade de dados obtida.

## 9. Dados e validação

Para avaliar o sistema de manutenção preditiva, será necessário obter:

- dados em condição normal;
- dados com falhas ou anomalias controladas;
- registro do momento em que cada falha ocorreu;
- quantidade mínima de amostras;
- critérios para classificar uma previsão como correta;
- procedimento para repetir os testes.

Os registros também deverão identificar o equipamento, o estado operacional, a carga aplicada, a data e hora, a frequência de amostragem, as unidades e qualquer intervenção realizada. Os dados usados para ajustar limites ou treinar modelos não deverão ser reutilizados como conjunto final de teste.

Não foram identificados entre os componentes disponíveis na faculdade uma máquina industrial, um conjunto de falhas controladas ou uma base de dados pronta. Essa definição deve ser confirmada com o professor.

## 10. Itens para confirmar ou providenciar

1. Sensor de vibração.
2. Sensor de corrente.
3. Fonte regulada.
4. Estrutura mecânica para fixar o motor.
5. Método para criar as falhas.
6. Frequência de amostragem.
7. Método de detecção: limites ou aprendizado de máquina.
8. Forma de armazenar e visualizar os dados.
9. Necessidade de desligamento automático por relé.
10. Necessidade de gabinete e proteção física.

## 11. Rastreabilidade acadêmica

- Yousuf et al. e Mohammed et al.: arquitetura de sensores, comunicação e monitoramento de motores.
- Kolok et al.: ESP32, sensores MEMS, RMS, FFT e detecção de anomalias.
- Meitz et al.: organização do fluxo completo de manutenção preditiva.
- Gupta et al.: limpeza, rotulagem e avaliação de dados reais de vibração.
- Burmeister et al.: interpretação das previsões e apoio à decisão.

Os metadados completos estão em `references.bib`, e a relação detalhada entre cada artigo e o projeto está em `reference-contributions.md`.
