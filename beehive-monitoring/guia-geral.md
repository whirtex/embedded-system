# Guia geral — projeto de monitoramento de colmeias

Este arquivo organiza o andamento do projeto **Low-Cost Embedded System for Beehive Monitoring**. Ele é um checklist de apoio e não substitui as orientações oficiais.

Os itens marcados foram comprovados pelos arquivos, pelo histórico do repositório e pelas confirmações do grupo em 1º e 3 de setembro de 2026. A apresentação do Seminário 1 foi realizada em 2 de setembro de 2026. Atividades externas que não puderam ser verificadas, como a inclusão dos PDFs acadêmicos e o envio do PDF por e-mail, permanecem desmarcadas.

## Fonte prioritária

O arquivo `orientacoes-artigo.pdf`, na raiz do repositório, é a fonte de prioridade número 1. Quando houver diferença entre este guia, outro arquivo do repositório, uma anotação ou uma interpretação anterior, deve-se seguir o PDF e, em caso de dúvida, confirmar com o professor. Este documento apenas reorganiza as instruções do PDF e registra o estado específico deste projeto.

## Escopo do projeto

Uma estação de baixo custo instalada na colmeia, com uma câmera apontada para a entrada e dois sensores de temperatura e umidade. O sistema **não usa rede**: grava tudo em um cartão microSD, que é recolhido uma vez por semana e analisado depois em um computador.

A análise se limita a contar as abelhas visíveis em cada janela de observação, como indicador de atividade na entrada. Como a câmera fica desligada entre as janelas, o artigo não deve afirmar que o sistema acompanha uma mesma abelha entre janelas diferentes.

Os detalhes estão em `decisoes-do-projeto.md`: resolução, horários, intervalos de leitura, posição dos sensores e alimentação. O plano de montagem está em `plano-do-prototipo.md`.

## Estrutura adotada

O projeto declara explicitamente o que fica de fora, em vez de omitir. Cada decisão se apoia em uma das referências já estudadas.

| Função | Situação | Referência que sustenta |
|---|---|---|
| Imagem da entrada | No escopo | Zheng et al., Narcia-Macias et al. |
| Contagem das abelhas visíveis | No escopo | Tu et al., Narcia-Macias et al. |
| Temperatura e umidade, interna e externa | No escopo | Zheng et al., Henry et al. |
| Armazenamento local e registro de horário | No escopo | Tashakkori et al. |
| Validação contra contagem manual | No escopo | Tu et al. |
| Rastreio de abelha individual entre janelas | Fora do escopo | Zheng et al. |
| Áudio e vibração | Fora do escopo | Uthoff et al. |
| Detecção de pólen | Fora do escopo | Narcia-Macias et al. |
| Detecção de *Varroa* | Fora do escopo | Narcia-Macias et al. |
| Presença da rainha e enxameação | Fora do escopo | Uthoff et al. |
| Peso da colmeia | Fora do escopo | Tashakkori et al. |
| Transmissão remota por MQTT | Fora do escopo nesta versão | Tashakkori et al., Henry et al. |

As exclusões não são omissões: o rastreio individual é impossível com a câmera desligada entre janelas, e as demais exigem sensores ou dados rotulados que a primeira versão não tem. A Narcia-Macias et al. relatam que os dados de *Varroa* eram insuficientes e em parte fictícios, o que reforça tratar essa detecção como prova de conceito e não como capacidade validada.

## Situação atual confirmada

- [x] Título consolidado: `Low-Cost Embedded System for Beehive Monitoring`.
- [x] Grupo e número confirmados: Grupo 4, Ibmec Barra, Rio de Janeiro–RJ.
- [x] Autores e e-mails atualizados no Overleaf.
- [x] Overleaf compartilhado com todos os integrantes.
- [x] Manuscrito compilando no Overleaf sem erros.
- [x] Dez referências acadêmicas encontradas, cadastradas e citadas no artigo.
- [x] Entrada BibTeX do repositório criada e citada no texto.
- [x] Dois primeiros parágrafos da introdução escritos: contexto dos polinizadores e contexto de sistemas embarcados e IoT.
- [x] Quatro parágrafos de trabalhos relacionados escritos com as seis referências estudadas nas AC2 e AC3.
- [x] Introdução completamente concluída: o penúltimo parágrafo, com a proposta e as quatro contribuições, e o último parágrafo, com a visita guiada pelas seções.
- [x] Seção II escrita, com os componentes e o planejamento dos experimentos.
- [x] Texto novo colado no `sbrt2026.tex` do Overleaf e recompilado.
- [ ] Resumo/Abstract: será escrito posteriormente, conforme o cronograma do PDF, depois que houver resultados.
- [x] Protótipo de bancada funcionando: DHT11 e relógio DS1302 no Arduino Uno, gerando na porta serial o CSV com data, hora, temperatura e umidade.
- [x] Fotos do protótipo registradas em `assets/`, incluindo a captura da saída em CSV.
- [x] Primeiro código no repositório, em `firmware/`.
- [x] AC5 e AC6 entregues por e-mail em 15 de setembro de 2026, com o PDF e duas imagens do protótipo.
- [ ] Conferir o limite de três páginas após retirar as notas verdes e concluir o texto.

## Regras gerais determinadas no PDF

- [x] Manter o projeto associado a um problema real identificado pelo grupo.
- [ ] Manter o manuscrito no formato do Simpósio Brasileiro de Telecomunicações e Processamento de Sinais (SBrT), com no máximo três páginas.
- [x] Manter dez referências acadêmicas citadas no texto.
- [x] Criar uma referência separada para o repositório, além das dez referências acadêmicas, e citá-la no artigo.
- [x] Manter o repositório público.
- [x] Colocar no repositório as implementações, documentos e materiais usados no protótipo. Primeiros sketches em `firmware/` e fotos em `assets/`.
- [x] Compartilhar o repositório com o professor.
- [ ] Construir a parte física para as demonstrações dos Seminários 2, 3 e 4.
- [x] Usar o Seminário 1 para apresentar os trabalhos relacionados.

## Cronograma oficial do PDF

| Período | Atividade prevista no PDF |
|---|---|
| Semana 1 — 03 a 07/08 | Formação dos grupos e início do projeto |
| Semana 2 — 10 a 14/08 | AC1 |
| Semana 3 — 17 a 21/08 | AC2 |
| Semana 4 — 24 a 28/08 | AC3 |
| Semana 5 — 31/08 a 04/09 | Seminário 1, que o cronograma associa à AC4 |
| Semana 6 — 07 a 11/09 | AC5 |
| Semana 7 — 14 a 18/09 | em branco no PDF |
| Semana 8 — 21 a 25/09 | em branco no PDF |
| AP1 — 28/09 a 02/10 | Prova escrita |
| Semana 9 — 05 a 09/10 | Seminário 2 |
| Semana 10 — 12 a 16/10 | em branco no PDF |
| Semana 11 — 19 a 23/10 | em branco no PDF |
| Semana 12 — 26 a 30/10 | Seminário 3 |
| Semana 13 — 02 a 06/11 | em branco no PDF |
| Semana 14 — 09 a 13/11 | em branco no PDF |
| AP2 — 16 a 20/11 | Seminário 4 |
| Semana 15 — 23 a 27/11 | em branco no PDF |
| AS — 30/11 a 04/12 | Avaliação substitutiva |

O calendário do PDF deixa várias semanas em branco. As descrições das atividades, porém, continuam: depois da AC5 vêm a AC6 e, em seguida, quatro blocos que o próprio PDF chama de Semana 7, Semana 8, Semana 9 e Semana 10. Esses rótulos são os do documento e não correspondem necessariamente às semanas do calendário. Este guia usa os rótulos do PDF, para não criar uma numeração própria.

### Observação sobre AC4, Seminário 1 e AC5

Na descrição das atividades, a AC4 pede os dois parágrafos de contexto da introdução e a elaboração dos slides. No cronograma, a semana seguinte aparece como “Seminário 1 (AC4)”, porque é quando os seis trabalhos relacionados devem ser apresentados. A AC5 reúne a apresentação presencial, o outline do artigo, os dois parágrafos finais da introdução e o início do protótipo. A AC6 trata da Seção II. Em caso de conflito de nomenclatura ou data, prevalecem o PDF e a confirmação do professor.

A entrega da AC5, originalmente prevista para 08/09, foi adiada pelo professor, e a AC5 e a AC6 passaram a ser entregues juntas.

## AC1 — início do projeto

### Organização do grupo e do repositório

- [x] Definir os integrantes e confirmar o número do grupo.
- [x] Criar o repositório público do grupo.
- [x] Criar e organizar a pasta `beehive-monitoring`.
- [x] Informar ao professor o e-mail de cada integrante para o compartilhamento do Overleaf.
- [x] Confirmar que todos os integrantes acessam o Overleaf.
- [x] Confirmar que todos os integrantes acessam o repositório.
- [x] Compartilhar o repositório com o professor.

### Manuscrito inicial

- [x] Definir e atualizar o título do projeto.
- [x] Atualizar os nomes e os e-mails dos autores no Overleaf.
- [x] Inserir no `refs.bib` uma entrada BibTeX própria para o repositório, conforme o modelo do PDF.
- [x] Citar o repositório no texto com `\cite{repo}`, além das dez referências acadêmicas.
- [ ] Conferir no PDF compilado se a referência do repositório aparece corretamente.

### Entrega da AC1

- [ ] Baixar do Overleaf o PDF mais recente do manuscrito.
- [ ] Enviar o PDF para `rigel.fernandes@professores.ibmec.edu.br`.
- [ ] Usar o assunto `[IBM3118 AC 2026-2 G4]`.
- [ ] Guardar uma cópia do e-mail enviado.

## AC2 — início da revisão de literatura

O PDF pede um ou dois parágrafos sintetizando pelo menos três referências encontradas no Google Scholar ou em bases reconhecidas, como IEEE Xplore, ACM, Elsevier e JASA. Cada referência deve ser adicionada ao BibTeX com `url` contendo o DOI, e o PDF do artigo deve ser salvo na pasta `refsPDF` do Overleaf. Se uma referência não estiver acessível gratuitamente, deve-se pedir orientação ao professor.

- [x] Selecionar três referências diretamente relacionadas ao monitoramento de colmeias.
- [x] Estudar Zheng et al. (2024), Narcia-Macias et al. (2024) e Uthoff et al. (2023).
- [x] Escrever os parágrafos correspondentes no artigo, com método, resultados e limitações.
- [x] Adicionar as entradas BibTeX com DOI no campo `url`.
- [x] Não utilizar no texto nenhuma referência que o grupo não tenha lido e verificado.
- [ ] Adicionar os três PDFs da AC2 à pasta `refsPDF` no Overleaf.
- [ ] Confirmar que todos os integrantes conseguem abrir os PDFs.
- [ ] Realizar ou registrar a entrega da AC2, se ainda não estiver arquivada.

## AC3 — continuação da revisão de literatura

O PDF mantém a mesma lógica da AC2 e pede pelo menos três novas referências. Elas não devem repetir as da atividade anterior; devem ampliar a revisão e ajudar a fundamentar o sistema.

- [x] Selecionar três novas referências: Tashakkori et al. (2021), Henry et al. (2019) e Tu et al. (2016).
- [x] Escrever os dois parágrafos de continuação da revisão.
- [x] Relacionar aquisição contínua, armazenamento, processamento local e validação ao projeto.
- [x] Adicionar as três novas entradas ao BibTeX com DOI.
- [ ] Baixar os três PDFs da AC3 e adicioná-los à pasta `refsPDF`.
- [ ] Confirmar a disponibilidade dos seis PDFs estudados para todos os integrantes.
- [ ] Realizar ou registrar a entrega da AC3, se ainda não estiver arquivada.

## AC4 — contextualização da introdução

Depois da revisão das seis referências específicas, o PDF pede dois parágrafos de contexto:

1. um parágrafo com o contexto geral do tema, apoiado por pelo menos duas referências;
2. um parágrafo com o problema específico, a motivação, a área de aplicação e o escopo da solução, apoiado por pelo menos duas referências.

Os quatro parágrafos de trabalhos relacionados das AC2 e AC3 devem permanecer depois desses dois parágrafos, com revisão de coerência e conexão com o projeto. Orientação complementar dada em sala: quatro referências gerais nos dois primeiros parágrafos, duas em cada.

- [x] Escrever o parágrafo geral sobre polinizadores e as pressões sobre as colônias.
- [x] Escrever o parágrafo específico sobre inspeção manual, sistemas embarcados e IoT.
- [x] Usar quatro referências gerais de contextualização, duas em cada parágrafo.
- [x] Manter os seis trabalhos específicos na sequência de revisão da literatura.
- [x] Totalizar dez referências acadêmicas no artigo.
- [x] Evitar apresentar faixas observadas em um artigo como regras universais.
- [x] Evitar afirmar que a detecção de *Varroa* está validada quando os dados forem insuficientes.
- [x] Preparar os slides da apresentação, um por artigo, além dos slides iniciais e finais.
- [ ] Adicionar os quatro PDFs de contextualização à pasta `refsPDF`.
- [ ] Revisar a redação das siglas na primeira ocorrência, quando necessário, como IoT, MOTA, MOTP e F1-score.

## Seminário 1 — trabalhos relacionados

O PDF determina que a apresentação seja sobre os trabalhos já estudados, com um ou dois slides por referência das AC2 e AC3, isto é, seis referências. Orientação dada em sala: um slide por artigo. Cada integrante deve apresentar pelo menos uma referência, destacando resultados qualitativos e quantitativos. A ordem das apresentações segue a ordem de envio dos slides por e-mail.

- [x] Preparar a capa e os slides de contexto e motivação.
- [x] Criar um slide para cada uma das seis referências da revisão específica.
- [x] Mostrar método, contribuição, resultados e limitações de cada trabalho.
- [x] Explicar como cada artigo influencia o projeto de monitoramento de colmeias.
- [x] Manter no final os nomes completos e os links das referências.
- [x] Apresentar no Seminário 1 — realizado em 2 de setembro de 2026.
- [ ] Conferir se os links DOI dos slides estão corretos e clicáveis.
- [ ] Registrar o envio dos slides por e-mail, se ainda não estiver arquivado.

## AC5 — Seminário 1, esboço, introdução final e protótipo

O PDF divide a AC5 em três frentes: a atividade presencial do Seminário 1, a parte escrita e a construção do protótipo.

### Atividade presencial

- [x] Apresentar as seis referências da revisão, usando os slides elaborados na AC4.

### Parte escrita

- [x] Definir o esboço do artigo, com os nomes das cinco seções: Introduction, System Description, The Method, Results e Conclusion. As seções já existem no `.tex`, cada uma com o seu `\label`.
- [x] Escrever o penúltimo parágrafo da introdução, apresentando a proposta do artigo e as contribuições do grupo.
- [x] Escrever o último parágrafo da introdução, apresentando a organização do restante do artigo.
- [ ] Verificar as referências produzidas por alunos do Ibmec e citá-las caso seja oportuno.

### Protótipo

- [x] Iniciar a construção do protótipo com os componentes disponíveis no laboratório.
- [x] Registrar fotos do protótipo para a avaliação qualitativa.

O Abstract não é uma pendência obrigatória desta etapa. Pelo cronograma do PDF, ele será produzido quando já houver resultados e refinado depois.

## AC6 — Seção II: desenvolvimento do sistema

Com a introdução pronta, o PDF orienta a escrever a seção de desenvolvimento do sistema, com uma referência dando suporte a cada componente apresentado.

- [x] Descrever a câmera, os sensores, o armazenamento local e o relógio de tempo real.
- [x] Descrever a alimentação por painel solar e bateria.
- [x] Citar as referências que fundamentam as escolhas de cada componente.
- [x] Planejar os experimentos e definir a configuração da primeira rodada.
- [x] Continuar a construção do protótipo para a avaliação qualitativa inicial.

A subseção que descrevia o MQTT foi substituída por armazenamento local e operação offline, para bater com a decisão registrada em `decisoes-do-projeto.md`.

## Semana 7 — Seção III: método

- [ ] Descrever detalhadamente o funcionamento do sistema, sem repetir a revisão bibliográfica.
- [ ] Criar um diagrama do método, preferencialmente no Lucidchart, exportando-o em PDF e cortando os espaços em branco.
- [ ] Incluir pseudocódigo, se ele ajudar a explicar o processamento.
- [ ] Escrever um parágrafo que apresente e explique o diagrama.
- [ ] Escrever um parágrafo que apresente e explique a foto do protótipo.
- [ ] Continuar a montagem para a primeira avaliação quantitativa.

## Semana 8 — resultados, resumo e conclusões iniciais

- [ ] Registrar resultados qualitativos do protótipo.
- [ ] Registrar os primeiros resultados quantitativos, se já houver dados suficientes.
- [ ] Escrever o Abstract.
- [ ] Escrever as conclusões iniciais com base nos resultados disponíveis.

## Semana 9 — refinamento dos resultados

- [ ] Continuar a coleta e a análise dos resultados quantitativos.
- [ ] Refinar o Abstract.
- [ ] Fazer a última linha do Abstract apresentar um resultado interessante que represente a principal contribuição do grupo.
- [ ] Refinar as conclusões, resumindo a avaliação do sistema embarcado.

## Semana 10 — método alternativo e comparação

O PDF pede uma solução alternativa para comparar dois métodos, com a comparação na Seção V.

Este projeto já tem três comparações candidatas, e qualquer uma atende ao pedido:

- as duas configurações de captura, cinco e dez segundos por janela, cada uma testada por três dias;
- o modelo de detecção pronto contra um modelo ajustado com imagens próprias;
- **duas variantes da estação: a offline, com cartão microSD, e uma segunda com Wi-Fi**, para apiários onde a colmeia fica perto de uma rede. Ideia do grupo, ainda não decidida.

A terceira é a que mais se parece com o que o PDF chama de solução alternativa, porque compara dois caminhos para o mesmo problema em vez de dois ajustes do mesmo caminho. Ela também aproveita Tashakkori et al. e Henry et al., que já estão citados no artigo e usam justamente aquisição em rede. O custo é ter de montar e validar dois sistemas em vez de um, e a variante com Wi-Fi depende de cobertura no local de teste.

- [ ] Decidir se a variante com Wi-Fi será desenvolvida.
- [ ] Escolher qual das três comparações será apresentada como método alternativo.
- [ ] Apresentar os resultados quantitativos e qualitativos da comparação.
- [ ] Criar um gráfico ou uma tabela comparando os métodos.
- [ ] Avaliar, se possível, alguma otimização da solução.

## Dados e validação do protótipo

Decisões necessárias para executar as etapas do PDF, algumas já fechadas em `decisoes-do-projeto.md`:

- [x] Definir os sinais coletados: imagens da entrada, temperatura e umidade internas e externas.
- [x] Definir a frequência: janela de imagens a cada cinco minutos, das 7h às 17h; sensores a cada três minutos.
- [x] Definir a unidade de armazenamento: cartão microSD de 32 GB, com pastas por data e horário no nome do arquivo.
- [x] Definir o formato do registro ambiental: CSV com data, hora, temperatura e umidade internas e externas, e nível da bateria.
- [x] Decidir manter as imagens originais durante os testes, para permitir nova análise.
- [ ] Definir o modelo de detecção que será testado primeiro.
- [ ] Definir a quantidade de imagens necessária para testar ou ajustar o modelo.
- [ ] Produzir contagens manuais de referência para comparação.
- [ ] Definir as métricas de avaliação e o critério para considerar a contagem adequada.
- [ ] Separar dados de treino e teste, caso o modelo seja ajustado com imagens próprias.
- [ ] Confirmar a colmeia, o local e as condições dos testes.
- [ ] Medir o consumo real e a autonomia da bateria nas duas configurações de captura.
- [ ] Registrar limitações e condições do experimento no artigo.

## Comunicação e MQTT — atividade complementar

O PDF de orientações do artigo não apresenta uma tarefa específica de Mosquitto/MQTT. Esta seção registra a atividade prática apresentada em sala e não deve ser tratada como uma AC obrigatória sem confirmação do professor.

O sistema desta primeira versão é offline, então o MQTT não faz parte da arquitetura. A atividade continua valendo como exercício da disciplina e como base caso a transmissão remota seja adotada mais adiante.

- [ ] Verificar se o Mosquitto e os clientes `mosquitto_sub` e `mosquitto_pub` estão instalados.
- [ ] Iniciar o broker localmente e testar com dois terminais.
- [ ] Testar o broker remoto `test.mosquitto.org`, se autorizado.
- [ ] Registrar os comandos utilizados e o resultado dos dois testes.
- [ ] Confirmar com o professor qual tópico deve ser usado no teste local. O texto do slide informa `ibmec/test`, enquanto os comandos mostrados na parte inferior usam `iotbr/esp32` com `localhost`.

### Comandos do teste local

```bash
mosquitto_sub -h localhost -t ibmec/test
mosquitto_pub -h localhost -t ibmec/test -m "Hello there!"
```

### Comandos do teste remoto

```bash
mosquitto_sub -h test.mosquitto.org -t iotbr/esp32
mosquitto_pub -h test.mosquitto.org -t iotbr/esp32 -m "Hello there!"
```

## Entrega de cada atividade

Conforme o PDF, para cada atividade o grupo deve enviar a versão mais recente do manuscrito em PDF para `rigel.fernandes@professores.ibmec.edu.br`, usando o assunto `[IBM3118 AC 2026-2 G4]`. O repositório público deve estar atualizado e acessível. A versão enviada deve ser arquivada pelo grupo.

Antes de enviar:

- [ ] Conferir a atividade e o prazo no PDF.
- [ ] Atualizar o `sbrt2026.tex` e o `refs.bib` do Overleaf com a versão do repositório.
- [ ] Compilar o Overleaf duas vezes, para o BibTeX entrar.
- [ ] Conferir citações, bibliografia, título, autores e número de páginas.
- [ ] Baixar e abrir o PDF gerado.
- [ ] Atualizar o repositório público e enviar os commits ao remoto.
- [ ] Enviar o e-mail com o PDF anexado, e com os slides quando a atividade pedir apresentação.
- [ ] Guardar a mensagem enviada e o PDF entregue.

## Arquivos do projeto

- `beehive-monitoring.tex`: manuscrito em inglês; corresponde ao `sbrt2026.tex` do Overleaf.
- `beehive-monitoring-pt.md`: tradução de apoio em português.
- `refs.bib`: referências acadêmicas e a entrada do repositório; mesmo nome usado no Overleaf.
- `reference-contributions.md`: contribuição de cada referência para o projeto.
- `research-notes.md`: matriz de evidências, com o que cada referência mostrou, onde ela falha e o papel dela no artigo.
- `requirements.md`: requisitos funcionais e não funcionais.
- `specifications.md`: especificações técnicas preliminares.
- `decisoes-do-projeto.md`: decisões de projeto já fechadas pelo grupo.
- `plano-do-prototipo.md`: o que montar, em que ordem, o que pegar no laboratório e o que comprar.
- `retirada-de-materiais.pdf`: folha entregue ao professor para a retirada dos componentes. Gerado a partir do plano; está no `.gitignore`.
- `firmware/`: os sketches do protótipo, um por pasta, no formato que o Arduino IDE espera.
- `assets/`: fotos do protótipo e imagens do projeto.
- `guia-geral.md`: este guia consolidado, subordinado ao PDF oficial.
- `orientacoes-artigo.pdf`: documento oficial de orientações, na raiz do repositório; fonte prioritária.
