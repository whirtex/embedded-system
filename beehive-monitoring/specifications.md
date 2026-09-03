# Especificações técnicas

Estas especificações foram elaboradas com base no objetivo do projeto, nos componentes disponíveis na faculdade e nas seis referências registradas em reference-contributions.md. Os valores indicados como proposta inicial devem ser confirmados com o professor e ajustados após os primeiros testes de bancada.

## 1. Arquitetura do sistema

O sistema será organizado em quatro blocos:

1. sensores ambientais e acústicos instalados na colmeia;
2. câmera posicionada na entrada da colmeia;
3. controlador responsável pela coleta, pelo registro temporal e pela comunicação;
4. computador ou servidor responsável pelo armazenamento, processamento de visão computacional e visualização.

A arquitetura deve preservar os dados brutos ou amostras selecionadas sempre que possível. O controlador pode enviar medições e resultados processados, enquanto o processamento mais pesado dos modelos ocorre em um computador ou servidor. Essa separação é compatível com as arquiteturas IoT e de processamento remoto discutidas por Zheng et al. [1] e Tashakkori et al. [4].

## 2. Controlador e comunicação

- A ESP32-CAM está disponível e será considerada a unidade de captura de imagens na entrada.
- O ESP8266 pode funcionar como controlador de sensores e comunicação.
- Arduino Uno e Arduino Mega estão disponíveis, mas não são a primeira opção para transmissão sem fio e processamento de imagens.
- Wi-Fi é a opção inicial quando houver cobertura no local da colmeia, em linha com as redes avaliadas por Henry et al. [5].
- MQTT é o protocolo recomendado para a primeira versão, por ser compatível com a arquitetura do Beemon [4]. HTTP pode ser usado como alternativa para testes simples.
- Ethernet e LoRa permanecem como alternativas de comunicação, mas o alcance, a infraestrutura, o consumo e o formato de integração ainda precisam ser avaliados.
- O envio deve incluir identificação da colmeia, identificação do sensor, data e hora, valor medido, unidade, qualidade da leitura e versão do firmware.

## 3. Sensoriamento ambiental

- O DHT11 disponível será usado inicialmente para temperatura e umidade.
- Como referência de instalação, serão avaliados quatro pontos: centro da colmeia, margem, entrada e ambiente externo, conforme a distribuição utilizada por Zheng et al. [1].
- A frequência inicial proposta é uma leitura por minuto para cada sensor.
- A quantidade de módulos DHT11 e a posição exata devem ser confirmadas antes da montagem final.
- O DHT11 é adequado para um protótipo didático, mas sua precisão, faixa de operação e resistência à umidade devem ser avaliadas antes de uma instalação prolongada.
- Cada leitura deve ser acompanhada de data, hora, identificação do ponto de medição e indicação de erro ou ausência de resposta.

## 4. Sensoriamento acústico e de vibração

- O KY-038 está disponível, mas deve ser usado apenas como indicador simples de intensidade de ruído. Ele não deve ser descrito no artigo como microfone de gravação acústica.
- Para reproduzir melhor a abordagem de Uthoff et al. [3], será necessário confirmar a disponibilidade de um microfone adequado e, se necessário, de um conversor analógico-digital.
- Um acelerômetro não foi identificado entre os componentes disponíveis. Ele deve ser confirmado com o professor caso a análise de vibração seja mantida.
- Proposta inicial para áudio: janelas de 10 segundos, uma vez por minuto, com taxa de amostragem definida após a escolha do microfone. A taxa de 4 kHz pode ser usada apenas como ponto de partida para um teste de indicador acústico, não como especificação validada.
- Caso um acelerômetro seja incluído, a frequência de amostragem e a forma de fixação deverão ser definidas a partir do sensor escolhido e da faixa de vibração esperada.
- Devem ser preservadas as características extraídas e, quando o armazenamento permitir, amostras brutas para posterior validação. A literatura não fornece um limite universal de áudio ou vibração para diagnóstico.

## 5. Captura de imagens

- A ESP32-CAM deve ser instalada voltada para a entrada da colmeia, com fixação estável e proteção contra chuva.
- O posicionamento não pode bloquear a passagem das abelhas nem alterar significativamente a ventilação.
- Para o primeiro teste, a câmera pode operar entre 10 e 16 quadros por segundo durante uma janela de captura. O valor de até 16 quadros por segundo é usado como referência por Zheng et al. [1].
- Proposta inicial de coleta: uma janela de 30 segundos a cada 5 minutos, com ajuste após medir volume de dados, consumo e qualidade das imagens.
- A resolução, o campo de visão, a iluminação e a distância até a entrada devem ser registrados e mantidos constantes durante cada experimento.
- Imagens representativas devem ser armazenadas para validação; não é necessário transmitir vídeo continuamente na primeira versão.

## 6. Visão computacional

- YOLOv5 e DeepSORT são referências para detecção e rastreamento de abelhas [1].
- YOLOv7-tiny é uma referência de modelo leve para monitoramento da entrada e detecção de pólen [2].
- A abordagem de baixo custo baseada em Raspberry Pi e subtração de fundo de Tu et al. [6] deve ser considerada como alternativa inicial se os modelos neurais forem inviáveis no hardware disponível.
- O processamento provavelmente será executado em computador ou servidor, pois não foi identificado um acelerador dedicado de visão computacional entre os componentes disponíveis.
- Será necessário criar ou obter imagens rotuladas de abelhas, entrada da colmeia e, se aplicável, pólen e Varroa.
- O desempenho deve ser medido separando dados de treinamento, validação e teste. Para rastreamento, podem ser usadas MOTA e MOTP; para detecção ou classificação, precisão, recall e F1-score; para contagens e atividade, erro de contagem e R².
- A detecção de Varroa deve ser tratada como prova de conceito até que existam dados de campo suficientes e rotulados para validá-la.

## 7. Registro, armazenamento e envio

- O módulo de relógio de tempo real pode fornecer a marcação temporal quando a rede não estiver disponível.
- O registro mínimo deve conter: data, hora, identificação da colmeia, identificação do sensor, temperatura, umidade, indicador ou características acústicas, janela de imagem, contagem de abelhas, fluxo de entrada e saída e resultados das detecções.
- Não foi identificado um módulo de cartão SD. A alternativa inicial é enviar os dados para um computador ou servidor; uma memória temporária deverá ser providenciada ou confirmada para suportar falhas de comunicação.
- Valores ambientais e resultados processados podem ser enviados a cada minuto.
- Imagens e sinais acústicos devem ser armazenados em janelas ou amostras selecionadas para reduzir o volume de dados, mantendo metadados suficientes para reproduzir a análise.
- Ainda é preciso definir banco de dados, formato dos registros, política de retenção e interface de visualização.
- A arquitetura deve permitir exportar os dados para análise posterior, conforme a necessidade de validar as hipóteses do projeto.

## 8. Frequência inicial de coleta

| Fonte de dados | Frequência proposta | Forma de registro | Observação |
|---|---|---|---|
| Temperatura e umidade | 1 leitura por minuto | Valor, unidade, ponto, data e hora | Pode ser reduzida ou aumentada após avaliar estabilidade e consumo. |
| Áudio | Janela de 10 s por minuto | Características e amostras selecionadas | Depende de microfone adequado; o KY-038 não substitui esse componente. |
| Vibração | A definir | Amostras ou características em janelas | Só será especificada após confirmar um acelerômetro. |
| Imagens da entrada | 10--16 fps durante 30 s a cada 5 min | Imagens selecionadas e métricas agregadas | Proposta inicial para reduzir armazenamento e consumo; deve ser validada com a atividade real da colmeia. |
| Dados processados | 1 pacote por minuto | Contagens, fluxo, características e alertas | Pode ser enviado por MQTT quando a conexão estiver disponível. |

Esses valores são parâmetros de protótipo, não limites estabelecidos pela literatura. A frequência final deve equilibrar resolução temporal, volume de dados, consumo de energia e capacidade da rede.

## 9. Alimentação e instalação

- Há suportes e conectores para pilhas AA, mas não foi confirmada uma fonte adequada para operação prolongada.
- A autonomia esperada, a necessidade de bateria recarregável e a possibilidade de alimentação solar devem ser discutidas com o professor.
- Será necessário um gabinete protegido contra chuva, poeira e umidade.
- Também serão necessários suportes, cabos adequados, vedações e uma fixação que não danifique a colmeia.
- A instalação não deve bloquear a entrada, alterar a ventilação de forma relevante ou expor as abelhas a partes elétricas.
- A câmera, os sensores e os cabos devem ser inspecionados periodicamente para verificar deslocamento, condensação e danos.

## 10. Dados e validação

Para avaliar o sistema, será necessário obter:

- dados ambientais em condições normais e em mudanças de clima;
- gravações acústicas ou de vibração acompanhadas do contexto da coleta;
- imagens da entrada em diferentes horários, iluminações e níveis de atividade;
- imagens rotuladas para treinar e testar os modelos;
- contagens ou anotações manuais para servir como referência;
- registros de chuva, temperatura externa e outros eventos relevantes;
- dados de mais de uma colmeia, quando possível, para avaliar generalização;
- critérios para identificar corretamente uma detecção ou classificação.

A validação deve separar treinamento e teste e informar as condições de coleta. As referências [1]--[6] mostram que métricas, conjuntos de dados e condições de registro variam; portanto, os resultados do projeto não devem ser generalizados para todas as colmeias sem evidência.

## 11. Itens para confirmar ou providenciar

1. Microfone adequado para registrar o som da colmeia.
2. Acelerômetro, caso a medição de vibração seja mantida.
3. Quantidade de sensores DHT11 e suas posições.
4. Estrutura para fixar a ESP32-CAM na entrada.
5. Gabinete protegido contra chuva e umidade.
6. Fonte de alimentação para operação prolongada.
7. Computador ou servidor para executar os modelos de visão computacional.
8. Base de imagens rotuladas de abelhas, pólen e, se necessário, Varroa.
9. Módulo de armazenamento local ou estratégia de buffer.
10. Definição do banco de dados, protocolo e dashboard.
11. Referências e dados bibliográficos dos alunos do IBMEC.

## 12. Arquitetura recomendada para energia e transmissão

### 12.1 Alimentação e conexão dos sensores internos

Os sensores devem permanecer dentro da colmeia, enquanto a bateria, o microcontrolador e os módulos de comunicação devem ser instalados preferencialmente fora dela, em uma caixa protegida contra chuva, poeira e umidade. Essa separação considera as restrições de tamanho, custo, consumo e confiabilidade características de sistemas embarcados [9] e reduz a necessidade de intervir no interior da colmeia. Dessa forma, somente os cabos dos sensores atravessam a parede da colmeia, por uma abertura pequena protegida por prensa-cabo ou vedação apropriada.

O fluxo de alimentação proposto é:

```text
Bateria ou fonte externa
        |
Regulador de tensão compatível com a placa
        |
ESP8266/ESP32, módulo LoRa e sensores
```

Todos os componentes devem compartilhar o mesmo terra (GND). A bateria não deve ser conectada diretamente antes de confirmar a tensão suportada por cada placa. A alimentação deve ser regulada, e capacitores próximos ao microcontrolador e ao rádio devem ser considerados para reduzir quedas de tensão durante a transmissão. O suporte de pilhas AA disponível pode ser usado no protótipo, mas a autonomia deverá ser medida com o sistema em operação.

Cada DHT11 pode receber alimentação e ser conectado a um pino de dados do microcontrolador. A saída analógica do KY-038 pode ser conectada a uma entrada ADC, lembrando que esse módulo deve ser tratado apenas como indicador simples de intensidade sonora. Os cabos e a instalação não podem bloquear a entrada, alterar significativamente a ventilação ou expor as abelhas a partes elétricas.

O nó de sensores pode acordar em intervalos definidos, realizar as medições, registrar a data e a hora, transmitir um pacote e retornar ao modo de baixo consumo. Essa estratégia é coerente com a operação contínua de redes de sensores sem fio para colmeias descrita por Henry et al. [5]. A câmera deve possuir alimentação separada ou uma estratégia própria de economia, pois seu consumo é maior que o dos sensores ambientais.

### 12.2 LoRa, LoRaWAN e MQTT

LoRa é a tecnologia de rádio usada para transmitir pequenas mensagens a longa distância com baixo consumo. LoRa não é, por si só, uma conexão com a internet: o módulo instalado junto ao microcontrolador precisa transmitir para outro módulo ou para um gateway. LoRaWAN é uma arquitetura de rede que organiza os dispositivos LoRa, os gateways, o servidor de rede e a aplicação.

MQTT é um protocolo de mensagens usado depois que os dados chegam a uma rede IP, como Wi-Fi, Ethernet ou 4G. Ele utiliza um broker: o nó ou gateway publica mensagens em tópicos, e o dashboard ou banco de dados assina esses tópicos para receber os dados. A escolha desse protocolo acompanha a arquitetura do Beemon, que combina aquisição multissensorial, MQTT, armazenamento remoto e dashboard [4].

Assim, LoRa e MQTT têm funções diferentes e podem ser usados em conjunto. A separação entre dispositivos, comunicação, serviços e processamento também segue a organização em camadas de arquiteturas IoT discutida por Ray [10]:

```text
Sensores internos
      | cabos
ESP8266/ESP32 + RTC + módulo LoRa
      | LoRa
Gateway LoRa próximo ao apiário
      | Wi-Fi, Ethernet ou 4G
Broker MQTT
      | tópicos
Banco de dados e dashboard
```

O pacote transmitido por LoRa deve conter apenas dados pequenos, como identificação da colmeia, data e hora, temperatura, umidade, intensidade sonora, nível da bateria e resultados agregados da visão computacional. Fotografias, vídeos e áudio contínuo não devem ser enviados por LoRa. Esses dados devem ser armazenados localmente ou transmitidos por Wi-Fi, Ethernet ou outra rede com maior capacidade.

Para o primeiro teste, recomenda-se uma comunicação LoRa ponto a ponto, com um ESP equipado com LoRa como transmissor e outro ESP equipado com LoRa como receptor. Essa etapa reproduz, em escala reduzida, a ideia de nós sensores distribuídos usada em redes sem fio para apiários [5]. O receptor pode encaminhar os dados para um computador por USB ou Wi-Fi. Em uma versão com várias colmeias, deve ser avaliada uma rede LoRaWAN com gateway e servidor apropriados.

### 12.2.1 Parâmetros e validação do enlace LoRa

A configuração do rádio deve equilibrar alcance, velocidade e consumo. O spreading factor (SF), a largura de banda, a potência de transmissão e o tempo no ar influenciam a sensibilidade, a duração da transmissão e a autonomia da bateria. Um SF maior tende a melhorar a recepção em enlaces difíceis, mas aumenta o tempo de transmissão; por isso, não deve ser escolhido apenas pelo maior alcance teórico. A configuração final deverá ser obtida por testes no local da colmeia, considerando obstáculos, altura e orientação da antena. A relação entre taxa de dados, sensibilidade e tempo no ar deve ser analisada conforme a documentação técnica da Semtech.

Se a versão LoRaWAN for adotada, o nó alimentado por bateria deverá priorizar a Classe A, na qual o dispositivo transmite quando necessário e abre janelas curtas para receber respostas. Essa classe permite que o nó permaneça em baixo consumo entre as medições, mas não é adequada para comandos que precisem chegar instantaneamente. Como os nós das colmeias serão fixos, o Adaptive Data Rate (ADR) poderá ser avaliado depois que a estabilidade do enlace for confirmada, com o objetivo de reduzir o tempo no ar e o consumo. Classes B e C não são necessárias para a primeira versão.

O teste inicial deve comparar a comunicação ponto a ponto com uma possível implantação LoRaWAN. No modo ponto a ponto, o grupo controla diretamente os dois rádios e não precisa de gateway ou servidor LoRaWAN, mas deverá implementar ou registrar endereçamento, confirmação, tentativas de reenvio e segurança. No modo LoRaWAN, será necessário configurar o plano regional correto no nó e no gateway, cadastrar os dispositivos e integrar o servidor de rede ao MQTT.

Para o uso no Brasil, o módulo, a antena e o gateway devem ser compatíveis com a faixa e o plano regional aplicáveis, além de atender às exigências de certificação da Anatel. A faixa nominal de 915 MHz não deve ser tratada como suficiente por si só: o grupo deverá confirmar canais, potência, antena e homologação do equipamento antes da aquisição e da instalação. A Resolução nº 680 da Anatel e o Ato nº 14.448 devem ser consultados junto com os parâmetros regionais atuais da LoRa Alliance.

Cada experimento deve registrar a distância, a presença de obstáculos, a configuração do rádio, RSSI, SNR, número de pacotes enviados, número de pacotes recebidos, perdas, retransmissões, latência e tensão da bateria antes e depois do teste. Esses dados permitirão decidir se LoRa atende à telemetria ambiental e evitarão apresentar o alcance como uma característica fixa do sistema.

### 12.3 Integração com a câmera e a visão computacional

A ESP32-CAM deve seguir um caminho de comunicação separado do nó de sensores:

```text
ESP32-CAM
      | Wi-Fi ou armazenamento local
Computador ou Raspberry Pi
      | YOLO + DeepSORT
Contagens, fluxo e alertas
      | MQTT e, quando necessário, LoRa
Servidor e dashboard
```

O YOLO processa cada imagem e fornece caixas delimitadoras, classes e níveis de confiança para as abelhas. O DeepSORT recebe essas detecções, associa objetos entre quadros e atribui identificadores temporários para estimar o fluxo de entrada e saída, conforme a combinação de detecção e rastreamento utilizada por Zheng et al. [1]. A adoção de modelos leves e a comparação com abordagens de baixo custo também são motivadas por Narcia-Macias et al. [2] e Tu et al. [6]. O sistema deve transmitir as métricas agregadas, e não cada quadro de vídeo.

Essa arquitetura separa o tráfego de baixa taxa e baixo consumo dos sensores do tráfego de maior volume da câmera, mantendo a integração multimodal sugerida pelos sistemas de monitoramento de colmeias [1], [4] e [5]. A escolha final entre LoRa ponto a ponto, LoRaWAN e Wi-Fi deverá considerar distância, cobertura, disponibilidade de gateway, consumo, custo, volume de dados e necessidade de armazenamento durante falhas de comunicação.

Referências introdutórias: [LoRa Alliance — visão geral de LoRaWAN](https://lora-alliance.org/resource_hub/what-is-lorawan/), [Semtech — visão geral de LoRa](https://www.semtech.com/lora/what-is-lora) e [OASIS — especificação MQTT](https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html).
