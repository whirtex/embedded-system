# Guia geral — projeto de manutenção preditiva

Este arquivo organiza o andamento do projeto **Embedded Systems-based Predictive Maintenance for Air-Conditioning Equipment**. Ele é um checklist de apoio e não substitui as orientações oficiais.

## Fonte prioritária

O arquivo `orientacoes-artigos.pdf` é a fonte de prioridade número 1. Quando houver diferença entre este guia, outro arquivo do repositório, uma anotação ou uma interpretação anterior, deve-se seguir o PDF e, em caso de dúvida, confirmar com o professor. Este documento apenas reorganiza as instruções do PDF e registra o estado específico deste projeto.

## Escopo do projeto

O sistema será voltado ao monitoramento e à manutenção preditiva de aparelhos de ar-condicionado que operam em regime contínuo, 24 horas por dia, em ambientes onde a refrigeração não pode ser interrompida. Exemplos de aplicação incluem enfermarias e UTIs, data centers e salas de servidores, e shelters de telecomunicação.

A restrição a 24 horas é uma decisão de escopo do grupo e também tem justificativa técnica: em regime contínuo o equipamento permanece em condição de operação estável, o que permite estabelecer uma linha de base confiável e evita que transitórios diários de partida e parada sejam confundidos com degradação progressiva. Ficam fora do escopo escolas, escritórios e shopping centers, que operam em horário comercial.

O protótipo deve investigar monitoramento contínuo e detecção antecipada de anomalias. Enquanto não houver histórico representativo de falhas validadas, o artigo não deve afirmar que o sistema estima a vida útil restante do equipamento. Um motor de passo pode ser usado como equipamento-simulador para os testes iniciais, mas isso deve ser declarado como limitação e não como validação de um aparelho de ar-condicionado real.

## Estrutura adotada

O projeto segue as etapas de manutenção preditiva descritas por Meitz et al., que é uma das seis referências específicas. Isso dá ao trabalho uma organização vinda da literatura e permite declarar o que fica de fora, em vez de simplesmente omitir.

| Etapa | Situação | Referência que sustenta |
|---|---|---|
| Monitoramento de condição | No escopo | Yousuf et al., Mohammed et al. |
| Tratamento de dados | No escopo | Gupta et al. |
| Detecção de falhas | No escopo | Kolok et al. |
| Avaliação | No escopo, sem requisito definido ainda | Meitz et al., Gupta et al. |
| Interpretação do alerta | No escopo; acréscimo do grupo, não é etapa do Meitz | Tormos et al. |
| Modelagem de degradação | Fora do escopo | — |
| Prognóstico e vida útil restante | Fora do escopo | — |
| Planejamento da manutenção | Fora do escopo | — |

As três etapas fora do escopo exigem histórico representativo de falhas validadas, que o protótipo não terá.

## Situação atual confirmada

- [x] Título atualizado: `Embedded Systems-based Predictive Maintenance for Air-Conditioning Equipment`.
- [x] Autores e e-mails atualizados no Overleaf.
- [x] Manuscrito compilando no Overleaf sem erros.
- [x] Dez referências acadêmicas encontradas, cadastradas e citadas no artigo.
- [x] Dois primeiros parágrafos da introdução escritos: contexto de sistemas embarcados/IoT e contexto específico de manutenção preditiva em ar-condicionado.
- [x] Quatro parágrafos de trabalhos relacionados escritos com as seis referências estudadas nas AC2 e AC3.
- [x] Foco ajustado para aparelhos de ar-condicionado em ambientes críticos ou coletivos, com operação prolongada.
- [x] As notas verdes do Rigel podem permanecer durante a produção; elas devem ser removidas ou resolvidas na versão final.
- [ ] Introdução completamente concluída: ainda faltam, no momento adequado, o parágrafo sobre a proposta/contribuições e o parágrafo final de organização do artigo.
- [ ] Resumo/Abstract: será escrito posteriormente, conforme o cronograma do PDF, depois que houver resultados.
- [ ] Conferir o limite final de três páginas após retirar as notas verdes e concluir o texto.

## Regras gerais determinadas no PDF

- [ ] Manter o manuscrito no formato do Simpósio Brasileiro de Telecomunicações e Processamento de Sinais (SBrT), com no máximo três páginas.
- [x] Manter dez referências acadêmicas citadas no texto.
- [x] Criar uma referência separada para o repositório, além das dez referências acadêmicas, e citá-la no artigo.
- [x] Manter o repositório público.
- [ ] Colocar no repositório as implementações, documentos e materiais usados no protótipo.
- [ ] Compartilhar o repositório com o professor.
- [ ] Construir a parte física para as demonstrações dos Seminários 2, 3 e 4.
- [ ] Usar o Seminário 1 para apresentar os trabalhos relacionados.

## Cronograma oficial do PDF

| Período | Atividade prevista no PDF |
|---|---|
| Semana 1 — 03 a 07/08 | Formação dos grupos e início do projeto |
| Semana 2 — 10 a 14/08 | AC1 |
| Semana 3 — 17 a 21/08 | AC2 |
| Semana 4 — 24 a 28/08 | AC3 |
| Semana 5 — 31/08 a 04/09 | Seminário 1 — apresentação dos trabalhos relacionados; o cronograma associa esta etapa à AC4 |
| Semana 6 — 07 a 11/09 | AC5 |
| Semana 7 — 14 a 18/09 | Desenvolvimento da Seção III — método |
| Semana 8 — 21 a 25/09 | Resultados iniciais; resumo e conclusões |
| AP1 — 28/09 a 02/10 | Primeira avaliação |
| Semana 9 — 05 a 09/10 | Seminário 2 — problema, método e resultados qualitativos |
| Semana 10 — 12 a 16/10 | Método alternativo e comparação |
| Semana 11 — 19 a 23/10 | Continuação do desenvolvimento |
| Semana 12 — 26 a 30/10 | Seminário 3 — método, protótipo e resultados quantitativos parciais |
| Semanas 13 e 14 — 02 a 13/11 | Finalização |
| AP2 — 16 a 20/11 | Seminário 4 e segunda avaliação |
| Semana 15 — 23 a 27/11 | Ajustes finais |
| AS — 30/11 a 04/12 | Avaliação substitutiva, se aplicável |

### Observação sobre AC4, Seminário 1 e AC5

Na descrição das atividades, a AC4 pede os dois parágrafos de contexto da introdução. No cronograma, a semana seguinte aparece como “Seminário 1 (AC4)”, porque é quando os seis trabalhos relacionados devem ser apresentados. A atividade seguinte é a AC5, que trata do esboço do artigo, dos dois parágrafos finais da introdução e do protótipo. Em caso de conflito de nomenclatura ou data, prevalecem o PDF e a confirmação do professor.

## AC1 — início do projeto

### Organização do grupo e do repositório

- [x] Criar o grupo e registrar os integrantes.
- [x] Criar o repositório público do grupo.
- [x] Criar e organizar a pasta `predictive-maintenance`.
- [ ] Informar ao professor o e-mail de cada integrante para o compartilhamento do Overleaf.
- [ ] Confirmar que todos os integrantes acessam o Overleaf.
- [ ] Compartilhar o repositório com o professor.

### Manuscrito inicial

- [x] Definir e atualizar o título do projeto.
- [x] Atualizar os nomes dos autores no Overleaf.
- [ ] Inserir no `refs.bib` uma entrada BibTeX própria para o repositório, conforme o modelo do PDF.
- [ ] Citar o repositório no texto com `\cite{repo}`, além das dez referências acadêmicas.
- [ ] Conferir se a referência do repositório aparece corretamente na bibliografia.

### Entrega da AC1

- [ ] Baixar do Overleaf o PDF mais recente do manuscrito.
- [ ] Enviar o PDF para `rigel.fernandes@professores.ibmec.edu.br`.
- [ ] Usar o assunto `[IBM3118 AC 2026-2 G3]`.
- [ ] Guardar uma cópia do e-mail enviado.

## AC2 — início da revisão de literatura

O PDF pede um ou dois parágrafos sintetizando pelo menos três referências encontradas no Google Scholar ou em bases reconhecidas, como IEEE Xplore, ACM, Elsevier e JASA. Cada referência deve ser adicionada ao BibTeX com `url` contendo o DOI, e o PDF do artigo deve ser salvo na pasta `refsPDF` do Overleaf. Se uma referência não estiver acessível gratuitamente, deve-se pedir orientação ao professor.

- [x] Selecionar três referências diretamente relacionadas a sistemas embarcados, sensores, motores e processamento.
- [x] Estudar Yousuf et al. (2024), Mohammed et al. (2023) e Kolok et al. (2025).
- [x] Escrever os parágrafos correspondentes no artigo.
- [x] Adicionar as entradas BibTeX com DOI e URL.
- [ ] Adicionar os três PDFs da AC2 à pasta `refsPDF` no Overleaf.
- [ ] Confirmar que todos os integrantes conseguem abrir os PDFs.
- [ ] Realizar ou registrar a entrega da AC2, se ainda não estiver arquivada.

## AC3 — continuação da revisão de literatura

O PDF mantém a mesma lógica da AC2 e pede pelo menos três novas referências. Elas não devem simplesmente repetir as referências da atividade anterior; devem ampliar a revisão e ajudar a fundamentar o sistema.

- [x] Selecionar três novas referências: Meitz et al. (2025), Gupta et al. (2023) e Tormos et al. (2026), esta última substituindo Burmeister et al. (2023) por tratar de ar-condicionado e dispensar rótulo de falha.
- [x] Escrever os dois parágrafos de continuação da revisão.
- [x] Relacionar dados, limpeza, rotulagem, avaliação e interpretação dos alertas ao projeto.
- [x] Adicionar as três novas entradas ao BibTeX com DOI e URL.
- [ ] Baixar os três PDFs da AC3 e adicioná-los à pasta `refsPDF`.
- [ ] Confirmar a disponibilidade dos seis PDFs estudados para todos os integrantes.
- [ ] Realizar ou registrar a entrega da AC3, se ainda não estiver arquivada.

## AC4 — contextualização da introdução

Depois da revisão das seis referências específicas, o PDF pede dois parágrafos de contexto:

1. um parágrafo com o contexto geral do tema, apoiado por pelo menos duas referências;
2. um parágrafo com o problema específico, a motivação, a área de aplicação e o escopo da solução, apoiado por pelo menos duas referências.

Os quatro parágrafos de trabalhos relacionados das AC2 e AC3 devem permanecer depois desses dois parágrafos, com revisão de coerência e conexão com o projeto.

- [x] Escrever o parágrafo geral sobre sistemas embarcados e IoT.
- [x] Escrever o parágrafo específico sobre manutenção preditiva aplicada a ar-condicionado.
- [x] Usar quatro referências gerais de contextualização, duas em cada parágrafo.
- [x] Manter os seis trabalhos específicos na sequência de revisão da literatura.
- [x] Totalizar dez referências acadêmicas no artigo.
- [ ] Adicionar os quatro PDFs de contextualização à pasta `refsPDF`.
- [ ] Revisar a redação das siglas na primeira ocorrência, quando necessário, como IoT, MQTT, RMS e FFT.

## Seminário 1 — trabalhos relacionados

O PDF determina que a apresentação seja sobre os trabalhos já estudados. Deve haver um ou dois slides por referência da revisão das AC2 e AC3, isto é, seis referências. Cada integrante deve apresentar pelo menos uma referência, em aproximadamente um ou dois minutos, destacando resultados qualitativos e quantitativos.

- [ ] Preparar a capa e a motivação do projeto.
- [ ] Criar um ou dois slides para cada uma das seis referências da revisão específica.
- [ ] Mostrar método, contribuição, resultados e limitações de cada trabalho.
- [ ] Explicar como cada artigo influencia o projeto de manutenção preditiva em ar-condicionado.
- [ ] Distribuir os artigos entre Igor, Jorge, Ian e Davi.
- [ ] Ensaiar o tempo e revisar a apresentação.
- [ ] Levar ou enviar os slides conforme a orientação do professor.

## AC5 — esboço, introdução final e protótipo

O PDF pede, após o Seminário 1:

- [ ] Definir o esboço do artigo, com nomes de seções como descrição do sistema, método, resultados e conclusões.
- [ ] Escrever o penúltimo parágrafo da introdução, apresentando a proposta do artigo e as contribuições do grupo.
- [ ] Escrever o último parágrafo da introdução, apresentando a organização do restante do artigo.
- [ ] Iniciar a construção do protótipo com os componentes disponíveis no laboratório.
- [ ] Registrar fotos do protótipo para a avaliação qualitativa.

O Abstract não é uma pendência obrigatória desta etapa. Pelo cronograma do PDF, ele será produzido quando já houver resultados, na Semana 8, e refinado depois.

## Semana 6 — Seção II: desenvolvimento do sistema

Com a introdução pronta, o PDF orienta a escrever a seção de desenvolvimento do sistema:

- [ ] Descrever sensores, microcontroladores e, se aplicável, protocolos de comunicação.
- [ ] Citar as referências que fundamentam as escolhas de hardware e comunicação.
- [ ] Planejar os experimentos e definir a primeira configuração.
- [ ] Continuar a construção do protótipo para a avaliação qualitativa inicial.

Para este projeto, ainda precisam ser definidos e/ou obtidos o acelerômetro, o sensor de corrente, a fonte regulada, o suporte mecânico, o gabinete e a forma de coleta de temperatura. Também é necessário decidir quando o teste usará um aparelho de ar-condicionado real e quando usará um motor de passo como simulador.

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

O PDF pede uma solução alternativa para comparar dois métodos. A comparação deve aparecer na Seção V, com os resultados quantitativos da Seção IV e os resultados qualitativos.

- [ ] Definir um método alternativo.
- [ ] Apresentar os resultados quantitativos e qualitativos da comparação.
- [ ] Criar um gráfico ou uma tabela comparando os métodos.
- [ ] Avaliar, se possível, alguma otimização da solução.

## Dados, falhas e validação do protótipo

Estas decisões são necessárias para executar as etapas do PDF, mas ainda precisam ser definidas pelo grupo:

- [ ] Definir quais sinais serão coletados: temperatura, vibração, corrente e outros sinais disponíveis.
- [ ] Definir frequência de amostragem, duração dos testes e unidade de armazenamento.
- [ ] Definir como as falhas serão aplicadas ou simuladas com segurança.
- [ ] Coletar dados de operação normal.
- [ ] Coletar dados com falhas controladas ou condições anômalas documentadas.
- [ ] Separar dados de treinamento e teste, caso seja usado aprendizado de máquina.
- [ ] Calibrar os sensores.
- [ ] Definir métricas de avaliação.
- [ ] Repetir os testes em condições semelhantes.
- [ ] Registrar limitações e condições do experimento no artigo.

Ainda não está decidido se o sistema usará limites fixos, detecção estatística de anomalias, aprendizado de máquina ou uma comparação entre essas alternativas. Essa decisão deve ser tomada junto com o método, os dados disponíveis e a possibilidade real de validar as falhas.

## Comunicação e MQTT — atividade complementar

O PDF de orientações do artigo não apresenta uma tarefa específica de Mosquitto/MQTT. Portanto, esta seção não deve ser tratada como uma AC obrigatória sem confirmação do professor. Ela pode ser usada como apoio técnico se o grupo escolher MQTT para o protótipo.

- [ ] Confirmar se MQTT fará parte da arquitetura.
- [ ] Testar o Mosquitto localmente.
- [ ] Testar o broker remoto `test.mosquitto.org`, se autorizado.
- [ ] Confirmar com o professor o tópico a ser utilizado.
- [ ] Documentar os testes e os resultados.

## Entrega de cada atividade

Conforme o PDF, para cada atividade o grupo deve enviar a versão mais recente do manuscrito em PDF para `rigel.fernandes@professores.ibmec.edu.br`, usando o assunto `[IBM3118 AC 2026-2 G3]`. O repositório público deve estar atualizado e acessível. A versão enviada deve ser arquivada pelo grupo.

Antes de enviar:

- [ ] Conferir a atividade e o prazo no PDF.
- [ ] Compilar o Overleaf sem erros.
- [ ] Conferir citações, bibliografia, título, autores e número de páginas.
- [ ] Baixar e abrir o PDF gerado.
- [ ] Atualizar o repositório público com a versão correspondente.
- [ ] Enviar o e-mail com o PDF anexado.
- [ ] Guardar a mensagem enviada e o PDF entregue.

## Arquivos do projeto

- `predictive-maintenance.tex`: manuscrito em inglês.
- `predictive-maintenance-pt.md`: tradução de apoio em português.
- `refs.bib`: referências acadêmicas e a entrada do repositório; mesmo nome usado no Overleaf.
- `reference-contributions.md`: contribuição de cada referência para o projeto.
- `requirements.md`: requisitos funcionais e não funcionais.
- `specifications.md`: especificações técnicas preliminares.
- `guia-geral.md`: este guia consolidado, subordinado ao PDF oficial.
- `orientacoes-artigos.pdf`: documento oficial de orientações; fonte prioritária.

