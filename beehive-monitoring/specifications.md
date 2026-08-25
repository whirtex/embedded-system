# Especificações técnicas

Estas são as especificações preliminares para o sistema de monitoramento de colmeias. Os valores indicados como proposta inicial ainda precisam ser confirmados com o professor e ajustados conforme os sensores e os dados disponíveis.

## 1. Arquitetura do sistema

O sistema pode ser dividido em quatro partes:

1. sensores ambientais e acústicos instalados na colmeia;
2. câmera posicionada na entrada da colmeia;
3. controlador responsável pela coleta e pela comunicação;
4. computador ou servidor para armazenamento, análise e visualização.

A câmera e os sensores não precisam executar todo o processamento localmente. Uma alternativa é usar o ESP32-CAM para capturar imagens e enviar os dados para um computador, onde os modelos de visão computacional serão executados.

## 2. Controlador e comunicação

- O ESP32-CAM está entre os componentes disponíveis e pode ser usado para capturar imagens na entrada da colmeia.
- O ESP8266 também está disponível e pode funcionar como controlador de sensores e comunicação.
- Arduino Uno e Arduino Mega estão disponíveis, mas não são a primeira opção para transmissão sem fio e processamento de imagens.
- A comunicação pode usar Wi-Fi, Ethernet ou LoRa.
- Para a primeira versão, recomenda-se usar Wi-Fi quando houver cobertura no local da colmeia.
- O protocolo de comunicação, como MQTT ou HTTP, ainda precisa ser definido.

## 3. Sensoriamento ambiental

- O DHT11 disponível pode medir temperatura e umidade.
- Como referência de instalação, podem ser considerados quatro pontos: centro da colmeia, margem, entrada e ambiente externo.
- A proposta inicial é coletar temperatura e umidade uma vez por minuto.
- A quantidade de módulos DHT11, a posição exata e a proteção contra umidade ainda precisam ser confirmadas.
- O DHT11 pode ser suficiente para um protótipo didático, mas sua precisão e sua resistência ao ambiente externo devem ser avaliadas antes da instalação permanente.

## 4. Sensoriamento acústico e de vibração

- O KY-038 está disponível, mas fornece uma indicação simples de som e não deve ser tratado como um sistema de gravação acústica confiável.
- Para reproduzir melhor a abordagem vibroacústica do artigo, será necessário um microfone adequado e, possivelmente, um conversor analógico-digital.
- Um acelerômetro também não foi identificado entre os componentes disponíveis.
- Como proposta inicial, o áudio pode ser coletado a 4 kHz em janelas curtas, por exemplo, 10 segundos por minuto. Esse valor precisa ser confirmado com o professor e com o sensor escolhido.
- Caso seja utilizado um acelerômetro em um protótipo de baixa velocidade, uma frequência inicial de 200 Hz pode ser testada. Diagnósticos industriais de rolamentos podem exigir uma frequência maior.

## 5. Captura de imagens

- A ESP32-CAM pode ser instalada voltada para a entrada da colmeia.
- A câmera deve possuir fixação estável, proteção contra chuva e posicionamento que não bloqueie a passagem das abelhas.
- Como referência inicial, a captura pode operar entre 10 e 16 quadros por segundo. O trabalho de Zheng et al. relata processamento de até 16 quadros por segundo.
- A resolução da imagem, o campo de visão, a iluminação e a distância até a entrada ainda precisam ser definidos.
- O sistema deve armazenar imagens ou resultados suficientes para validar as detecções sem transmitir vídeo continuamente.

## 6. Visão computacional

- O texto cita YOLOv5 e DeepSORT para detecção e rastreamento de abelhas.
- O texto também cita modelos YOLOv7-tiny para monitoramento de entrada e detecção de pólen.
- O processamento provavelmente precisará ser executado em um computador ou servidor, pois não foi identificado um acelerador de visão computacional entre os componentes disponíveis.
- Será necessário criar ou obter um conjunto de imagens rotuladas de abelhas, entrada da colmeia e, se aplicável, pólen e Varroa.
- O modelo deverá ser avaliado com métricas adequadas, como MOTA e MOTP para rastreamento e precisão, recall e F1-score para classificação ou detecção.
- A detecção de Varroa deve ser tratada como prova de conceito até que existam dados de campo suficientes para validá-la.

## 7. Registro, armazenamento e envio

- O módulo de relógio de tempo real pode fornecer a marcação temporal das medições.
- O sistema deve registrar, no mínimo, data, hora, identificação da colmeia, temperatura, umidade, dados acústicos ou suas características e resultados da visão computacional.
- Não foi identificado um módulo de cartão SD. A alternativa é enviar os dados para um computador ou servidor.
- A proposta inicial é enviar os valores ambientais e os resultados processados a cada minuto.
- Imagens e sinais acústicos podem ser armazenados em janelas ou amostras selecionadas para reduzir o volume de dados.
- Ainda é preciso definir o banco de dados, o formato dos registros e a interface de visualização.

## 8. Alimentação e instalação

- Há suportes e conectores para pilhas AA, mas não foi confirmada uma fonte adequada para operação prolongada.
- A autonomia esperada, a necessidade de bateria recarregável e a possibilidade de alimentação solar devem ser discutidas com o professor.
- Será necessário um gabinete protegido contra chuva, poeira e umidade.
- Também serão necessários suportes, cabos adequados, vedações e fixação que não danifique a colmeia.
- A instalação não deve bloquear a entrada, alterar a ventilação de forma relevante ou expor as abelhas a partes elétricas.

## 9. Dados e validação

Para avaliar o sistema, será necessário obter:

- dados ambientais em condições normais;
- gravações acústicas ou de vibração;
- imagens da entrada da colmeia em diferentes condições;
- imagens rotuladas para treinar e testar os modelos;
- registros de chuva, temperatura externa e outros eventos relevantes;
- critérios para identificar corretamente uma detecção ou classificação.

As referências fornecidas no texto devem ser conferidas antes da versão final do artigo. As referências dos alunos do IBMEC também precisam ser fornecidas para que possam ser verificadas e citadas quando contribuírem diretamente para o trabalho.

## 10. Itens para confirmar ou providenciar

1. Microfone adequado para registrar o som da colmeia.
2. Acelerômetro, caso a medição de vibração seja mantida.
3. Quantidade de sensores DHT11 e suas posições.
4. Estrutura para fixar a ESP32-CAM na entrada.
5. Gabinete protegido contra chuva e umidade.
6. Fonte de alimentação para operação prolongada.
7. Computador ou servidor para executar os modelos de visão computacional.
8. Base de imagens rotuladas de abelhas, pólen e, se necessário, Varroa.
9. Definição do banco de dados, protocolo e dashboard.
10. Referências e dados bibliográficos dos alunos do IBMEC.
