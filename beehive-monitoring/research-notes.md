# Research notes — beehive monitoring

Este arquivo registra, para cada referência, o que ela mostrou, onde ela falha e qual
papel exerce no artigo. Serve para escrever sem reler os PDFs e para não atribuir a
uma referência mais do que ela sustenta.

O sistema proposto é uma estação de baixo custo que fotografa a entrada da colmeia em
horário fixo, mede temperatura e umidade dentro e fora, grava tudo localmente e conta
as abelhas visíveis por janela, fora do equipamento. As decisões estão em
`decisoes-do-projeto.md`.

## Matriz de evidências

### Referências específicas, das AC2 e AC3

| Chave | Estudo e acesso | Evidência principal e limitação | Papel no artigo |
|---|---|---|---|
| `zheng2024intelligent` | Sensores de temperatura e umidade no centro, na margem, na entrada e no ambiente da colmeia, mais sensor de som interno e câmera voltada para a entrada. Rastreamento com YOLOv5 e DeepSORT. | Alcançou 83,5% ± 0,7 de MOTA e 77,3% ± 0,2 de MOTP, a até 16 quadros por segundo. É um sistema de rastreio contínuo, com a câmera sempre ligada, o que não se aplica a uma estação que dorme entre janelas. | Sustenta a imagem da entrada e a distribuição dos pontos de temperatura entre interior, entrada e ambiente. É também a referência que justifica **não** prometer rastreio individual. |
| `narciamacias2024intellibeehive` | IntelliBeeHive, de baixo custo, com YOLOv7-tiny para detecção de abelhas, pólen e *Varroa*. | 96,28% de acurácia de rastreamento e F1-score de 0,8319 na detecção de pólen. Os próprios autores relatam que os dados de *Varroa* eram insuficientes e em parte fictícios. | Sustenta a viabilidade de detecção leve na entrada. A ressalva sobre *Varroa* é o que fundamenta tirar essa detecção do escopo em vez de prometê-la. |
| `uthoff2023acoustic` | Revisão do uso de microfones e acelerômetros para inferir estados da colônia, como presença da rainha e preparação de enxameação. | Aponta relações promissoras entre sinais da colônia e esses estados, mas registra conjuntos de dados pequenos, ausência de métricas padronizadas, engenharia de atributos inconsistente e baixa generalização entre colônias. | Fundamenta deixar áudio, vibração, rainha e enxameação **fora** do escopo, com motivo declarado em vez de omissão. |
| `tashakkori2021beemon` | Beemon: arquitetura com temperatura, umidade, peso, áudio e vídeo, comunicação MQTT, painel ThingsBoard e armazenamento remoto. | Demonstra a viabilidade de integrar várias modalidades e manter um fluxo histórico. É uma arquitetura conectada, que pressupõe rede disponível no apiário. | É o contraponto da decisão de arquitetura: o projeto guarda localmente **em vez** de transmitir. Também sustenta a exclusão do peso da colmeia. |
| `henry2019precision` | Rede de sensores sem fio para medição contínua de temperatura, umidade relativa e acústica dentro de colmeias, em apiário real. | Mostra aquisição contínua em campo funcionando. Depende de infraestrutura de rede, que é justamente o que falta no cenário do projeto. | Junto com Tashakkori, sustenta a medição contínua e serve de base para a variante com Wi-Fi, caso ela seja desenvolvida. |
| `tu2016automatic` | Monitoramento da entrada por visão computacional em Raspberry Pi, com subtração de fundo, contando abelhas e estimando entradas e saídas. | R² de 0,987 na contagem, 0,953 na atividade de entrada e 0,888 na de saída. O desempenho varia com iluminação, posição da câmera, geometria da entrada e sobreposição de abelhas. | É a referência mais próxima do método do projeto: contagem por imagem em plataforma barata, validada contra contagem manual. Sustenta a métrica escolhida e o procedimento de validação. |

### Referências gerais, da AC4

| Chave | Estudo | Papel no artigo |
|---|---|---|
| `hung2018pollinators` | Importância dos polinizadores, com a abelha *Apis mellifera* entre os polinizadores de cultivo mais observados, e variação da relevância conforme o contexto ecológico. | Primeiro parágrafo da introdução, contexto geral. |
| `brown2009conservation` | Pressões sobre as populações de abelhas: perda de habitat, espécies invasoras, doenças emergentes, exposição a pesticidas e clima. | Primeiro parágrafo, motivação da observação contínua. |
| `demicco2020embedded` | Revisão de sistemas embarcados, suas restrições de tempo de processamento, confiabilidade, consumo, tamanho e custo, e a relação com IoT e computação de borda. | Segundo parágrafo e abertura da Seção II. A restrição de consumo é o que amarra a agenda de captura. |
| `ray2018iotarchitectures` | Levantamento de arquiteturas de IoT, com dispositivos, sensores, protocolos, serviços e camadas de processamento. | Segundo parágrafo e abertura da Seção II. |

## Por que estas seis específicas

As seis cobrem camadas complementares do problema: **imagem da entrada** em Zheng,
Narcia-Macias e Tu; **medição ambiental contínua** em Zheng e Henry; **arquitetura de
aquisição e armazenamento** em Tashakkori e Henry; e **os limites do que se pode
afirmar** em Uthoff e Narcia-Macias.

Esse último ponto é o que sustenta a parte mais defensável do artigo. Três das seis
referências relatam explicitamente as próprias limitações — dados insuficientes de
*Varroa*, conjuntos pequenos, ausência de métrica padronizada. É com base nelas que o
projeto declara o que fica de fora, em vez de omitir.

## Métricas: o que se aplica e o que não

O artigo deve reportar **erro de contagem** e **R²**, seguindo Tu et al., porque o
sistema conta abelhas visíveis por janela.

**MOTA e MOTP não se aplicam.** São métricas de rastreamento multiobjeto, usadas por
Zheng et al. porque o sistema deles segue cada abelha entre quadros. Como a câmera do
projeto fica desligada entre as janelas, não existe trajetória a avaliar. Reportar
MOTA seria medir algo que o sistema não faz.

## Registros primários

- Zheng et al.: <https://doi.org/10.1016/j.atech.2024.100584>
- Narcia-Macias et al.: <https://doi.org/10.1109/ICMLA61862.2024.00122>
- Uthoff et al.: <https://doi.org/10.1016/j.compag.2022.107589>
- Tashakkori et al.: <https://doi.org/10.1016/j.compag.2021.106427>
- Henry et al.: <https://doi.org/10.1016/j.compag.2018.11.001>
- Tu et al.: <https://doi.org/10.1016/j.compag.2016.01.011>

Os dados completos de cada entrada estão em `refs.bib`, e a relação detalhada entre
cada artigo e as decisões do projeto está em `reference-contributions.md`.
