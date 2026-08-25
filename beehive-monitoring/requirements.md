# Requisitos do sistema de monitoramento de colmeias

A lista foi elaborada com base no objetivo do projeto e nos componentes disponíveis na faculdade. Os requisitos consideram uma solução embarcada e não invasiva, capaz de acompanhar as condições ambientais e a atividade da colônia, registrar os dados e disponibilizá-los para análise posterior.

As referências [1]--[6] correspondem aos trabalhos registrados em reference-contributions.md e em references.bib.

## Legenda

- **Disponível:** o componente ou recurso foi identificado entre os materiais disponíveis.
- **Parcial:** existe um componente relacionado, mas falta confirmar quantidade, adequação, instalação ou integração.
- **Ausente:** o item não foi identificado entre os componentes disponíveis e deve ser confirmado com o professor.
- **A definir:** depende do escopo, dos dados disponíveis ou da orientação do professor.

## Requisitos funcionais

| Código | Requisito | Situação | Base bibliográfica |
|---|---|---|---|
| RF01 | O sistema deve monitorar continuamente as condições ambientais da colmeia e do ambiente externo. | Parcial. Há módulos DHT11, mas ainda é preciso definir quantidade, posição, proteção e alimentação. | [1], [4], [5] |
| RF02 | O sistema deve medir temperatura e umidade em pontos relevantes, como centro, margem, entrada e ambiente externo. | Parcial. O DHT11 está disponível, mas a quantidade necessária para todos os pontos não foi confirmada. | [1], [4], [5] |
| RF03 | O sistema deve registrar sinais acústicos no interior da colmeia. | Ausente. O KY-038 pode indicar intensidade de ruído, mas não substitui um microfone adequado para registrar sinais acústicos. | [1], [3], [4], [5] |
| RF04 | O sistema deve registrar a atividade das abelhas na entrada da colmeia. | Parcial. Há uma ESP32-CAM, mas faltam suporte, proteção, posicionamento e definição da qualidade da imagem. | [1], [2], [6] |
| RF05 | O sistema deve detectar e contar abelhas nas imagens da entrada. | A definir. Será necessário implementar, treinar e validar um modelo de visão computacional. | [1], [2], [6] |
| RF06 | O sistema deve acompanhar a movimentação das abelhas ao longo do tempo. | A definir. A solução pode usar rastreamento de objetos ou análise do fluxo de entrada e saída. | [1], [2], [6] |
| RF07 | O sistema deve permitir a identificação de pólen nas imagens, caso essa função faça parte da primeira versão. | A definir. O recurso depende de imagens rotuladas e de um escopo aprovado pelo professor. | [2] |
| RF08 | O sistema deve produzir evidências que apoiem a avaliação de estados da colônia, como presença da rainha ou preparação para enxameação. | A definir. A classificação deve ser validada com dados de campo e não deve ser apresentada como diagnóstico automático sem testes suficientes. | [3], [5] |
| RF09 | O sistema deve registrar data e hora para cada medição, imagem, amostra acústica e resultado processado. | Parcial. Há um módulo de relógio de tempo real, mas a sincronização ainda precisa ser definida. | [1], [4] |
| RF10 | O sistema deve enviar dados processados para uma aplicação ou servidor remoto. | Parcial. Há ESP8266, ESP32-CAM, Ethernet e LoRa, mas o protocolo, a rede e o destino ainda não foram definidos. | [1], [4], [5] |
| RF11 | O sistema deve armazenar o histórico de medições, amostras selecionadas, imagens processadas e resultados das detecções. | Ausente. Não foi identificado um módulo de cartão SD; o armazenamento em servidor ainda precisa ser providenciado ou confirmado. | [1], [4] |
| RF12 | O sistema deve apresentar dados e alertas ao responsável pela colmeia. | A definir. Ainda é preciso escolher dashboard, display local, e-mail ou mensagem para celular. | [1], [4] |
| RF13 | O sistema deve continuar registrando dados quando a comunicação estiver indisponível e reenviá-los quando a conexão retornar. | A definir. Será necessária uma memória temporária e uma estratégia de reenvio. | [4], [5] |
| RF14 | O sistema deve permitir a exportação e a análise posterior dos dados coletados. | A definir. O formato dos registros, o banco de dados e o método de exportação ainda precisam ser definidos. | [1], [4], [6] |

## Requisitos não funcionais

| Código | Requisito | Situação | Base bibliográfica |
|---|---|---|---|
| RNF01 | O monitoramento deve causar o mínimo de interferência possível na colônia. | Requisito do projeto. A instalação deve reduzir a necessidade de abrir a colmeia e não pode bloquear a entrada. | [1], [3], [4], [5] |
| RNF02 | O sistema deve funcionar por longos períodos sem manutenção constante. | Parcial. A fonte de energia, a autonomia e a rotina de manutenção ainda precisam ser definidas. | [4], [5] |
| RNF03 | Os componentes instalados na colmeia devem ser protegidos contra umidade, poeira e variações de temperatura. | Ausente. Não foi identificada uma caixa ou proteção adequada para instalação externa. | — |
| RNF04 | O sistema deve consumir pouca energia e permitir operação compatível com a fonte escolhida. | A definir. Ainda faltam autonomia, modo de repouso e fonte de alimentação. | [4], [5] |
| RNF05 | As medições devem possuir precisão suficiente para acompanhar mudanças ambientais e comportamentais da colônia. | A definir. A precisão mínima e o procedimento de calibração devem ser estabelecidos com o professor. | [1], [3], [5] |
| RNF06 | O sistema deve permitir a substituição ou a adição de sensores sem reconstrução completa da instalação. | Parcial. Há protoboards, jumpers e módulos de expansão disponíveis, mas a montagem final ainda não foi definida. | [4], [5] |
| RNF07 | O sistema deve preservar a integridade dos dados quando houver falha de energia ou comunicação. | A definir. Será necessário escolher armazenamento temporário, confirmação de recebimento e recuperação. | [1], [4] |
| RNF08 | O sistema deve permitir a avaliação objetiva dos modelos de visão computacional. | A definir. É necessário estabelecer imagens rotuladas, dados de teste e métricas como precisão, recall, F1-score, MOTA, MOTP e R². | [1], [2], [6] |
| RNF09 | O sistema deve permitir a repetição dos testes em diferentes colmeias, iluminações e condições de registro. | Parcial. Ainda falta definir a posição da câmera, a iluminação e o procedimento de coleta. | [3], [6] |
| RNF10 | O sistema deve ser documentado quanto à montagem, instalação na colmeia, coleta, comunicação e validação. | A documentação deverá ser produzida durante o projeto. | [1]--[6] |

## Itens que precisam ser confirmados com o professor

Os seguintes itens não foram identificados com segurança entre os componentes disponíveis ou dependem de uma decisão de escopo:

1. Quantidade de sensores DHT11 e posições de instalação.
2. Microfone adequado para gravação acústica; o KY-038 deve ser considerado apenas um indicador simples de ruído.
3. Acelerômetro, caso a análise de vibração seja mantida.
4. Suporte, gabinete e vedação para a ESP32-CAM e os sensores.
5. Fonte de alimentação e autonomia esperada.
6. Computador ou servidor para executar os modelos e armazenar os dados.
7. Módulo de armazenamento local ou estratégia de buffer durante falhas de comunicação.
8. Quantidade de imagens rotuladas e disponibilidade de dados para abelhas, pólen e Varroa.
9. Necessidade de classificar enxameação, ausência da rainha ou outros estados da colônia na primeira versão.
10. Frequência de envio em tempo real ou em lotes.
11. Referências dos alunos do IBMEC mencionadas no texto, para que possam ser verificadas e citadas.

Até que esses pontos sejam respondidos, os recursos de pólen, Varroa, presença da rainha e preparação para enxameação devem ser descritos como funcionalidades experimentais, e não como resultados garantidos.
