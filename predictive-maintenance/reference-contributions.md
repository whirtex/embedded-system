# Relação das referências com o projeto

Este arquivo registra como cada referência utilizada no artigo de manutenção preditiva contribui para o desenvolvimento do projeto.

## Referências utilizadas

| Referência | O que o trabalho apresenta | Contribuição para o projeto | Limitação considerada |
|---|---|---|---|
| Meitz et al. (2025) | Organiza 249 publicações sobre manutenção preditiva em nove categorias e 73 atributos, incluindo monitoramento de condição, detecção de falhas, degradação, planejamento, dados, prognóstico e avaliação. | Ajuda a estruturar o projeto como um sistema completo, incluindo sensores, tratamento de dados, modelo de previsão, avaliação e apoio à decisão. | É um trabalho de revisão e não apresenta uma comparação experimental própria entre modelos. |
| Gupta et al. (2023) | Analisa dados de vibração coletados em um sistema real de transporte de bagagens. O estudo trata anomalias, limpeza de dados, registros de manutenção e classificação supervisionada. O Random Forest obteve os melhores resultados relatados, com precisão, recall e F1-score de 0,86. | Apoia a escolha de dados de sensores, a necessidade de filtrar ruídos e o cuidado com registros incompletos, rótulos e ausência de histórico completo de falhas. | O estudo não realizou prognóstico de falha até o fim da vida útil e teve limitações de transferência entre diferentes transportadores. |
| Burmeister et al. (2023) | Usa 227.996 observações de produção e inspeção, com 29 variáveis, para comparar redes Bayesianas e árvores de classificação. A configuração CT RUS apresentou os melhores resultados entre os modelos avaliados e gerou regras interpretáveis. | Mostra como incluir dados operacionais e produzir alertas que possam ser entendidos pela equipe de manutenção, em vez de apresentar apenas uma classificação. | Os dados vêm de uma única empresa e a resposta é desbalanceada, portanto a generalização precisa de validação externa. |

## Como as referências orientam a solução

As três referências cobrem partes diferentes do sistema:

1. Meitz et al. orientam a organização geral da arquitetura e da avaliação.
2. Gupta et al. orientam a coleta, a limpeza e o tratamento de dados de sensores em uma situação real.
3. Burmeister et al. orientam a interpretação dos resultados e a transformação das previsões em ações de manutenção.

Com base nesse conjunto, o projeto deve tratar a coleta de dados, o processamento, a detecção de anomalias e a apresentação dos resultados como etapas conectadas. A precisão do modelo não deve ser analisada sem considerar ruído, desbalanceamento, qualidade dos rótulos e possibilidade de uso em outra máquina.

## Registros das referências

- [Meitz et al. (2025)](https://doi.org/10.1016/j.cie.2025.111193)
- [Gupta et al. (2023)](https://doi.org/10.1016/j.cie.2023.109033)
- [Burmeister et al. (2023)](https://doi.org/10.1109/ACCESS.2023.3315842)
