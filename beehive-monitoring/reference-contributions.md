# Contribuição das referências para o projeto

A lista foi elaborada com base no objetivo do projeto e nos componentes disponíveis na faculdade. Este arquivo relaciona as dez referências acadêmicas selecionadas com a arquitetura, os requisitos e as especificações do sistema de monitoramento inteligente de colmeias.

## Matriz de contribuição

| Ref. | Trabalho | Contribuição para o projeto | Limitação ou cuidado |
|---|---|---|---|
| [1] | Zheng et al., *Intelligent beehive monitoring system based on internet of things and colony state analysis* | Apoia a arquitetura multimodal com temperatura, umidade, som interno e câmera na entrada. O uso de YOLOv5 e DeepSORT orienta o rastreamento e a análise da atividade das abelhas. | As faixas de temperatura e umidade observadas não devem ser tratadas como limites universais sem validação em outras colmeias e condições climáticas. |
| [2] | Narcia-Macias et al., *IntelliBeeHive: An Automated Honey Bee, Pollen, and Varroa Destructor Monitoring System* | Apoia o uso de uma câmera voltada para a entrada, processamento de baixo custo e modelos leves, como YOLOv7-tiny, para rastrear abelhas e detectar pólen. | A detecção de Varroa deve ser apresentada como prova de conceito, pois o próprio trabalho informa limitações nos dados de ácaros e o uso de dados de preenchimento. |
| [3] | Uthoff et al., *Acoustic and vibration monitoring of honeybee colonies for beekeeping-relevant aspects of presence of queen bee and swarming* | Justifica a coleta de áudio e vibração como forma não invasiva de acompanhar a presença da rainha e possíveis sinais de enxameação. | A revisão aponta conjuntos de dados pequenos, falta de métricas padronizadas, diferenças no processamento dos sinais e baixa generalização entre colmeias. |
| [4] | Tashakkori, Hamza e Crawford, *Beemon: An IoT-based beehive monitoring system* | Orienta a coleta contínua de temperatura, umidade, peso, áudio e vídeo, além da comunicação MQTT, do armazenamento remoto e da visualização em dashboard. | A implementação de monitoramento não substitui a validação de um classificador de saúde da colônia em condições reais. |
| [5] | Henry et al., *Precision apiculture: Development of a wireless sensor network for honeybee hives* | Apoia o uso de uma rede sem fio para sensores ambientais e acústicos e reforça a importância de analisar os dados ao longo do tempo para identificar alterações associadas a estresse ou enxameação. | O alcance, a estabilidade e o consumo da comunicação sem fio devem ser avaliados no ambiente da faculdade antes da implantação definitiva. |
| [6] | Tu et al., *Automatic behaviour analysis system for honeybees using computer vision* | Apoia o processamento de visão computacional em plataforma de baixo custo para contar abelhas e medir o fluxo de entrada e saída. Também orienta o uso de contagens manuais como referência de avaliação. | O desempenho pode variar com iluminação, câmera, posicionamento e geometria da entrada; por isso, o método precisa ser validado com os componentes disponíveis. |
| [7] | Hung et al., *The worldwide importance of honey bees as pollinators in natural habitats* | Fundamenta a importância ecológica e agrícola da abelha-europeia e ajuda a contextualizar por que o acompanhamento das colônias é relevante. | A importância da abelha pode variar conforme o habitat e a região; o artigo não define um método de monitoramento embarcado. |
| [8] | Brown e Paxton, *The conservation of bees: a global perspective* | Contextualiza ameaças como perda de habitat, espécies invasoras, doenças, pesticidas e mudanças climáticas, motivando observação contínua das abelhas. | É uma revisão geral sobre conservação e não fornece parâmetros de sensores ou limites para diagnóstico. |
| [9] | De Micco et al., *A review on embedded systems* | Fundamenta o uso de sistemas embarcados como plataformas para funções específicas e relaciona o projeto às restrições de processamento, confiabilidade, consumo de energia, tamanho e custo. | É uma revisão geral; não define qual microcontrolador ou sensor deve ser usado na colmeia. |
| [10] | Ray, *A survey on Internet of Things architectures* | Fundamenta a integração entre dispositivos, sensores, protocolos, comunicação, serviços e processamento em uma arquitetura IoT. | É uma revisão de arquiteturas gerais; a escolha do protocolo e da plataforma precisa ser validada no ambiente do projeto. |

## Relação com os requisitos e as especificações

| Parte do projeto | Referências que dão suporte | Aplicação prevista |
|---|---|---|
| Monitoramento de temperatura e umidade | [1], [4] e [5] | Instalar sensores em pontos relevantes, registrar as medições com data e hora e acompanhar a variação ambiental dentro e fora da colmeia. |
| Monitoramento acústico ou de vibração | [1], [3], [4] e [5] | Coletar sinais sem abrir a colmeia e investigar indicadores de presença da rainha, estresse e enxameação. |
| Observação da entrada da colmeia | [1], [2] e [6] | Usar a câmera para contar abelhas, estimar o fluxo de entrada e saída e, quando houver dados suficientes, investigar a presença de pólen. |
| Comunicação e acesso remoto | [1], [4] e [5] | Enviar os dados por comunicação sem fio para armazenamento e visualização remota, considerando a frequência de coleta definida para o projeto. |
| Processamento e avaliação | [1], [2] e [6] | Priorizar modelos leves e medir o desempenho com dados rotulados, contagens de referência e métricas apropriadas. |
| Interpretação da saúde da colônia | [1], [3], [4] e [5] | Combinar sinais ambientais, acústicos e visuais para gerar indícios, sem afirmar um diagnóstico definitivo sem validação experimental. |
| Contextualização ecológica | [7] e [8] | Justificar a relevância do monitoramento de abelhas a partir da importância da polinização e das ameaças às populações. |
| Sistemas embarcados e IoT | [9] e [10] | Fundamentar a integração de sensores e processamento em dispositivos embarcados conectados a uma arquitetura IoT. |

## Síntese para o desenvolvimento

As seis referências específicas sustentam uma solução que combina sensores ambientais, coleta acústica ou vibroacústica, câmera na entrada, processamento local e comunicação sem fio. As quatro referências gerais complementam essa base ao justificar a importância da conservação das abelhas e a adoção de sistemas embarcados conectados por uma arquitetura IoT. A literatura também indica que a arquitetura deve preservar os dados brutos, registrar o contexto das medições e permitir validação posterior, pois uma variável isolada não é suficiente para determinar a saúde da colônia.

No escopo atual, a detecção de pólen, Varroa, presença da rainha e preparação para enxameação deve ser tratada como uma hipótese ou funcionalidade experimental. A confirmação desses eventos exige dados representativos, rotulagem adequada e testes em mais de uma colmeia e condição de operação.

## Registros bibliográficos verificados

| Ref. | Tipo e publicação | DOI / registro |
|---|---|---|
| [1] | Artigo — *Smart Agricultural Technology*, v. 9, art. 100584, 2024 | [10.1016/j.atech.2024.100584](https://doi.org/10.1016/j.atech.2024.100584) |
| [2] | Artigo de conferência — *2024 International Conference on Machine Learning and Applications (ICMLA)*, p. 845--850, 2024 | [10.1109/ICMLA61862.2024.00122](https://doi.org/10.1109/ICMLA61862.2024.00122) · [registro IEEE](https://ieeexplore.ieee.org/document/10903284/) |
| [3] | Artigo de revisão — *Computers and Electronics in Agriculture*, v. 205, art. 107589, 2023 | [10.1016/j.compag.2022.107589](https://doi.org/10.1016/j.compag.2022.107589) |
| [4] | Artigo — *Computers and Electronics in Agriculture*, v. 190, art. 106427, 2021 | [10.1016/j.compag.2021.106427](https://doi.org/10.1016/j.compag.2021.106427) |
| [5] | Artigo — *Computers and Electronics in Agriculture*, v. 156, p. 138--144, 2019 | [10.1016/j.compag.2018.11.001](https://doi.org/10.1016/j.compag.2018.11.001) |
| [6] | Artigo — *Computers and Electronics in Agriculture*, v. 122, p. 10--18, 2016 | [10.1016/j.compag.2016.01.011](https://doi.org/10.1016/j.compag.2016.01.011) · [registro da Aarhus University](https://pure.au.dk/portal/da/publications/automatic-behaviour-analysis-system-for-honeybees-using-computer-/) |
| [7] | Artigo — *Proceedings of the Royal Society B: Biological Sciences*, v. 285, n. 1870, art. 20172140, 2018 | [10.1098/rspb.2017.2140](https://doi.org/10.1098/rspb.2017.2140) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/29321298/) |
| [8] | Artigo de revisão — *Apidologie*, v. 40, p. 410--416, 2009 | [10.1051/apido/2009019](https://doi.org/10.1051/apido/2009019) |
| [9] | Artigo de revisão — *IEEE Latin America Transactions*, v. 18, n. 2, p. 188--205, 2020 | [10.1109/TLA.2020.9085271](https://doi.org/10.1109/TLA.2020.9085271) · [repositório PUCRS](https://repositorio.pucrs.br/dspace/handle/10923/18526) |
| [10] | Artigo de revisão — *Journal of King Saud University - Computer and Information Sciences*, v. 30, n. 3, p. 291--319, 2018 | [10.1016/j.jksuci.2016.10.003](https://doi.org/10.1016/j.jksuci.2016.10.003) |

As referências dos alunos do IBMEC ainda não foram adicionadas porque os dados bibliográficos e os links dos trabalhos não foram fornecidos. Quando forem enviados, elas poderão ser comparadas com os requisitos do projeto e incluídas na matriz.
