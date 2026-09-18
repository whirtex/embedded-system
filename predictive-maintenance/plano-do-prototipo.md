# Plano do protótipo e materiais

O que vamos montar, em que ordem, o que já existe no laboratório e o que precisa ser
comprado.

Os nomes em maiúsculas são as etiquetas das gavetas do laboratório.

## O que vamos montar

O sistema completo mede três grandezas em um aparelho de ar-condicionado em operação
contínua: **vibração**, **corrente elétrica** e **temperatura**. Um microcontrolador
lê os sensores no próprio equipamento, calcula características no tempo e na
frequência, e envia as medições para uma aplicação remota, que compara com a linha de
base saudável e informa qual medição desviou.

Os pontos de instalação no aparelho estão em `assets/instalacao-sensores-ac.png`. As
decisões e as dúvidas em aberto estão em `perguntas-em-aberto.md`.

## Etapas da montagem

1. **Sensores lendo na bancada**, com o microcontrolador alimentado por USB. Cada
   sensor validado isoladamente antes de juntar.
2. **Aquisição contínua e registro**, com as três grandezas saindo juntas e
   carimbadas. É aqui que sai a foto da avaliação qualitativa.
3. **Falhas induzidas**, com desbalanceamento, atrito e obstrução aplicados de forma
   controlada e repetível, e os dados de cada condição separados.
4. **Linha de base e detecção**, com o processamento das características e o critério
   de anomalia.
5. **Instalação em aparelho real**, se houver autorização e equipamento disponível.

As etapas 1 e 2 são o objetivo imediato, e dependem de compra. O laboratório não tem
acelerômetro, não tem sensor de corrente e não tem mais nenhum sensor de temperatura:
o único DHT11 está na bancada do projeto de colmeias.

Enquanto os sensores não chegam, dá para adiantar a cadeia de aquisição no **Arduino
Uno**, que funciona com o cabo USB-B do laboratório: relógio carimbando, LCD
mostrando e o CSV saindo na serial, com valor fixo no lugar do sensor. Quando o
primeiro sensor chegar, ele entra numa cadeia que já roda.

## O equipamento de ensaio

**Cooler de 12 V, de 80 mm, com rolamento e conector de 3 ou 4 pinos.** Decisão
tomada, registrada em `perguntas-em-aberto.md`.

Gira a milhares de RPM, aceita desbalanceamento com massa presa a uma pá, sobe de
corrente quando o fluxo é obstruído e aquece sob carga. Os três sinais têm o que
medir, o que não acontece com o motor de passo de 5 V do laboratório.

E é da mesma classe do ventilador da unidade condensadora, então o artigo declara um
componente equivalente em vez de um substituto genérico.

O terceiro pino é a saída de tacômetro. Ele entrega um pulso por volta e rende um
quarto sinal sem custo nenhum: rotação caindo junto com corrente subindo é assinatura
de atrito.

## Disponível no laboratório

| Qtd | Item | Onde | Para quê |
|---|---|---|---|
| 1 | Placa ESP32-WROVER-DEV v1.6 | Gaveta `ESP 32 CAM` | Controlador. Tem micro-USB embutido. A câmera OV2640 que vem junto não é usada aqui e pode ficar na gaveta |
| 1 | Arduino Uno, com o cabo USB azul | Caixa das placas azuis | Validar sensores antes de passar para o ESP32 |
| 1 | Módulo de relógio de tempo real | Gaveta `MÓDULO REAL TIME CLOCK` | Data e hora em cada medição |
| 1 | Protoboard HIKARI HK-P100 | Caixa das protoboards | Montagem, e bornes para medir consumo |
| ~15 | Jumpers macho-fêmea | Caixa `MACHO-FÊMEA` | Ligar os módulos à placa |
| ~10 | Jumpers macho-macho | Caixa `MACHO-MACHO` | Ligações na protoboard |
| 4 | Resistores de 10 kΩ | Gaveteiro laranja, gaveta `10 KΩ` | Pull-up, se o sensor for de 4 pinos |
| 1 | Módulo relé | Gaveta `MÓDULO RELÉ` | Desligamento automático, se o RF10 for adotado |
| 1 | Display LCD 1602 | Gaveta `LCD 1602` | Acompanhar as leituras durante a montagem |
| 1 | Módulo conversor I2C para LCD | Gaveta `MÓDULO CONVERSOR P/ LCD 1602` | Peça separada, em outra gaveta. Sem ela o display consome seis pinos em vez de dois |

## Precisa ser comprado

Nenhum destes está no laboratório.

### Libera a montagem de bancada

| Qtd | Item | Especificação | Por que |
|---|---|---|---|
| 1 | Acelerômetro | MPU6050 ou ADXL345, barramento I2C | Vibração é o sinal mais usado na bibliografia do projeto, presente em 4 das 6 referências específicas. Sem ele não há RMS nem FFT. |
| 1 | Sensor de corrente de bancada | INA219, barramento I2C | Mede a corrente do motor de ensaio, que é de baixa tensão. O ACS712 de 5 A não tem resolução para algumas centenas de miliampères. |
| 3 | Cooler de 12 V | 80 mm, rolamento, conector de 3 ou 4 pinos | Equipamento de ensaio. O kit de três permite provocar falha sem perder a única unidade e repetir a mesma condição em unidades diferentes. |
| 1 | Fonte de 12 V | corrente suficiente para o cooler | O cooler é de 12 V e o ESP32 de 3,3 V. |
| 1 | Módulo driver ou transistor | MOSFET ou ponte H simples | Para o microcontrolador ligar e desligar o cooler. |
| 4 | Sonda de temperatura | DS18B20 encapsulado, duas de 1 m e duas de 3 m | O laboratório não tem mais nenhum sensor de temperatura: o único DHT11 está na bancada do outro projeto. Os quatro dividem um pino, porque o DS18B20 é de barramento 1-Wire. |
| 1 | Resistor de 4,7 kΩ | — | Pull-up do barramento 1-Wire. Um só, para as quatro sondas. |
| 1 | Cabo micro-USB | com linhas de dados | Os cabos do laboratório são USB-B, dos Arduino, e não encaixam na ESP32-WROVER-DEV. |

### Permite instalar em aparelho real

| Qtd | Item | Especificação | Por que |
|---|---|---|---|
| 1 | Transformador de corrente não invasivo | SCT-013, garra dividida | Mede a corrente do compressor por indução, sem cortar fio e sem contato com a rede. O INA219 não serve nessa tensão. |
| 2 | Sondas de temperatura | DS18B20 encapsulado em aço | Presas nos tubos de cobre com abraçadeira e pasta térmica. |
| 1 | Base magnética ou adesivo estrutural | para o acelerômetro | Sensor de vibração frouxo mede o próprio balanço, não a máquina. |
| 1 | Pasta térmica e abraçadeiras metálicas | — | Acoplamento térmico das sondas ao cobre. |
| 1 | Caixa vedada com prensa-cabo | uso externo | Protege a eletrônica junto à unidade externa. |
| 1 | Fonte regulada de 5 V | corrente suficiente para placa e sensores | O RNF02 exige, e não há fonte confirmada. |

## Não pegar

Estão no laboratório e parecem úteis, mas ficaram fora do escopo:

- `MÓDULO SENSOR DE SOM KY-038`, porque áudio não entra nesta versão
- Célula de carga e `MÓDULO HX711`, porque não há peso a medir num ar-condicionado.
  Serviriam apenas como ferramenta de ensaio, para aplicar carga controlada
- `SHIELD LORAWAN` e `SHIELD ETHERNET W5500`, porque a comunicação prevista é Wi-Fi
- `SERVO MOTOR SG90`, que não gira continuamente
- `MÓDULO STEP MOTOR 28BYJ-48`, descartado como equipamento de ensaio porque não aquece
