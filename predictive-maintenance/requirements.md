# Requisitos do sistema

Este documento reúne os requisitos iniciais para um protótipo de sistema embarcado de manutenção preditiva. A lista foi elaborada com base no objetivo do projeto e nos componentes disponíveis na faculdade.

## Escopo do projeto

O sistema será desenvolvido para monitorar aparelhos de ar-condicionado que operam em regime contínuo, 24 horas por dia, em ambientes nos quais a refrigeração não pode ser interrompida, como enfermarias e UTIs, data centers e salas de servidores, e shelters de telecomunicação. A operação em regime contínuo é um pressuposto do método: ela permite estabelecer uma linha de base estável e evita que transitórios de partida e parada sejam confundidos com degradação. A primeira versão terá como objetivo detectar anomalias e emitir alertas; a estimativa da vida útil restante dependerá da obtenção de um histórico representativo de falhas validadas.

## Legenda

- Disponível: componente ou recurso disponível na faculdade.
- Parcial: há algum componente relacionado, mas ainda falta uma confirmação ou um complemento.
- Ausente: o item não foi identificado entre os componentes disponíveis na faculdade e deve ser confirmado com o professor.

## Requisitos funcionais

Os requisitos estão agrupados pelas etapas de manutenção preditiva descritas por
Meitz et al., a mesma estrutura adotada no artigo. As etapas de modelagem de
degradação, prognóstico e planejamento da manutenção ficam fora do escopo do
protótipo, porque dependem de um histórico representativo de falhas validadas.

### Monitoramento de condição

Medir o equipamento e levar a medição até onde ela será usada.

| Código | Requisito | Situação |
|---|---|---|
| RF01 | O sistema deve coletar dados da máquina continuamente. | Parcial. A frequência de coleta ainda precisa ser definida. |
| RF02 | O sistema deve medir temperatura e umidade. | Disponível. Há um módulo DHT11. |
| RF03 | O sistema deve medir a vibração do motor. | Ausente. É necessário solicitar um acelerômetro, como MPU6050 ou ADXL345. |
| RF04 | O sistema deve medir o esforço ou o peso aplicado ao equipamento. | Disponível. Há uma célula de carga de 50 kg e um módulo HX711. |
| RF05 | O sistema deve medir o consumo de corrente do motor. | Ausente. Seria necessário um sensor ACS712 ou INA219. |
| RF06 | O sistema deve possuir uma máquina ou um motor para realizar os testes. | Parcial. Há um motor de passo e um driver, mas não foram identificados suporte mecânico, carga ou estrutura de teste. |
| RF12 | O sistema deve enviar as medições para outro dispositivo ou plataforma. | Parcial. Há ESP8266, ESP32-CAM, Ethernet e LoRa. A proposta é MQTT, seguindo Mohammed et al. O MQTT transporta a medição, mas não notifica pessoas: isso é tratado no RF18. |
| RF14 | O sistema deve testar os sensores ao ser ligado. | Será implementado no software. |
| RF15 | O sistema deve identificar uma falha ou desconexão de sensor. | Será implementado no software. |

### Tratamento de dados

Organizar, filtrar e separar o que será usado para treinar e para testar.

| Código | Requisito | Situação |
|---|---|---|
| RF07 | O sistema deve filtrar e processar os dados dos sensores. | Será implementado no software. |
| RF11 | O sistema deve armazenar o histórico das medições. | Ausente. Não foi identificado um módulo de cartão SD. Como alternativa, os dados podem ser armazenados em um servidor pela rede. |
| RF17 | O sistema deve manter separados os dados de operação normal, falha, treinamento e teste. | Será implementado no procedimento de coleta e validação. |

### Detecção de falhas

Distinguir operação normal de anomalia.

| Código | Requisito | Situação |
|---|---|---|
| RF08 | O sistema deve identificar o funcionamento normal e uma possível falha. | A definir. É necessário escolher entre limites fixos e um modelo de aprendizado de máquina. |
| RF13 | O sistema deve permitir a configuração dos limites de alerta. | Parcial. Há botões, potenciômetros e teclado, mas a forma de configuração ainda precisa ser definida. |

### Interpretação e ação

Informar o que motivou o alerta e permitir uma resposta.

| Código | Requisito | Situação |
|---|---|---|
| RF09 | O sistema deve emitir um alerta local quando detectar uma anomalia. | Disponível. Há LEDs, buzzer e display LCD. |
| RF18 | O sistema deve enviar uma notificação remota a cada alerta, de forma que a equipe de manutenção seja avisada sem estar no local. | A definir. A proposta é usar um bot do Telegram: o ESP32 faz uma requisição à API do Telegram, que entrega a notificação aos celulares cadastrados. Exige acesso à internet, não apenas à rede local. |
| RF16 | O sistema deve registrar quais variáveis ou condições motivaram cada alerta. | Será implementado no software. A forma de explicação ainda precisa ser definida. |
| RF19 | A notificação remota deve informar qual medição motivou o alerta, e não apenas que houve anomalia. | A definir. Depende do RF16. |
| RF10 | O sistema deve permitir o desligamento ou o acionamento de um dispositivo em caso de falha. | Parcial. Há módulos relé, mas a função e as condições de acionamento ainda precisam ser definidas. |

### Avaliação

Nenhum requisito funcional foi definido para esta etapa. Meitz et al. tratam
avaliação como categoria própria, e Gupta et al. mostram na prática que métrica
e separação de dados decidem se o resultado se sustenta. Falta definir quais
métricas serão reportadas e como os conjuntos de treino e teste serão separados.

## Requisitos não funcionais

| Código | Requisito | Situação |
|---|---|---|
| RNF01 | O sistema deve operar com baixa tensão e sem oferecer risco ao usuário. | Parcial. Há conectores de pilhas, mas ainda não foi confirmada uma fonte regulada adequada. |
| RNF02 | O sistema deve ser alimentado por fonte regulada de 5 V ligada à rede elétrica, e não por pilhas ou bateria. | Ausente. É necessário obter uma fonte de 5 V com corrente suficiente para o microcontrolador e os sensores. A operação de 24 horas inviabiliza alimentação por pilha. |
| RNF03 | O ponto de alimentação deve estar disponível junto ao equipamento monitorado. | A definir. A unidade externa do ar-condicionado raramente tem tomada próxima, e puxar energia de dentro do próprio aparelho exige eletricista. |
| RNF04 | O sistema deve funcionar continuamente durante os testes, reproduzindo o regime ininterrupto do equipamento monitorado. | A duração dos testes ainda precisa ser definida. |
| RNF05 | As leituras dos sensores devem ter precisão suficiente para identificar anomalias. | O nível de precisão precisa ser definido com o professor. |
| RNF06 | O sistema deve apresentar o alerta dentro de um tempo adequado. | O tempo máximo de resposta precisa ser definido. |
| RNF07 | O sistema deve ser modular, permitindo trocar ou adicionar sensores. | Parcial. Há protoboards, jumpers e vários módulos. |
| RNF08 | O sistema deve possuir documentação de montagem e funcionamento. | A documentação deverá ser produzida durante o projeto. |
| RNF09 | O sistema deve ter baixo custo e usar, de preferência, os componentes disponíveis. | Parcial. A maior parte da montagem pode usar os componentes disponíveis. |
| RNF10 | O sistema deve possuir proteção física para os circuitos. | Ausente. Não foi identificada uma caixa ou um gabinete de proteção. |
| RNF11 | O sistema deve permitir repetir os testes em condições semelhantes. | Parcial. Ainda falta definir o suporte, a carga mecânica e o procedimento de teste. |
| RNF12 | O sistema deve registrar a frequência de coleta, unidades, calibração e contexto de cada medição. | Será documentado durante a implementação. |

## Relação com a literatura

- Yousuf et al. e Mohammed et al. apoiam o monitoramento conjunto de temperatura, vibração e grandezas elétricas, além de alertas e comunicação remota.
- Kolok et al. apoiam a extração de características como RMS e FFT e a detecção leve de anomalias em um ESP32.
- Meitz et al. e Gupta et al. mostram que coleta, limpeza, rotulagem e avaliação precisam fazer parte do mesmo fluxo.
- Tormos et al. apoiam aprender a linha de base saudável sem rótulo de falha e informar qual medição disparou o alerta.
- As chaves BibTeX e os dados completos das dez referências acadêmicas, mais a entrada do repositório, estão em `refs.bib`.

## Perguntas para o professor

1. Qual tipo de falha o projeto deverá detectar?
2. O projeto precisa medir vibração obrigatoriamente?
3. O sensor de corrente será necessário?
4. Será usado um motor real ou apenas um motor de passo para simulação?
5. O sistema deve apenas emitir um alerta ou também desligar o motor?
6. Os dados precisam ser enviados para uma aplicação web?
7. Qual frequência de amostragem deve ser usada?
8. Qual precisão mínima será exigida?
9. O projeto precisa usar aprendizado de máquina ou pode usar limites fixos?
10. Será necessário comprar os sensores que não estão entre os componentes disponíveis na faculdade?
11. O projeto deve funcionar com bateria ou com fonte externa?
12. Será necessário construir um gabinete e uma estrutura mecânica?
13. O objetivo da primeira versão é detectar anomalias, classificar falhas ou estimar a vida útil restante?
14. Como as condições normais e as falhas controladas serão produzidas e validadas com segurança?
