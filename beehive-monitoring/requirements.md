# Requisitos do sistema de monitoramento de colmeias

Este documento reúne os requisitos iniciais para um sistema embarcado de monitoramento não invasivo de colmeias. A lista foi elaborada a partir do texto sobre o artigo Beehive Monitoring e dos componentes disponíveis na faculdade.

## Legenda

- Disponível: componente ou recurso disponível na faculdade.
- Parcial: há algum componente relacionado, mas ainda falta uma confirmação ou um complemento.
- Ausente: o item não foi identificado entre os componentes disponíveis na faculdade e deve ser confirmado com o professor.
- A definir: depende do escopo do artigo, dos dados disponíveis ou da orientação do professor.

## Requisitos funcionais

| Código | Requisito | Situação |
|---|---|---|
| RF01 | O sistema deve monitorar continuamente as condições ambientais da colmeia e do ambiente externo. | Parcial. Há módulos DHT11, mas ainda é preciso definir a quantidade, a posição e a proteção dos sensores. |
| RF02 | O sistema deve medir temperatura e umidade em pontos relevantes da colmeia, como centro, margem, entrada e ambiente externo. | Parcial. O DHT11 está disponível, mas não foi confirmada a quantidade de sensores necessária para todos os pontos. |
| RF03 | O sistema deve registrar sinais acústicos no interior da colmeia. | Ausente. O KY-038 pode indicar ruído, mas não substitui um microfone adequado para registrar sinais acústicos. |
| RF04 | O sistema deve registrar a atividade das abelhas na entrada da colmeia. | Parcial. Há uma placa ESP32-CAM, mas ainda faltam suporte, posicionamento, proteção e definição da qualidade da imagem. |
| RF05 | O sistema deve detectar e contar abelhas nas imagens da entrada. | A definir. Será necessário implementar e treinar um modelo de visão computacional. |
| RF06 | O sistema deve acompanhar a movimentação das abelhas ao longo do tempo. | A definir. A solução pode usar rastreamento de objetos, como o DeepSORT citado no texto. |
| RF07 | O sistema deve permitir a identificação de pólen nas imagens. | A definir. Esse recurso depende de imagens rotuladas e deve ser tratado como uma etapa específica do projeto. |
| RF08 | O sistema deve produzir dados que possam apoiar a avaliação de estados da colônia, como presença da rainha ou preparação para enxameação. | A definir. A classificação precisa ser validada com dados de campo e não deve ser considerada automática sem testes suficientes. |
| RF09 | O sistema deve registrar data e hora para cada medição. | Parcial. Há um módulo de relógio de tempo real, mas ainda é preciso definir a forma de sincronização. |
| RF10 | O sistema deve enviar os dados para uma aplicação ou servidor remoto. | Parcial. Há ESP8266, ESP32-CAM, Ethernet e LoRa, mas o protocolo, a rede e o destino ainda não foram definidos. |
| RF11 | O sistema deve armazenar o histórico de medições, imagens processadas e resultados das detecções. | Ausente. Não foi identificado um módulo de cartão SD; será necessário usar armazenamento local ou um servidor. |
| RF12 | O sistema deve apresentar os dados e os alertas ao responsável pela colmeia. | A definir. Ainda é preciso escolher entre dashboard, display local, e-mail ou mensagem para celular. |
| RF13 | O sistema deve continuar registrando dados quando a comunicação estiver indisponível. | A definir. Será necessário definir uma memória temporária ou um mecanismo de reenvio. |
| RF14 | O sistema deve permitir a análise posterior dos dados coletados. | A definir. O formato dos registros e o método de exportação ainda precisam ser definidos. |

## Requisitos não funcionais

| Código | Requisito | Situação |
|---|---|---|
| RNF01 | O monitoramento deve causar o mínimo de interferência possível na colônia. | Requisito do projeto. A instalação dos sensores e da câmera deve evitar a abertura frequente da colmeia. |
| RNF02 | O sistema deve funcionar por longos períodos sem manutenção constante. | Parcial. Ainda falta definir a fonte de energia e a autonomia esperada. |
| RNF03 | Os componentes instalados na colmeia devem ser protegidos contra umidade, poeira e variações de temperatura. | Ausente. Não foi identificada uma caixa ou proteção adequada para instalação externa. |
| RNF04 | O sistema deve consumir pouca energia. | A definir. A autonomia, o modo de repouso e a fonte de alimentação ainda precisam ser especificados. |
| RNF05 | As medições devem possuir precisão suficiente para acompanhar mudanças ambientais e comportamentais da colônia. | A definir. A precisão mínima deve ser estabelecida com o professor. |
| RNF06 | O sistema deve permitir a substituição ou a adição de sensores. | Parcial. Há protoboards, jumpers e módulos de expansão disponíveis. |
| RNF07 | O sistema deve preservar a integridade dos dados quando houver falha de energia ou comunicação. | A definir. Será necessário escolher uma estratégia de armazenamento e recuperação. |
| RNF08 | O sistema deve permitir a avaliação objetiva dos modelos de visão computacional. | A definir. É necessário estabelecer métricas, dados de teste e imagens rotuladas. |
| RNF09 | O sistema deve permitir a repetição dos testes em condições semelhantes. | Parcial. Ainda falta definir a posição da câmera, a iluminação e o procedimento de coleta. |
| RNF10 | O sistema deve ser documentado quanto à montagem, à instalação na colmeia e ao funcionamento. | A documentação deverá ser produzida durante o projeto. |

## Perguntas para o professor

1. O objetivo é apenas monitorar a colmeia ou também classificar eventos, como enxameação e ausência da rainha?
2. A detecção de pólen fará parte da primeira versão?
3. A detecção de Varroa fará parte do projeto? Se sim, quais dados rotulados estarão disponíveis?
4. Podemos usar o ESP32-CAM apenas para capturar imagens e fazer o processamento em um computador ou servidor?
5. Qual quantidade e quais posições de sensores devem ser usadas dentro e fora da colmeia?
6. O KY-038 pode ser usado apenas como indicador de ruído ou será necessário um microfone com gravação de áudio?
7. O projeto precisa medir vibração? Se sim, será necessário adquirir um acelerômetro.
8. Qual autonomia de funcionamento é esperada?
9. Os dados precisam ser enviados em tempo real ou podem ser enviados em lotes?
10. Qual tipo de proteção física deve ser usada para a instalação externa?
11. O professor possui as referências dos alunos do IBMEC mencionadas no texto?
12. As três referências já citadas serão mantidas no artigo após a verificação dos dados bibliográficos?
