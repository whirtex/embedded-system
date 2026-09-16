# Decisões do projeto

## Escopo da primeira versão

- O sistema usará uma câmera para observar a entrada da colmeia.
- Serão usados dois sensores de temperatura e umidade.
- O sensor acústico poderá ser considerado em uma etapa posterior.
- Sensores de vibração e peso ficarão fora do escopo da primeira versão.
- A inteligência artificial fará apenas a detecção e a contagem das abelhas visíveis nas imagens.
- O sistema estimará a atividade das abelhas na entrada da colmeia.
- O sistema não deverá afirmar que identifica entradas e saídas individuais, doenças, ausência da rainha ou enxameação.

## Sensores de temperatura e umidade

- Serão usados dois sensores:
  - um dentro da colmeia;
  - um do lado de fora, próximo à entrada.
- O sensor interno será protegido por uma capa ventilada, permitindo a passagem do ar sem deixar a parte eletrônica exposta ao contato direto com as abelhas.
- O sensor interno receberá energia e enviará os dados por um cabo até a eletrônica instalada do lado de fora.
- Os sensores farão uma leitura a cada 3 minutos.

## Câmera

- A câmera será instalada do lado de fora da colmeia.
- Ela ficará acima e um pouco à frente da entrada, apontada para o local onde as abelhas entram e saem.
- A instalação terá suporte firme e proteção contra chuva.
- A câmera não deverá bloquear a entrada nem interferir na ventilação da colmeia.
- A resolução inicial será de 1280 × 720.
- A câmera funcionará em horário predefinido, das 7h às 17h.
- Serão testadas duas configurações:
  - 5 segundos de captura a 10 quadros por segundo, a cada 5 minutos;
  - 10 segundos de captura a 10 quadros por segundo, a cada 5 minutos.
- Cada configuração será testada durante 3 dias.
- As duas configurações serão comparadas pela qualidade da contagem, pelo espaço ocupado no cartão e pelo consumo de energia.
- As imagens serão salvas como uma sequência de arquivos JPEG, em vez de vídeos H.264 ou H.265.
- As imagens originais serão mantidas durante os testes para permitir novas análises.

## Placa e armazenamento

- A placa confirmada com o hardware na mão é uma **ESP32-WROVER-DEV v1.6**, com módulo ESP32-WROVER-E, e a câmera **OV2640** separada, ligada pelo conector flat.
- A placa tem micro-USB e conversor CH340C embutidos, então grava firmware direto pelo cabo, sem adaptador FTDI.
- O módulo WROVER-E tem PSRAM, necessária para a câmera trabalhar em 1280 × 720.
- A placa **não tem slot de cartão microSD**. Será necessário um módulo leitor avulso, ligado aos pinos do header.
- A placa central deverá receber os dados dos dois sensores e gravar as imagens e as medições no mesmo cartão.
- Será usado um cartão microSD de 32 GB, de uma marca confiável.
- Os dados serão coletados aproximadamente uma vez por semana.
- As imagens serão organizadas em pastas por data e terão o horário registrado no nome do arquivo.
- As medições serão registradas em um arquivo CSV contendo data, hora, temperatura interna, umidade interna, temperatura externa, umidade externa e, se possível, nível da bateria.
- Será usado um relógio de tempo real para manter a data e a hora mesmo quando não houver Wi-Fi.

## Comunicação e análise

- O sistema não dependerá de Wi-Fi para funcionar.
- As imagens e os dados ambientais serão armazenados localmente no cartão microSD.
- Os dados serão retirados ou copiados uma vez por semana e levados para análise em um computador.
- LoRa não será necessário na primeira versão.
- A análise das imagens será feita posteriormente, fora da colmeia.
- Será testado primeiro um modelo de inteligência artificial já existente.
- Se o modelo pronto não apresentar resultado suficiente nas imagens do projeto, será criado ou ajustado um modelo com imagens próprias.
- A inteligência artificial contará as abelhas visíveis em cada imagem ou janela de observação.
- A análise não tentará acompanhar a mesma abelha entre janelas diferentes, porque a câmera ficará desligada entre as capturas.

## Alimentação

- O sistema usará um mini painel solar.
- A potência inicialmente escolhida para o painel é de aproximadamente 3 W.
- Será usada uma bateria recarregável 18650 de aproximadamente 2600 mAh.
- A bateria deverá possuir proteção BMS ou ser usada com um circuito de proteção adequado.
- O sistema também precisará de um controlador de carga solar e de um regulador de tensão.
- A bateria, o controlador, o regulador e a placa ficarão em uma caixa externa protegida contra chuva e umidade.

## Decisões ainda pendentes

Agrupadas por tema. Enquanto um item estiver aqui, o artigo não deve afirmar nada
sobre ele.

### Análise das imagens

- Definir o modelo de detecção que será testado primeiro. As referências do projeto
  usam três caminhos diferentes: YOLOv5 com DeepSORT em Zheng et al., YOLOv7-tiny em
  Narcia-Macias et al., e subtração de fundo em Tu et al. O último é o mais leve e o
  que mais se aproxima do que o projeto precisa, já que a contagem é por janela e não
  há rastreio entre janelas.
- Definir a quantidade de imagens necessária para testar ou ajustar o modelo.
- Produzir contagens manuais de referência, que são o padrão de comparação.
- Separar os conjuntos de treino, validação e teste, caso o modelo seja ajustado com
  imagens próprias.
- Escolher as métricas que serão reportadas. Erro de contagem e R² são os candidatos
  diretos, seguindo Tu et al. MOTA e MOTP não se aplicam, porque medem rastreio.
- Definir o critério final para considerar a contagem adequada.

### Hardware e alimentação

- Confirmar se o cartão de 32 GB funciona com a placa e em que formato deve estar.
- Escolher o controlador de carga solar e o regulador de tensão.
- Medir o consumo real da placa, da câmera, do cartão e dos sensores.
- Medir a autonomia real da bateria de 2600 mAh nas duas configurações de captura.
- Confirmar a disponibilidade do painel solar de 3 W e da bateria.

### Instalação na colmeia

- Definir a capa ventilada do sensor interno, a passagem do cabo e a vedação.
- Confirmar a colmeia, o local e as condições em que os testes serão realizados.

### Variante com Wi-Fi

- Decidir se será desenvolvida uma segunda versão da estação, com transmissão por
  Wi-Fi, para apiários onde a colmeia fica perto de uma rede. A versão offline
  continua sendo a principal. Ver a seção do método alternativo em `guia-geral.md`.
