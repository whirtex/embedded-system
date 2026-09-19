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
decisões e as dúvidas em aberto estão em `decisoes-do-projeto.md`.

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
tomada, registrada em `decisoes-do-projeto.md`.

Gira a milhares de RPM, aceita desbalanceamento com massa presa a uma pá, sobe de
corrente quando o fluxo é obstruído e aquece sob carga. Os três sinais têm o que
medir, o que não acontece com o motor de passo de 5 V do laboratório.

E é da mesma classe do ventilador da unidade condensadora, então o artigo declara um
componente equivalente em vez de um substituto genérico.

O terceiro pino é a saída de tacômetro. Ele entrega dois pulsos por volta, no padrão
de cooler de PC, e rende um quarto sinal sem custo nenhum: rotação caindo junto com
corrente subindo é assinatura de atrito. A saída é de coletor aberto, então precisa de
pull-up, e é para isso que servem os resistores de 10 kΩ da lista do laboratório.

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
| 2 | Acelerômetro | ADXL345 em placa GY-291, 8 pinos, barramento I2C | Vibração é o sinal mais usado na bibliografia do projeto, presente em 4 das 6 referências específicas. Sem ele não há RMS nem FFT. Escolhido no lugar do MPU6050 pelo teto de amostragem: o MPU6050 trava em 1 kHz de saída, o que deixa 500 Hz úteis, e a assinatura de atrito é de banda larga e mora acima disso. O ADXL345 chega a 3200 Hz. Começa em I2C, nos mesmos dois fios do INA219, e se a banda não bastar aceita SPI sem trocar de peça, saída que o MPU6050 não tem. A GY-291 atende os dois requisitos de montagem: tem os dois furos de fixação e os 8 pinos que o SPI exige. Vendido em par, e o par serve de seguro contra placa que chega defeituosa, sem mudar uma linha de código. **Usar apenas uma**: um sensor por cooler faria a variação entre sensores se misturar com a variação entre unidades, que é justamente a separação que sustenta o treino e o teste. A barra de pinos vem solta e precisa ser soldada antes do primeiro ensaio. |
| 1 | Super cola | cianoacrilato, tubo pequeno | Fixa o acelerômetro na moldura do cooler. Fita dupla-face não serve: ela é mole e some com a assinatura de atrito, que mora em alta frequência. Uma colagem por unidade, com todas as condições medidas na mesma sessão. |
| 2 | Parafuso M3 × 12 mm | auto-atarraxante para plástico, cabeça chata | Fixa o acelerômetro na moldura do cooler, como alternativa à cola, para comparar os dois acoplamentos. Furo cego na moldura, sem porca: porca passante cairia do lado de dentro, no caminho do ar. São dois porque com um só a placa gira em torno do parafuso e o acoplamento fica pior que o da cola — confirmar na compra que a plaquinha escolhida tem dois furos de fixação. A placa tem que ficar prensada contra o plástico, sem espaçador, que vira mola e inventa ressonância. |
| 1 | Sensor de corrente de bancada | INA219, barramento I2C | Mede a corrente do motor de ensaio, que é de baixa tensão. O ACS712 de 5 A não tem resolução para algumas centenas de miliampères. |
| 3 | Cooler de ensaio | **Akasa DFC802512**, 80 mm, ball bearing, 4 pinos, 2500 RPM, 0,18 A | Equipamento de ensaio. O kit de três permite provocar falha sem perder a única unidade e repetir a mesma condição em unidades diferentes. O quarto pino é entrada de PWM e não é usado para variar rotação nos ensaios, que rodam em 12 V fixo: serve para comandar duas rotações diferentes e conferir se os canais de corrente e de tacômetro respondem, antes de confiar neles para detectar falha. Modelo escolhido depois de comparar 17 anúncios: é o único que reúne rolamento de esferas, impresso na etiqueta do fabricante, e quatro fios de sinal. Ventoinha de gabinete comum é bucha de dois fios, e bucha não produz as frequências de defeito que a FFT procura. **Cuidado com dois enganos comuns nos anúncios**: conector Molex tem quatro vias mas carrega só 12 V e terra, sem tacômetro; e vários títulos anunciam "4 pinos" enquanto a ficha do mesmo anúncio diz 2. |
| 1 | Ventoinha de montagem | 80 × 80 × 25 mm, 12 V, entrega imediata, mancal indiferente | Comprada só para adiantar a montagem enquanto os coolers de ensaio não chegam: parafusar na base, colar o acelerômetro, ligar o INA219 e fazer o CSV sair. Permite validar vibração, corrente e temperatura antes dos Akasa chegarem; só o tacômetro fica de fora se ela for de dois fios. **Não entra em nenhum ensaio registrado**, porque o mancal é diferente e misturar unidades de modelos distintos contamina a comparação com a linha de base. |
| 4 | Parafuso M4 × 50 mm, com porca e arruela | passante, de máquina | Prende o cooler à base rígida. Não use auto-atarraxante: a falha de fixação frouxa aperta e afrouxa os mesmos parafusos dezenas de vezes, e rosca em MDF espana. Com porca dá para contar voltas a partir do encosto, o que torna a condição documentável e repetível. Quatro servem para os três coolers, porque se monta um de cada vez. |
| 1 | Massa adesiva | tipo massa de fixação de cartaz | Fabrica a falha de desbalanceamento: uma bolinha presa numa pá tira o centro de rotação do lugar. Escolhida por ser pesável, moldável e removível sem resíduo, o que permite repetir a mesma massa em ensaios diferentes. Registrar o peso em gramas e qual pá, senão a falha não é repetível. Passar fita por cima: a 2500 RPM o que soltar vira projétil. |
| 1 | Fonte de 12 V | 1 A, regulada, plugue P4 | O cooler é de 12 V e o ESP32 de 3,3 V. 1 A cobre o consumo com folga, inclusive o pico de partida, porque se monta um cooler por vez. Precisa ser regulada: duas das quatro falhas são detectadas por corrente subindo, e fonte que cai de tensão sob carga contamina justamente essa leitura. |
| 1 | Adaptador P4 fêmea com borne | 5,5 × 2,1 mm | A fonte de 12 V termina em plugue P4, que não entra na protoboard. |
| 2 | Sensor de temperatura | DS18B20 em encapsulamento TO-92, sem sonda de aço | O laboratório não tem mais nenhum sensor de temperatura: o único DHT11 está na bancada do outro projeto. Uma vai no cubo do motor e outra mede o ar ambiente, para ler o aquecimento como elevação acima da sala, que é o que a Seção II já declara. TO-92 nu porque a sonda de aço tem massa térmica demais para um cubo de 40 mm e é lenta no ar; o encapsulado em aço é a peça da fase do ar-condicionado. As duas dividem um pino, porque o DS18B20 é de barramento 1-Wire. |
| 1 | Resistor de 4,7 kΩ | — | Pull-up do barramento 1-Wire. Um só, para as duas sondas. |
| 1 | Cabo micro-USB | com linhas de dados | Os cabos do laboratório são USB-B, dos Arduino, e não encaixam na ESP32-WROVER-DEV. |
| 2 | Barra de jumpers | uma de 40 vias macho-fêmea e uma de 40 macho-macho | A montagem consome cerca de 16 macho-fêmea entre acelerômetro, INA219, os dois DS18B20 e os sinais do cooler, e o laboratório tem ~15. Jumper é vendido em barra de 40 e custa pouco, então vale ter folga para refazer ligação, perder ponta e emendar distância sem ficar na mão. |

### Não precisa comprar

Fazem parte da bancada, mas saem de sobra ou já existem.

| Item | Especificação | Para quê |
|---|---|---|
| Base rígida | tábua de madeira reta, uns 2 cm de espessura | O cooler é parafusado nela pelos M4. Grossa para não flexionar, e pesada ou presa à mesa: tábua fina anda junto com o cooler e cada ensaio começa num lugar diferente. |
| Papelão rígido | sobra de caixa | Fabrica a falha de obstrução, tapando a entrada de ar. Recortar peças que cubram frações definidas da área, como 25%, 50% e 75%, e segurar sempre à mesma distância, em vez de improvisar a cada ensaio. |
| Fita | qualquer uma | Prende os fios dos DS18B20 na grade e cobre a massa adesiva na pá. |

Ferramentas necessárias, todas já disponíveis: furadeira com brocas de 4 mm e 2,5 mm, alicate
descascador e chave de fenda pequena. A soldagem das barras de pinos do ADXL345 e do INA219
é serviço externo, a menos que as placas venham com os pinos já soldados.

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
