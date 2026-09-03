"""Gera o deck do Seminario 1 — trabalhos relacionados."""

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.oxml.ns import qn
from pptx.util import Emu, Inches, Pt

SAIDA = "seminario-1-trabalhos-relacionados.pptx"

FUNDO = RGBColor(0xF7, 0xF9, 0xFB)
TEXTO = RGBColor(0x16, 0x20, 0x2A)
SECUNDARIO = RGBColor(0x5A, 0x6B, 0x7A)
FRIO = RGBColor(0x1B, 0x6E, 0x8C)
QUENTE = RGBColor(0xD9, 0x7A, 0x28)
LINHA = RGBColor(0xDC, 0xE4, 0xEA)
CAIXA_FRIA = RGBColor(0xFF, 0xFF, 0xFF)
CAIXA_QUENTE = RGBColor(0xEC, 0xF3, 0xF7)
BRANCO = RGBColor(0xFF, 0xFF, 0xFF)

FONTE = "Arial"
L, A = Inches(13.333), Inches(7.5)
MARGEM = Inches(0.9)
UTIL = L - 2 * MARGEM


def retangulo(slide, x, y, cx, cy, cor):
    from pptx.enum.shapes import MSO_SHAPE

    forma = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, cx, cy)
    forma.fill.solid()
    forma.fill.fore_color.rgb = cor
    forma.line.fill.background()
    forma.shadow.inherit = False
    forma.text_frame.text = ""
    return forma


def texto(slide, x, y, cx, cy, conteudo, tamanho, cor=TEXTO,
          negrito=False, espaco=1.15, alinha=PP_ALIGN.LEFT, ancora=MSO_ANCHOR.TOP):
    caixa = slide.shapes.add_textbox(x, y, cx, cy)
    tf = caixa.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = ancora
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0

    linhas = conteudo if isinstance(conteudo, list) else [conteudo]
    for i, linha in enumerate(linhas):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = alinha
        p.line_spacing = espaco
        if i:
            p.space_before = Pt(10)
        r = p.add_run()
        r.text = linha
        r.font.size = Pt(tamanho)
        r.font.bold = negrito
        r.font.color.rgb = cor
        r.font.name = FONTE
    return caixa


def topicos(slide, x, y, cx, cy, itens, tamanho=17):
    """Lista com marcador e recuo pendurado."""
    caixa = slide.shapes.add_textbox(x, y, cx, cy)
    tf = caixa.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0

    recuo = Inches(0.28)
    for i, item in enumerate(itens):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.line_spacing = 1.2
        if i:
            p.space_before = Pt(11)

        pPr = p._pPr
        pPr.set("marL", str(recuo))
        pPr.set("indent", str(-recuo))

        # marcador nativo, para o recuo pendurado alinhar no PowerPoint
        cor = pPr.makeelement(qn("a:buClr"), {})
        cor.append(pPr.makeelement(qn("a:srgbClr"), {"val": "1B6E8C"}))
        pPr.append(cor)
        pPr.append(pPr.makeelement(qn("a:buFont"), {"typeface": "Arial"}))
        pPr.append(pPr.makeelement(qn("a:buChar"), {"char": "•"}))

        r = p.add_run()
        r.text = item
        r.font.size = Pt(tamanho)
        r.font.color.rgb = TEXTO
        r.font.name = FONTE
    return caixa


def slide_base(prs, camada=None):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    retangulo(s, 0, 0, L, A, FUNDO)
    if camada:
        retangulo(s, 0, 0, L, Inches(0.16), FRIO)
        texto(s, MARGEM, Inches(0.34), UTIL, Inches(0.3),
              camada.upper(), 12, FRIO, negrito=True)
    return s


def rodape(slide, esquerda, direita):
    y = A - Inches(0.62)
    retangulo(slide, MARGEM, y - Inches(0.16), UTIL, Emu(9525), LINHA)
    texto(slide, MARGEM, y, UTIL * 0.6, Inches(0.3), esquerda, 12, SECUNDARIO)
    texto(slide, MARGEM + UTIL * 0.6, y, UTIL * 0.4, Inches(0.3),
          direita, 12, SECUNDARIO, alinha=PP_ALIGN.RIGHT)


# ---------------------------------------------------------------- 1. capa
def capa(prs):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    retangulo(s, 0, 0, L, A, FUNDO)
    retangulo(s, 0, 0, Inches(0.28), A, FRIO)
    retangulo(s, 0, A - Inches(1.9), Inches(0.28), Inches(1.9), QUENTE)

    texto(s, Inches(1.5), Inches(1.6), Inches(10.5), Inches(0.4),
          "SEMINÁRIO 1 · TRABALHOS RELACIONADOS", 15, FRIO, negrito=True)
    texto(s, Inches(1.5), Inches(2.25), Inches(10.6), Inches(2.0),
          "Manutenção preditiva de aparelhos de ar-condicionado em operação contínua",
          40, TEXTO, negrito=True, espaco=1.1)
    retangulo(s, Inches(1.5), Inches(4.35), Inches(1.6), Inches(0.05), QUENTE)
    texto(s, Inches(1.5), Inches(4.75), Inches(10.5), Inches(0.9),
          ["Igor Costa · Jorge Alves · Ian Dias · Davi Ito",
           "Ibmec, Rio de Janeiro · IBM3118 · 2026.2 · Grupo 3"],
          19, SECUNDARIO, espaco=1.3)


# ----------------------------------------------------------- 2. motivação
def motivacao(prs):
    s = slide_base(prs, "Motivação")
    texto(s, MARGEM, Inches(1.05), UTIL, Inches(0.9),
          "Começou pelas áreas com pacientes", 36, TEXTO, negrito=True)
    retangulo(s, MARGEM, Inches(1.85), Inches(1.6), Inches(0.05), QUENTE)
    texto(s, MARGEM, Inches(2.15), UTIL, Inches(0.5),
          "Aparelhos instalados nos ambientes onde há paciente o tempo todo.",
          19, SECUNDARIO)

    ambientes = [
        ("Enfermarias e quartos",
         "O aparelho fica ligado dia e noite. Parar significa remanejar quem está internado."),
        ("UTIs e leitos críticos",
         "O paciente não tem condição de ser removido, e a temperatura do ambiente faz parte do cuidado."),
        ("Pronto-socorro",
         "Ocupação contínua e imprevisível. O equipamento quase nunca é desligado para manutenção."),
    ]
    larg = (UTIL - Inches(0.5)) / 3
    for i, (titulo, corpo) in enumerate(ambientes):
        x = MARGEM + i * (larg + Inches(0.25))
        retangulo(s, x, Inches(2.95), larg, Inches(2.6), CAIXA_FRIA)
        retangulo(s, x, Inches(2.95), larg, Inches(0.07), FRIO)
        texto(s, x + Inches(0.3), Inches(3.3), larg - Inches(0.6), Inches(0.8),
              titulo, 20, TEXTO, negrito=True)
        texto(s, x + Inches(0.3), Inches(4.15), larg - Inches(0.6), Inches(1.3),
              corpo, 16, SECUNDARIO, espaco=1.25)

    texto(s, MARGEM, Inches(5.85), UTIL, Inches(0.9),
          "O desgaste desses aparelhos aparece antes da parada, na vibração do compressor, "
          "na corrente do motor e na temperatura de operação.",
          20, TEXTO, espaco=1.3)
    rodape(s, "Seminário 1 · Trabalhos relacionados", "2 / 11")


# --------------------------------------------------- 3. outros locais
def outros_locais(prs):
    s = slide_base(prs, "Alcance")
    texto(s, MARGEM, Inches(1.05), UTIL, Inches(0.9),
          "O mesmo problema aparece fora do hospital", 36, TEXTO, negrito=True)
    retangulo(s, MARGEM, Inches(1.85), Inches(1.6), Inches(0.05), QUENTE)
    texto(s, MARGEM, Inches(2.15), UTIL, Inches(0.5),
          "O critério é operação ininterrupta somada a uma parada que custa mais que o reparo.",
          19, SECUNDARIO)

    locais = [
        ("Data centers e salas de servidores",
         "A refrigeração é o ponto único de falha. Sem ela, o hardware desliga por temperatura."),
        ("Laboratórios refrigerados",
         "Reagentes e amostras fora de faixa invalidam resultados e perdem-se em silêncio."),
        ("Centros de operações e emergência",
         "Salas do 190 e do 193 nunca desligam. Se o equipamento cai, o atendimento cai junto."),
        ("Aeroportos e rodoviárias",
         "Terminais abertos o tempo todo. A manutenção precisa acontecer sem interromper a operação."),
    ]
    larg = (UTIL - Inches(0.4)) / 2
    alt = Inches(1.5)
    for i, (titulo, corpo) in enumerate(locais):
        x = MARGEM + (i % 2) * (larg + Inches(0.4))
        y = Inches(2.8) + (i // 2) * (alt + Inches(0.22))
        retangulo(s, x, y, larg, alt, CAIXA_FRIA)
        retangulo(s, x, y, Inches(0.07), alt, FRIO)
        texto(s, x + Inches(0.4), y + Inches(0.22), larg - Inches(0.8), Inches(0.4),
              titulo, 19, TEXTO, negrito=True)
        texto(s, x + Inches(0.4), y + Inches(0.72), larg - Inches(0.8), Inches(0.7),
              corpo, 16, SECUNDARIO, espaco=1.2)

    texto(s, MARGEM, Inches(6.25), UTIL, Inches(0.5),
          "Muda a consequência da parada. O equipamento e o método continuam os mesmos.",
          18, TEXTO, espaco=1.25)
    rodape(s, "Seminário 1 · Trabalhos relacionados", "3 / 11")


# ---------------------------------------------------------------- 3. mapa
def mapa(prs):
    s = slide_base(prs, "Como organizamos a leitura")
    texto(s, MARGEM, Inches(1.05), UTIL, Inches(0.9),
          "Seis trabalhos, três camadas", 36, TEXTO, negrito=True)
    retangulo(s, MARGEM, Inches(1.85), Inches(1.6), Inches(0.05), QUENTE)
    texto(s, MARGEM, Inches(2.15), UTIL, Inches(0.5),
          "Cada camada responde a uma pergunta diferente do nosso projeto.",
          19, SECUNDARIO)

    camadas = [
        ("MEDIR", "Como instrumentar o equipamento e levar o dado até uma decisão.",
         "[1] Yousuf et al., 2024\n[2] Mohammed et al., 2023"),
        ("DETECTAR", "Como separar operação normal de anomalia com hardware barato.",
         "[3] Kolok et al., 2025"),
        ("CONFIAR", "Como garantir que o resultado se sustenta e vira ação.",
         "[4] Meitz et al., 2025\n[5] Gupta et al., 2023\n[6] Burmeister et al., 2023"),
    ]
    larg = (UTIL - Inches(0.5)) / 3
    for i, (nome, pergunta, refs) in enumerate(camadas):
        x = MARGEM + i * (larg + Inches(0.25))
        retangulo(s, x, Inches(2.95), larg, Inches(3.35), CAIXA_FRIA)
        retangulo(s, x, Inches(2.95), larg, Inches(0.5), FRIO)
        texto(s, x + Inches(0.3), Inches(3.08), larg - Inches(0.6), Inches(0.3),
              nome, 17, BRANCO, negrito=True)
        texto(s, x + Inches(0.3), Inches(3.7), larg - Inches(0.6), Inches(1.1),
              pergunta, 17, TEXTO, espaco=1.25)
        texto(s, x + Inches(0.3), Inches(4.85), larg - Inches(0.6), Inches(0.9),
              refs.split("\n"), 16, FRIO, negrito=True, espaco=1.2)
    rodape(s, "Seminário 1 · Trabalhos relacionados", "4 / 11")


# ------------------------------------------------- 4-9. uma por referência
REFERENCIAS = [
    dict(
        camada="Medir", numero="5 / 11",
        autor="Yousuf et al., 2024",
        problema="Monitoramento de condição e detecção de falhas em motor de indução CA",
        estudou=['Motor de indução CA instrumentado com temperatura, vibração, corrente, tensão e velocidade', 'Aquisição em Arduino, com alarme local e notificação por GSM', 'Proteção automática por relé e histórico na plataforma IoT Blynk'],
                levamos=['Fechar a cadeia inteira, do sensor até a ação', 'Temperatura, vibração e corrente como lista de partida', 'Relé como resposta automática à falha'],
                fonte="Measurement and Control, v. 57, n. 8, 2024 · DOI 10.1177/00202940241231473 · [1]",
    ),
    dict(
        camada="Medir", numero="6 / 11",
        autor="Mohammed, Abdulateef e Hamad, 2023",
        problema="Manutenção preditiva de motores elétricos com IoT industrial e aprendizado de máquina",
        estudou=['Raspberry Pi coletando vibração, corrente e temperatura', 'Transmissão por MQTT para servidor em nuvem', 'Cinco algoritmos supervisionados sobre falhas induzidas, com Random Forest à frente'],
                levamos=['MQTT separa aquisição de análise e libera o ESP32', 'Falha induzida gera dados sem histórico prévio', 'Coleta a cada segundo não preserva a vibração'],
                fonte="J. Européen des Systèmes Automatisés, v. 56, n. 4, 2023 · DOI 10.18280/jesa.560414 · [2]",
    ),
    dict(
        camada="Detectar", numero="7 / 11",
        autor="Kolok et al., 2025",
        problema="Manutenção preditiva de baixo custo baseada em vibração",
        estudou=['ESP32 com sensores MEMS de vibração e acústico', 'RMS no domínio do tempo e FFT no da frequência', 'Isolation Forest treinado apenas com operação saudável'],
                levamos=['Dispensa exemplos de falha, nossa maior limitação', 'Extração de característica cabe na borda', 'Calibração por equipamento é obrigatória'],
                fonte="Sensors, v. 25, art. 6610, 2025 · DOI 10.3390/s25216610 · [3]",
    ),
    dict(
        camada="Confiar", numero="8 / 11",
        autor="Meitz et al., 2025",
        problema="Revisão estruturada e desafios em aberto da manutenção preditiva na Indústria 4.0",
        estudou=['Revisão sistemática de 249 publicações', 'Nove categorias e 73 atributos de manutenção preditiva', 'Do monitoramento de condição ao prognóstico e ao planejamento'],
                levamos=['O projeto é um fluxo inteiro: aquisição, tratamento, detecção e avaliação',
                 'Nosso escopo fica na detecção de anomalia, antes do prognóstico',
                 'Avaliação é etapa própria, com métrica escolhida de propósito',
                 'Documentar amostragem, limpeza e separação de treino e teste'],
                fonte="Computers & Industrial Engineering, v. 206, 2025 · DOI 10.1016/j.cie.2025.111193 · [4]",
    ),
    dict(
        camada="Confiar", numero="9 / 11",
        autor="Gupta et al., 2023",
        problema="Manutenção preditiva de esteiras de bagagem de aeroporto com IoT",
        estudou=['Vibração por IoT em oito esteiras idênticas em operação real', 'Sem histórico até a falha, com limpeza apoiada em RMS', 'Rótulos extraídos de registros de manutenção em texto', 'Quatro classificadores comparados, com Random Forest à frente'],
                levamos=['É o caso mais próximo do nosso', 'Limpar ruído e rotular consomem a maior parte do trabalho', 'Registro escrito de manutenção pode virar rótulo'],
                fonte="Computers & Industrial Engineering, v. 177, 2023 · DOI 10.1016/j.cie.2023.109033 · [5]",
    ),
    dict(
        camada="Confiar", numero="10 / 11",
        autor="Burmeister et al., 2023",
        problema="Exploração de dados de produção para manutenção preditiva de equipamento industrial",
        estudou=['Redes bayesianas e árvores de classificação', '227.996 observações de produção e inspeção, com 29 variáveis', 'Reamostragem para lidar com a resposta desbalanceada', 'Previsões traduzidas em regras interpretáveis'],
                levamos=['Todo alerta precisa dizer o que o motivou', 'Modelo legível vale mais que modelo opaco', 'Dado operacional complementa o sinal de sensor'],
                fonte="IEEE Access, v. 11, 2023 · DOI 10.1109/ACCESS.2023.3315842 · [6]",
    ),
]


def slide_referencia(prs, ref):
    s = slide_base(prs, ref["camada"])
    texto(s, MARGEM, Inches(1.0), UTIL, Inches(0.55),
          ref["autor"], 32, TEXTO, negrito=True)
    texto(s, MARGEM, Inches(1.62), UTIL, Inches(0.5),
          ref["problema"], 19, SECUNDARIO, espaco=1.2)

    larg = (UTIL - Inches(0.4)) / 2
    topo, alt = Inches(2.35), Inches(4.25)

    retangulo(s, MARGEM, topo, larg, alt, CAIXA_FRIA)
    retangulo(s, MARGEM, topo, larg, Inches(0.07), FRIO)
    texto(s, MARGEM + Inches(0.35), topo + Inches(0.35), larg - Inches(0.7), Inches(0.3),
          "O QUE O TRABALHO ESTUDOU", 14, FRIO, negrito=True)
    topicos(s, MARGEM + Inches(0.35), topo + Inches(0.95), larg - Inches(0.7),
            alt - Inches(1.3), ref["estudou"])

    x2 = MARGEM + larg + Inches(0.4)
    retangulo(s, x2, topo, larg, alt, CAIXA_QUENTE)
    retangulo(s, x2, topo, larg, Inches(0.07), QUENTE)
    texto(s, x2 + Inches(0.35), topo + Inches(0.35), larg - Inches(0.7), Inches(0.3),
          "O QUE LEVAMOS PARA O PROJETO", 14, QUENTE, negrito=True)
    topicos(s, x2 + Inches(0.35), topo + Inches(0.95), larg - Inches(0.7),
            alt - Inches(1.3), ref["levamos"])

    rodape(s, ref["fonte"], ref["numero"])


# ------------------------------------------------------------- 10. síntese
def sintese(prs):
    s = slide_base(prs, "Síntese")
    texto(s, MARGEM, Inches(1.0), UTIL, Inches(0.8),
          "O que cada trabalho decidiu no nosso projeto", 34, TEXTO, negrito=True)
    retangulo(s, MARGEM, Inches(1.75), Inches(1.6), Inches(0.05), QUENTE)

    itens = [
        ("[1] Yousuf", "Fechar a cadeia do sensor até a ação."),
        ("[2] Mohammed", "Separar aquisição de análise; induzir falhas para gerar dados."),
        ("[3] Kolok", "Treinar apenas com operação saudável, processando na borda."),
        ("[4] Meitz", "Assumir detecção de anomalia como escopo desta etapa."),
        ("[5] Gupta", "Tratar ruído e ausência de rótulo como o trabalho principal."),
        ("[6] Burmeister", "Todo alerta precisa registrar o que o motivou."),
    ]
    y = Inches(2.25)
    alt = Inches(0.62)
    for i, (chave, decisao) in enumerate(itens):
        yi = y + i * (alt + Inches(0.06))
        retangulo(s, MARGEM, yi, UTIL, alt, CAIXA_FRIA)
        retangulo(s, MARGEM, yi, Inches(0.07), alt, QUENTE if i % 2 else FRIO)
        texto(s, MARGEM + Inches(0.4), yi + Inches(0.16), Inches(2.4), Inches(0.4),
              chave, 19, FRIO, negrito=True)
        texto(s, MARGEM + Inches(3.0), yi + Inches(0.16), UTIL - Inches(3.4), Inches(0.4),
              decisao, 19, TEXTO)
    rodape(s, "Seminário 1 · Trabalhos relacionados", "11 / 11")


def main():
    prs = Presentation()
    prs.slide_width, prs.slide_height = L, A

    capa(prs)
    motivacao(prs)
    outros_locais(prs)
    mapa(prs)
    for ref in REFERENCIAS:
        slide_referencia(prs, ref)
    sintese(prs)

    prs.save(SAIDA)
    print(f"{SAIDA} — {len(prs.slides.__iter__.__self__._sldIdLst)} slides")


if __name__ == "__main__":
    main()
