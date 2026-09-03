# Contribuição das referências para o projeto

A lista foi elaborada com base no objetivo do projeto e nos componentes disponíveis na faculdade. Este arquivo relaciona as dez referências selecionadas com a arquitetura, os requisitos e as especificações do sistema embarcado de manutenção preditiva.

## Matriz de contribuição

| Ref. | Trabalho | Contribuição para o projeto | Limitação ou cuidado |
|---|---|---|---|
| [1] | Yousuf et al., *IoT-Based Health Monitoring and Fault Detection of Industrial AC Induction Motor for Efficient Predictive Maintenance* | Apoia uma arquitetura de baixo custo com sensores de temperatura, vibração, corrente, tensão e velocidade, aquisição embarcada, alertas e armazenamento remoto. | O trabalho monitora um motor de indução industrial; os resultados não podem ser transferidos diretamente para compressores de ar-condicionado sem testes próprios. |
| [2] | Mohammed, Abdulateef e Hamad, *An IoT and Machine Learning-Based Predictive Maintenance System for Electrical Motors* | Orienta o uso conjunto de acelerômetro, sensor de corrente e temperatura, Raspberry Pi, MQTT e modelos supervisionados para distinguir operação normal e falhas. Também informa uma coleta experimental a cada segundo. | O conjunto é de uma única máquina, tem tamanho limitado e usa falhas induzidas; a frequência de um segundo não é suficiente para preservar a forma de onda bruta de vibração. |
| [3] | Kolok et al., *Low-Cost IoT-Based Predictive Maintenance Using Vibration* | Apoia o uso de ESP32 e sensores MEMS de baixo custo, extração de RMS e FFT e detecção de anomalias com Isolation Forest treinado a partir da operação saudável. | A acurácia de detecção ficou pouco acima de 72,9\%, e o protótipo foi avaliado em uma pequena máquina rotativa; é necessária calibração para o equipamento do projeto. |
| [4] | Meitz et al., *A Literature Review Framework and Open Research Challenges for Predictive Maintenance in Industry 4.0* | Ajuda a organizar o projeto como um fluxo completo que inclui monitoramento, tratamento dos dados, detecção de falhas, prognóstico, planejamento e avaliação. | É uma revisão de literatura e não fornece um protótipo único nem parâmetros de aquisição prontos para serem copiados. |
| [5] | Gupta et al., *Predictive Maintenance of Baggage Handling Conveyors Using IoT* | Mostra como tratar vibrações e registros de manutenção de um sistema real, lidar com ruído e ausência de histórico até a falha e comparar classificadores. | O estudo trata esteiras de bagagens, não equipamentos de refrigeração, e depende da qualidade dos registros e rótulos disponíveis. |
| [6] | Tormos et al., *A Physics-Informed Explainable AI Framework for HVAC Anomaly Detection and Maintenance-Oriented Analysis in Urban Bus Fleets* | Mostra como detectar anomalia em ar-condicionado sem rótulo de falha, mapeando os sensores sobre o ciclo de refrigeração e usando Kernel SHAP para indicar qual variável causou cada desvio. | O estudo usa telemetria de frota de ônibus, não equipamento estacionário, e a atribuição por SHAP é pesada demais para rodar em microcontrolador. |
| [7] | Gubbi et al., *Internet of Things (IoT): A Vision, Architectural Elements, and Future Directions* | Fundamenta a integração entre redes de sensores, Internet, computação distribuída e nós embarcados de sensores e atuadores. | É uma visão geral da IoT, não um estudo específico de manutenção ou HVAC. |
| [8] | Lin et al., *A Survey on Internet of Things: Architecture, Enabling Technologies, Security and Privacy, and Applications* | Apoia a organização da arquitetura IoT e o uso de processamento em névoa ou na borda, próximo aos dispositivos, para reduzir latência e melhorar a resiliência. | É uma revisão ampla; a escolha dos protocolos e da arquitetura precisa ser validada no protótipo. |
| [9] | Carvalho et al., *A Systematic Literature Review of Machine Learning Methods Applied to Predictive Maintenance* | Fundamenta o uso de aprendizado de máquina em manutenção preditiva e destaca a importância da qualidade dos dados, da seleção do método e da validação. | A revisão abrange diferentes setores e não fornece um modelo pronto para aparelhos de ar-condicionado. |
| [10] | Es-Sakali et al., *Review of Predictive Maintenance Algorithms Applied to HVAC Systems* | Relaciona diretamente manutenção preditiva a sistemas HVAC e organiza abordagens baseadas em conhecimento, modelos físicos e dados históricos obtidos por sensores IoT. | É uma revisão sem dados experimentais próprios; o projeto ainda precisa produzir e validar seus próprios dados. |

## Relação com os requisitos e as especificações

| Parte do projeto | Referências que dão suporte | Aplicação prevista |
|---|---|---|
| Temperatura e condições de operação | [1] e [2] | Registrar a condição térmica do equipamento e o contexto ambiental ao longo do tempo. |
| Vibração e sinais acústicos | [1], [2], [3] e [5] | Medir alterações mecânicas, extrair características como RMS e FFT e investigar desbalanceamento ou desgaste. |
| Corrente elétrica | [1] e [2] | Acompanhar variações de carga e sobrecorrente, caso um sensor adequado seja disponibilizado. |
| Comunicação e histórico | [1], [2], [7] e [8] | Transmitir medições e alertas por rede, preferencialmente com MQTT, e manter um histórico para análise. |
| Organização e qualidade dos dados | [4] e [5] | Documentar frequência de coleta, limpeza, rótulos, falhas induzidas e separação dos dados de treinamento e teste. |
| Detecção e avaliação | [2], [3], [5], [6] e [9] | Comparar limites ou modelos leves, medir o desempenho com métricas adequadas e evitar depender apenas da acurácia. |
| Alertas interpretáveis | [4] e [6] | Informar qual medição motivou o alerta, com a atribuição rodando no servidor e não no microcontrolador. |
| Aplicação em climatização | [10] | Relacionar sensores, histórico operacional e algoritmos de manutenção preditiva ao monitoramento de aparelhos HVAC em ambientes críticos ou coletivos, com operação prolongada. |

## Síntese para o desenvolvimento

As dez referências sustentam uma solução que combina sensores de vibração, corrente e temperatura, processamento embarcado, comunicação sem fio e armazenamento histórico. A literatura também indica que o modelo é apenas uma parte do sistema: qualidade dos dados, calibração, rotulagem das falhas, escolha das métricas e interpretação dos alertas precisam ser documentadas.

No escopo definido, o protótipo deve ser apresentado como um sistema de monitoramento e detecção experimental de anomalias para aparelhos de ar-condicionado instalados em ambientes críticos ou coletivos e sujeitos a operação prolongada. A previsão de falhas futuras ou da vida útil restante somente poderá ser afirmada depois da obtenção de um histórico representativo, com estados normais e falhas validadas no equipamento-alvo.

## Registros bibliográficos verificados

| Ref. | Tipo e publicação | DOI / registro |
|---|---|---|
| [1] | Artigo — *Measurement and Control*, v. 57, n. 8, p. 1146--1160, 2024 | [10.1177/00202940241231473](https://doi.org/10.1177/00202940241231473) |
| [2] | Artigo — *Journal Européen des Systèmes Automatisés*, v. 56, n. 4, p. 651--656, 2023 | [10.18280/jesa.560414](https://doi.org/10.18280/jesa.560414) |
| [3] | Artigo — *Sensors*, v. 25, n. 21, art. 6610, 2025 | [10.3390/s25216610](https://doi.org/10.3390/s25216610) |
| [4] | Artigo de revisão — *Computers \& Industrial Engineering*, v. 206, art. 111193, 2025 | [10.1016/j.cie.2025.111193](https://doi.org/10.1016/j.cie.2025.111193) |
| [5] | Artigo — *Computers \& Industrial Engineering*, v. 177, art. 109033, 2023 | [10.1016/j.cie.2023.109033](https://doi.org/10.1016/j.cie.2023.109033) |
| [6] | Artigo — *Algorithms*, v. 19, n. 7, art. 586, 2026; acesso aberto, CC BY 4.0 | [10.3390/a19070586](https://doi.org/10.3390/a19070586) |
| [7] | Artigo — *Future Generation Computer Systems*, v. 29, n. 7, p. 1645--1660, 2013 | [10.1016/j.future.2013.01.010](https://doi.org/10.1016/j.future.2013.01.010) |
| [8] | Artigo — *IEEE Internet of Things Journal*, v. 4, n. 5, p. 1125--1142, 2017 | [10.1109/JIOT.2017.2683200](https://doi.org/10.1109/JIOT.2017.2683200) |
| [9] | Artigo — *Computers \& Industrial Engineering*, v. 137, art. 106024, 2019 | [10.1016/j.cie.2019.106024](https://doi.org/10.1016/j.cie.2019.106024) |
| [10] | Artigo — *Energy Reports*, v. 8, p. 1003--1012, 2022 | [10.1016/j.egyr.2022.07.130](https://doi.org/10.1016/j.egyr.2022.07.130) |

As referências dos alunos do IBMEC ainda não foram adicionadas porque os dados bibliográficos e os links dos trabalhos não foram fornecidos. Quando forem enviados, elas poderão ser comparadas com os requisitos do projeto e incluídas na matriz.
