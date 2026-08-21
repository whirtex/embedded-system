# Requisitos do sistema

Este documento reúne os requisitos iniciais para um protótipo de sistema embarcado de manutenção preditiva. A lista foi elaborada com base no objetivo do projeto e nos componentes disponíveis na faculdade.

## Legenda

- Disponível: componente ou recurso disponível na faculdade.
- Parcial: há algum componente relacionado, mas ainda falta uma confirmação ou um complemento.
- Ausente: o item não foi identificado entre os componentes disponíveis na faculdade e deve ser confirmado com o professor.

## Requisitos funcionais

| Código | Requisito | Situação |
|---|---|---|
| RF01 | O sistema deve coletar dados da máquina continuamente. | Parcial. A frequência de coleta ainda precisa ser definida. |
| RF02 | O sistema deve medir temperatura e umidade. | Disponível. Há um módulo DHT11. |
| RF03 | O sistema deve medir a vibração do motor. | Ausente. É necessário solicitar um acelerômetro, como MPU6050 ou ADXL345. |
| RF04 | O sistema deve medir o esforço ou o peso aplicado ao equipamento. | Disponível. Há uma célula de carga de 50 kg e um módulo HX711. |
| RF05 | O sistema deve medir o consumo de corrente do motor. | Ausente. Seria necessário um sensor ACS712 ou INA219. |
| RF06 | O sistema deve possuir uma máquina ou um motor para realizar os testes. | Parcial. Há um motor de passo e um driver, mas não foram identificados suporte mecânico, carga ou estrutura de teste. |
| RF07 | O sistema deve filtrar e processar os dados dos sensores. | Será implementado no software. |
| RF08 | O sistema deve identificar o funcionamento normal e uma possível falha. | A definir. É necessário escolher entre limites fixos e um modelo de aprendizado de máquina. |
| RF09 | O sistema deve emitir um alerta quando detectar uma anomalia. | Disponível. Há LEDs, buzzer e display LCD. |
| RF10 | O sistema deve permitir o desligamento ou o acionamento de um dispositivo em caso de falha. | Parcial. Há módulos relé, mas a função e as condições de acionamento ainda precisam ser definidas. |
| RF11 | O sistema deve armazenar o histórico das medições. | Ausente. Não foi identificado um módulo de cartão SD. Como alternativa, os dados podem ser armazenados em um servidor pela rede. |
| RF12 | O sistema deve enviar os dados para outro dispositivo ou plataforma. | Parcial. Há ESP8266, ESP32-CAM, Ethernet e LoRa, mas o protocolo e o destino ainda não foram definidos. |
| RF13 | O sistema deve permitir a configuração dos limites de alerta. | Parcial. Há botões, potenciômetros e teclado, mas a forma de configuração ainda precisa ser definida. |
| RF14 | O sistema deve testar os sensores ao ser ligado. | Será implementado no software. |
| RF15 | O sistema deve identificar uma falha ou desconexão de sensor. | Será implementado no software. |

## Requisitos não funcionais

| Código | Requisito | Situação |
|---|---|---|
| RNF01 | O sistema deve operar com baixa tensão e sem oferecer risco ao usuário. | Parcial. Há conectores de pilhas, mas ainda não foi confirmada uma fonte regulada adequada. |
| RNF02 | O sistema deve funcionar continuamente durante os testes. | A duração dos testes ainda precisa ser definida. |
| RNF03 | As leituras dos sensores devem ter precisão suficiente para identificar anomalias. | O nível de precisão precisa ser definido com o professor. |
| RNF04 | O sistema deve apresentar o alerta dentro de um tempo adequado. | O tempo máximo de resposta precisa ser definido. |
| RNF05 | O sistema deve ser modular, permitindo trocar ou adicionar sensores. | Parcial. Há protoboards, jumpers e vários módulos. |
| RNF06 | O sistema deve possuir documentação de montagem e funcionamento. | A documentação deverá ser produzida durante o projeto. |
| RNF07 | O sistema deve ter baixo custo e usar, de preferência, os componentes disponíveis. | Parcial. A maior parte da montagem pode usar os componentes disponíveis. |
| RNF08 | O sistema deve possuir proteção física para os circuitos. | Ausente. Não foi identificada uma caixa ou um gabinete de proteção. |
| RNF09 | O sistema deve permitir repetir os testes em condições semelhantes. | Parcial. Ainda falta definir o suporte, a carga mecânica e o procedimento de teste. |

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
