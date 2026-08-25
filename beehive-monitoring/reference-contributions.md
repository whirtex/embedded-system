# Relação das referências com o projeto

Este arquivo registra como cada referência utilizada no artigo de monitoramento de colmeias contribui para o desenvolvimento do projeto.

## Referências já utilizadas no texto

| Referência | O que o trabalho apresenta | Contribuição para o projeto | Limitação ou cuidado |
|---|---|---|---|
| Zheng et al. [1] | Apresenta um sistema IoT com sensores de temperatura e umidade em diferentes pontos da colmeia, sensor de som interno e webcam voltada para a entrada. Usa YOLOv5 e DeepSORT para rastrear abelhas e relaciona a atividade observada com chuva, temperatura e umidade. | Apoia a arquitetura multimodal do projeto, a distribuição dos sensores e o uso de visão computacional para acompanhar a movimentação das abelhas. | Os limites ambientais observados não devem ser tratados como universais sem validação em outras colmeias e condições climáticas. |
| Narcia-Macias et al. [2] | Apresenta o IntelliBeeHive, um sistema de baixo custo para monitoramento da entrada da colmeia com modelos YOLOv7-tiny. O trabalho avalia rastreamento e detecção de pólen. | Apoia a escolha de uma câmera voltada para a entrada e a possibilidade de usar modelos leves para acompanhar abelhas e identificar pólen. | A detecção de Varroa deve ser tratada como prova de conceito, pois os dados eram limitados e parte deles usava dados de preenchimento. |
| Uthoff et al. [3] | Revisa o uso de microfones e acelerômetros para identificar estados da colônia relacionados à presença da rainha e à preparação para enxameação. | Justifica a inclusão de sensores acústicos ou de vibração como parte do monitoramento não invasivo. | O trabalho aponta conjuntos de dados pequenos, falta de métricas padronizadas, diferenças no processamento dos sinais e baixa generalização entre colmeias. |

## Referências adicionais pesquisadas

| Referência | O que o trabalho apresenta | Contribuição para o projeto | Limitação ou cuidado |
|---|---|---|---|
| Tashakkori, Hamza e Crawford (2021) | Apresenta o Beemon, um sistema IoT que coleta temperatura, umidade, peso, áudio e vídeo. Os dados são enviados por MQTT para o ThingsBoard e para um servidor remoto. | Apoia a definição da arquitetura de comunicação, do armazenamento remoto, do dashboard e da operação contínua em ambiente externo. | O artigo descreve principalmente a implementação do sistema e apresenta resultados limitados da operação em campo; isso não substitui a validação de um classificador de saúde da colônia. |
| Henry et al. (2019) | Desenvolve uma rede sem fio para acompanhar temperatura, umidade relativa e acústica dentro das colmeias. O estudo também analisa o uso de Wi-Fi e relaciona alterações nos dados a sinais de estresse, como enxameação. | Apoia o uso de sensores ambientais e acústicos em uma rede sem fio e reforça a necessidade de observar os dados ao longo do tempo. | A dinâmica da colmeia é complexa e os efeitos de diferentes condições de comunicação precisam ser avaliados antes da implantação definitiva. |
| Tu et al. (2016) | Desenvolve um sistema de visão computacional com Raspberry Pi para contar abelhas, identificar posições e medir a atividade de entrada e saída na colmeia. | Apoia o uso de processamento de baixo custo para contar abelhas e medir o fluxo na entrada, além de orientar a definição das métricas de avaliação. | A transferência do método para outras iluminações, câmeras e geometrias de entrada precisa ser validada no projeto. |

## Como as referências orientam a solução

As referências sustentam cinco partes principais do projeto:

1. sensores ambientais distribuídos dentro e fora da colmeia;
2. coleta acústica ou vibroacústica sem abrir a colmeia;
3. câmera voltada para a entrada e análise da movimentação das abelhas;
4. comunicação sem fio, armazenamento remoto e visualização dos dados;
5. avaliação dos modelos com dados rotulados e métricas adequadas.

O projeto deve combinar essas fontes de dados sem assumir que uma única variável seja suficiente para determinar a saúde da colônia. A detecção de pólen, Varroa, presença da rainha ou preparação para enxameação deve ser apresentada como uma hipótese que precisa de dados e validação específicos.

## Registros das referências adicionais

- [Tashakkori, Hamza e Crawford (2021), Beemon](https://doi.org/10.1016/j.compag.2021.106427)
- [Henry et al. (2019), Precision apiculture](https://doi.org/10.1016/j.compag.2018.11.001)
- [Tu et al. (2016), Automatic behaviour analysis system for honeybees using computer vision](https://doi.org/10.1016/j.compag.2016.01.011)

As referências dos alunos do IBMEC ainda não foram incluídas porque os dados bibliográficos e os links dos trabalhos não foram fornecidos.
