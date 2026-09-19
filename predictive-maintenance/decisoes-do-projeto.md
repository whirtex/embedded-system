# Decisões do projeto

O que já está decidido no protótipo de manutenção preditiva, agrupado por tema, e o
que ainda está em aberto no fim do arquivo.

Cada decisão registra o porquê, o que foi descartado e, quando existe, o limite que
precisa ser declarado no artigo. A ideia é não rediscutir o que já foi resolvido.

## Escopo e objetivo

- **Escopo restrito** às etapas de monitoramento de condição, tratamento de dados,
  detecção de falhas e avaliação do Meitz et al. Modelagem de degradação, prognóstico
  e vida útil restante ficam de fora.
- **Objetivo da primeira versão**: detecção de anomalia como resultado principal, e
  **classificação das falhas induzidas como resultado adicional**, se os ensaios
  renderem dados suficientes. **Estimativa de vida útil restante fica fora**, porque
  exige dados de operação até a falha, com várias unidades e meses de registro.

  A classificação é viável porque a bancada fabrica os próprios rótulos: cada falha
  induzida já vem etiquetada, e as quatro condições previstas produzem combinações
  distintas entre os três sinais. Desbalanceamento dá vibração alta com corrente quase
  igual; atrito dá corrente alta com vibração moderada; obstrução dá corrente alta com
  temperatura subindo; fixação frouxa dá vibração alta com corrente quase inalterada.
  É essa separação que um classificador aproveita, e ela só existe porque são três
  sinais e não um.

  Mohammed et al. comparam cinco algoritmos supervisionados em motor CA com falhas
  induzidas, e Gupta et al. relatam F1 de 0,86 classificando motor e caixa de
  engrenagens com Random Forest. Os dois sustentam o método.

  **Limite a declarar no artigo**: o sistema classificaria falhas induzidas em
  bancada, não falhas de ar-condicionado. Massa presa a uma hélice não é rolamento de
  compressor desgastado.
- **Operação contínua de 24 horas** como recorte de aplicação.
- **Ordem de execução: bancada primeiro, ar-condicionado real como segunda fase.**
  Decisão de 18 de setembro de 2026. A primeira versão do artigo é construída inteira
  sobre o cooler de ensaio.

  O ensaio em aparelho real não está cancelado. Fica condicionado à confirmação de
  segurança da instalação, que é a única pergunta desta lista que depende do
  professor. Por isso a garra SCT-013, as sondas em aço, a base magnética, a pasta
  térmica, a caixa vedada e a fonte de 5 V saem da primeira compra e voltam quando a
  autorização vier.

  **Limite a declarar no artigo**: enquanto a segunda fase não acontecer, o texto
  reporta resultados de bancada, não de ar-condicionado. Vale o mesmo limite já
  registrado na decisão sobre classificação.

## Equipamento de ensaio

- **Equipamento de ensaio da bancada**: **cooler de 12 V**, não o motor de passo. Um
  cooler gira a milhares de RPM, aceita desbalanceamento com massa presa a uma pá,
  sobe de corrente quando o fluxo é obstruído e aquece sob carga, então os três sinais
  têm o que medir. O motor de passo de 5 V não aquece e deixaria o canal de
  temperatura sem demonstração.

  O argumento principal, porém, é de escopo: o ventilador da unidade condensadora
  **é** um cooler, motor elétrico girando hélice para mover ar através de uma
  serpentina. O artigo passa a dizer que usa um ventilador da mesma classe do
  ventilador do condensador, em vez de um substituto genérico de componente rotativo.

  Comprar o modelo de **3 ou 4 pinos**: o terceiro pino é a saída de tacômetro, que
  entrega dois pulsos por volta e dá um quarto sinal sem custo. Rotação caindo com
  corrente subindo é assinatura de atrito, e é o tipo de evidência cruzada que
  sustenta a contribuição de informar qual medição desviou.

  Levar o kit de três unidades: permite provocar falha sem medo de perder a única, e
  repetir a mesma condição em unidades diferentes, o que reforça a separação entre
  treino e teste.
- **Mecanismo das falhas induzidas**, três das quatro definidas:

  | Falha | Como |
  |---|---|
  | Desbalanceamento | massa adesiva pesada, presa numa pá, com peso em gramas registrado |
  | Fixação frouxa | parafuso M4 afrouxado em número contado de voltas a partir do encosto |
  | Obstrução | papelão recortado cobrindo frações definidas da entrada de ar |

  Os três são reversíveis, repetíveis e documentáveis, que é o que a pergunta exigia.
  **Atrito continua sem mecanismo** e segue na lista aberta.
- **Como induzir atrito: parafuso com pastilha pressionando a face do cubo, dosado em
  voltas.** Decisão de 19 de setembro de 2026, fechando a última das quatro falhas sem
  mecanismo.

  Uma ripa de madeira atravessa dois dos parafusos M4 do canto, do lado da entrada de
  ar, e sustenta um parafuso M3 com feltro ou borracha na ponta. O parafuso avança
  contra a face do cubo, perto do centro: quanto menor o raio, menor a velocidade de
  contato e menos a pastilha se gasta entre um ensaio e outro.

  **A dose é o número de voltas a partir do encosto.** Zero é a condição normal, e as
  demais são graduadas. É a mesma lógica já adotada na fixação frouxa, o que mantém o
  procedimento uniforme entre as falhas.

  Três ganhos sobre as alternativas. É **reversível**, então as três unidades
  sobrevivem e a ordem dos ensaios deixa de importar; cai a regra de deixar o atrito
  por último. É **graduável**, então dá para mostrar a resposta crescendo com a dose,
  o que é mais forte no artigo do que uma condição binária. E **produz os quatro
  sinais**: calor, corrente, queda de rotação e energia de alta frequência na
  vibração.

  Descartadas: retirar lacre e lubrificante mata a unidade e não é dosável; injetar
  material viscoso no mancal não é quantificável nem reversível.

  **Limite a declarar no artigo**: é atrito aplicado de fora, não desgaste de
  rolamento. Mesma classe de limitação já declarada sobre a massa presa à pá.

  Extra opcional, só depois de gravar tudo nas três unidades: sacrificar uma delas
  retirando o lubrificante, para um ponto de comparação com desgaste real.

## Sensores e medição

- **Três sinais**: temperatura, vibração e corrente. Votação do grupo em 16 de
  setembro de 2026, confirmando o que o artigo já declarava.
- **Dois sensores de corrente diferentes**: INA219 na bancada, que é de baixa tensão,
  e transformador de corrente não invasivo tipo SCT-013 no equipamento real, que é de
  rede elétrica. Ligar o INA219 em 220 V não serve e é perigoso.
- **Pontos de medição no split**: acelerômetro na carcaça do compressor; garra de
  corrente no condutor do compressor, com a caixa elétrica fechada; sondas de
  temperatura na linha de líquido e na linha de sucção; sensores de ar no retorno e no
  insuflamento da evaporadora. Ver `assets/instalacao-sensores-ac.png`.
- **Pontos de temperatura na bancada: dois.** Um no ar que sai do cooler, preso na
  moldura logo atrás do cubo, e outro solto no ar da sala, fora do jato. O sinal é a
  **diferença** entre os dois, não o valor de cada um: leitura isolada mede a estação
  do ano, e a diferença mede o cooler.

  Nenhum dos dois encosta no motor. A ideia de colar sensor no cubo foi descartada
  porque o lado visível do cubo gira junto com as pás, e porque o fluxo de ar
  resfriaria o sensor, fazendo a obstrução aparecer como aquecimento sem ser.

  **Limite a declarar no artigo**: o que se mede é elevação térmica do conjunto sobre
  o ambiente, não temperatura do enrolamento do motor.
- **Acelerômetro e sensor de corrente comprados** em 18 de setembro de 2026: ADXL345
  em placa GY-291, duas unidades, e um INA219. O ADXL345 foi escolhido no lugar do
  MPU6050 pelo teto de amostragem, e a segunda unidade é seguro contra placa
  defeituosa, não para usar as duas ao mesmo tempo.

## Aquisição e dados

- **Onde os dados ficam: servidor remoto por Wi-Fi.** Decisão de 18 de setembro de
  2026. O ESP32 envia as medições pela rede, sem cartão de memória. Isso fecha o RF11,
  que o `requirements.md` marcava como ausente por falta de módulo de cartão SD.

  Duas consequências. A primeira está na pergunta sobre o MQTT, que deixou de ser
  opcional: sem destino escolhido, não há para onde enviar. A segunda é que o firmware
  precisa de buffer local em LittleFS, na própria flash do ESP32, gravando quando a
  rede cai e despejando o atraso na reconexão. Sem isso, cada oscilação de Wi-Fi custa
  um ensaio de 24 horas inteiro, e não há prazo para refazer ensaio.
- **Destino dos dados: MQTT em broker público, com LittleFS como pulmão.** Decisão de
  19 de setembro de 2026, fechando a pergunta que a escolha do Wi-Fi tinha tornado
  obrigatória.

  O ESP32 publica cada registro num tópico do `test.mosquitto.org`, sem infraestrutura
  para montar. Mohammed et al., já citado no artigo, usa o mesmo arranjo, e a Seção II
  já estava escrita declarando MQTT. O tópico ainda precisa ser confirmado com o
  professor, tarefa que o `guia-geral.md` já previa.

  A fraqueza do MQTT é não guardar histórico: se ninguém estiver assinando, a mensagem
  se perde. Por isso o firmware **só grava na flash quando o envio falha**, e despeja
  o acumulado quando a rede volta. Em operação normal o arquivo fica vazio, então o
  limite de espaço da partição deixa de ser problema.
- **O módulo DS1302 sai do projeto; a hora vem de NTP.** Medido em 18 e 19 de setembro
  de 2026: com `delay(3000)` no laço, o relógio avançava 18 segundos por ciclo, ou
  seja, exatamente **seis vezes mais rápido** que o tempo real. Além disso, sem
  bateria no suporte ele voltava para a hora da compilação a cada religamento.

  O defeito é do módulo, não da fiação, e não vale consertar: a bancada final roda no
  ESP32 com Wi-Fi, e o NTP entrega hora correta sem módulo, sem bateria e sem cristal.
  Confirmado funcionando em 19 de setembro de 2026.
- **Rotulagem dos ensaios por comando na porta serial.** Cada linha do CSV carrega duas
  colunas de rótulo, `unidade` e `condicao`, alteradas durante o ensaio digitando
  `u B` ou `c desbalanceamento` no monitor serial.

  Sem isso os dados não servem para nada: um arquivo com milhares de linhas de números
  não guarda em lugar nenhum qual delas foi gravada com o peso preso na pá, e essa
  informação não se recupera depois. Anotar em papel exigiria casar horário com linha
  na mão, em milhares de registros, com erro silencioso a cada engano.

  A coluna `condicao` é o que permite aprender a linha de base saudável e treinar a
  classificação. A coluna `unidade` é o que permite segurar um cooler inteiro fora do
  treino.

## Ensaios e avaliação

- **Protocolo dos ensaios: três repetições por condição em cada unidade, com duas como
  piso.** Decisão de 19 de setembro de 2026.

  **Repetição significa desfazer e refazer a falha**, não cortar uma gravação longa em
  pedaços. Tirar a massa da pá e prender de novo, apertar o parafuso e afrouxar de
  novo contando as voltas. Dividir um único ensaio entre treino e teste vaza
  informação e infla o resultado, que é a crítica registrada sobre o Gupta et al.

  **Entre repetições refaz-se a falha, nunca a colagem do acelerômetro.** O sensor
  fica colado do começo ao fim daquela unidade. Recolar no meio faz a diferença de
  acoplamento entrar nos dados disfarçada de falha.

  **Dez minutos por rodada, descartando os três primeiros.** A temperatura é o canal
  mais lento e precisa estabilizar; o início é transitório térmico, não condição.

  **Separação treino e teste**, conforme o número de coolers comprados:

  | Unidades | Ajuste | Teste |
  |---|---|---|
  | três | A e B | **C inteira**, nunca usada no ajuste |
  | uma | repetições 1 e 2 | repetição 3 |

  Com três unidades o teste roda num cooler fisicamente diferente, o que corrige a
  fraqueza anotada sobre o Gupta et al. Com uma só, a separação por repetição é mais
  fraca e **precisa ir declarada como limitação no artigo**.

  Custo em tempo, com três unidades e três repetições: 5 condições × 3 unidades × 3
  repetições dão 45 rodadas, cerca de 7h30 de gravação. Com duas repetições cai para
  30 rodadas e 5 horas. É tempo de deixar rodando, não de trabalho ativo.
- **Método de detecção: Isolation Forest treinado apenas na operação saudável.**
  Decisão de 19 de setembro de 2026. É o mesmo arranjo que Kolok et al. aplicam com
  ESP32 e sensores MEMS, extraindo RMS e FFT, e é o que a introdução já declara como
  contribuição: aprender a linha de base saudável em vez de exigir um histórico de
  falhas rotuladas.

  O modelo roda no notebook, sobre o CSV, não dentro do ESP32. A placa calcula as
  características e envia; a decisão fica do lado remoto, como a Seção II descreve.

  **Solução alternativa da Seção V: detecção por limite fixo no RMS contra o Isolation
  Forest.** Os dois aproveitam exatamente os mesmos dados dos ensaios, então a
  comparação não custa coleta adicional. O `specifications.md` já sugeria esse par.
- **Métricas reportadas: F1 para a detecção, matriz de confusão para a classificação.**
  Decisão de 19 de setembro de 2026.

  Na **detecção de anomalia**: precisão, recall e F1. Acurácia fica de fora de
  propósito. Como as gravações em condição normal tendem a somar mais tempo que as de
  falha, um modelo que responde sempre "normal" acertaria a maioria e pareceria bom
  sendo inútil. F1 não cai nessa armadilha.

  Na **classificação das quatro falhas**: matriz de confusão mais F1 por classe. A
  matriz mostra **quais** falhas o modelo troca entre si, e isso é exatamente o que
  interessa aqui: a tabela de assinaturas prevê que desbalanceamento e fixação frouxa
  são o par difícil, porque os dois dão vibração alta com corrente quase igual. A
  matriz prova ou desmente essa previsão numa figura só.

  Escolher F1 também deixa o resultado **diretamente comparável com o Gupta et al.**,
  que relata F1 de 0,86 e já está citado no artigo.

  A segunda metade da pergunta original, sobre separar os dados de ajuste dos de
  teste, está respondida no protocolo de ensaios registrado acima.

## Fora desta versão

- **Alerta remoto e desligamento por relé ficam fora desta versão.** Decisão de 19 de
  setembro de 2026. O RF18, com bot de Telegram, e o RF10, com acionamento de relé,
  não são exigidos pelo PDF de orientações e competiriam com os ensaios na mesma
  semana da AP1.

  **Não estão cancelados**: ficam declarados no artigo como trabalho futuro e seguem
  previstos para depois. A arquitetura escolhida facilita: como a comunicação é por
  MQTT, os dois entram depois como assinantes do mesmo tópico, **sem alterar nem
  regravar o firmware do ESP32**. Foi um dos motivos de escolher publicação e
  assinatura em vez de envio ponto a ponto.

## Referências

- **Referências de alunos do Ibmec**: o PDF manda procurar num slide de aula ou nas
  Instruções da AP1, que não estão no repositório. A lista foi levantada direto no
  anais do SBrT 2025, varrendo as 24 páginas do evento. O professor assina sete
  trabalhos, e o mais próximo deste projeto é **A Low-Cost IoT-Driven Reuse of
  Condensate Water for Automated Plant Irrigation**, DOI
  `10.14209/sbrt.2025.1571157370`, que trata de água de condensado de ar-condicionado
  com sensores IoT de baixo custo.

## Decisões ainda pendentes

### Depende de confirmação com o professor

- **Quem faz a instalação no aparelho real, e como.** A caixa elétrica da unidade
  externa é rede elétrica. O `specifications.md` já determina que o protótipo não
  use tensão da rede sem proteção e autorização, então esta é a única pergunta da
  lista que precisa de confirmação com o professor antes de ser executada.

  A garra SCT-013 mede por indução, sem cortar fio nem encostar em terminal, o que
  reduz bastante o risco. Os dois sensores de ar da evaporadora medem por fora e não
  exigem abrir nada.

### Para resolver medindo

Não têm resposta de escritório. Só saem com a bancada montada.

- **Frequência de amostragem da vibração.** Precisa cobrir a faixa de interesse do
  equipamento, e é o que decide se a FFT enxerga alguma coisa. O ADXL345 escolhido
  chega a 3200 Hz, então o teto não é mais restrição: falta escolher o valor.

- **Quanto a corrente sobe** em cada falha induzida, para saber se o sensor escolhido
  tem resolução suficiente. Vale medir logo na primeira sessão: se a obstrução mal
  mexer na corrente, essa classe passa a depender da temperatura.

- **Qual limiar separa normal de anômalo**, e com que margem.
