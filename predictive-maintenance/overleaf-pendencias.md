# Pendências no Overleaf

O Overleaf não está sincronizado com o repositório. Tudo o que foi alterado aqui
precisa ser copiado manualmente para lá. Este arquivo registra o que falta fazer.

Última atualização do repositório: commit `e74f374`.

## 1. Substituir o `refs.bib`

Abrir `predictive-maintenance/refs.bib` no repositório, copiar o conteúdo inteiro
e colar por cima do `refs.bib` do Overleaf, apagando o que estava lá.

Isso resolve de uma vez:

- [x] Entrada `@misc{repo}` do repositório, com o título entre chaves duplas para o `ieeetr` não converter para minúsculas
- [x] Remoção da entrada `burmeister2023production`
- [x] Inclusão da entrada `tormos2026hvacxai`

## 2. Substituir o `predictive-maintenance.tex`

Mesma coisa: copiar o arquivo local inteiro e colar por cima do `.tex` do Overleaf.

Isso traz:

- [x] Parágrafo de escopo restrito a operação contínua de 24 horas, com três exemplos
- [x] Frase com `\cite{repo}` depois do último parágrafo de trabalhos relacionados, para o repositório sair como `[11]`
- [x] `\bibliography{refs}` no lugar do `\IfFileExists`
- [x] Parágrafo do Tormos no lugar do parágrafo do Burmeister

## 3. Compilar duas vezes

- [x] Clicar em Recompile duas vezes seguidas

A primeira passada roda o LaTeX, a segunda incorpora o BibTeX. Compilando só uma
vez, as citações saem como `[?]`.

## 4. Conferir o resultado

- [x] A lista de referências termina com onze entradas
- [x] O Tormos aparece como `[6]`, entre Gupta e Gubbi
- [x] O repositório aparece como `[11]`, no fim da lista
- [x] Não sobrou nenhuma menção a Burmeister nem a IEEE Access

Se ainda aparecer Burmeister, algum dos dois arquivos não foi colado.

## 5. Subir os PDFs para `refsPDF`

- [x] Tormos et al., 2026 — baixar em <https://www.mdpi.com/1999-4893/19/7/586> (acesso aberto, CC BY 4.0, sem login)
- [x] Apagar o PDF do Burmeister, se estiver na pasta
- [x] Os quatro PDFs de contextualização, pendência da AC4
- [x] Os três PDFs da AC3

## Observação

Se o `refs.bib` ou o `.tex` do Overleaf tiverem alguma alteração feita apenas lá,
que não esteja no repositório, ela será perdida ao colar por cima. Nesse caso,
conferir antes o que existe só no Overleaf.
