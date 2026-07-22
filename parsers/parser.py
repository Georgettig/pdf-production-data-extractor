import re
from .helpers import extract, to_float, to_int, extrair_metrica, extrair_porcentagem, extrair_tempo, formatar_data
from models import RoloReport
from datetime import datetime

def parse_scanner(texto, nome):
    
    pattern = (
        rf"{re.escape(nome)}\s+"
        rf"[^\n]+\s+"
        rf"([^\n]+)\s+"
        rf"([^\n]+)\s+"
        rf"([^\n]+)\s+"
        rf"([^\n]+)\s+"
        rf"([^\n]+)\s+"
        rf"([^\n]+)"
    )

    match = re.search(pattern, texto, re.IGNORECASE)

    if not match:
        return None

    return {
        "setpoint": to_float(match.group(1)),
        "media": to_float(match.group(2))
    }


def parse_report(texto: str, arquivo: str = None, machine = None):
    report = RoloReport()
    report.arquivo_origem = arquivo
    
    # Cabeçalho
    report.numero_rolo = extract(r"Número do rolo.*?(\d{8,9})", texto)
    report.produto_id = to_int(extract(r"Produto ID.*?(\d+)", texto))
    report.data = formatar_data(extract(r"Data:\s*([^\n]+)", texto))
    
    # Visão Geral da Produção
    report.producao_total = extrair_metrica(texto, "Produção Total")
    report.tempo_total_maquina = extrair_tempo(texto, "Tempo Total da Máquina")
    report.tempo_quebra = extrair_tempo(texto, "Tempo de quebra")
    report.tempo_producao = extrair_tempo(texto, "Tempo de produção")
    report.comprimento_total = extrair_metrica(texto, "Comprimento total do rolo")
    report.velocidade_enroladeira = extrair_metrica(texto, "Velocidade da enroladeira")
    report.largura_rolo = extrair_metrica(texto, "Largura do rolo")
    report.taxa_producao = extrair_metrica(texto, "Taxa de produção")

    match = re.search(
        r"Número de quebras\s+#\s+([\d,]+)",
        texto,
        re.IGNORECASE
    )

    if match:
        report.numero_quebras = int(
            float(
                match.group(1).replace(",", ".")
            )
        )

    # Scanner Enroladeira
    gramatura = parse_scanner(texto, "Gramatura")

    if gramatura:
        report.gramatura_setpoint = gramatura["setpoint"]
        report.gramatura_media = gramatura["media"]

    umidade = parse_scanner(texto, "Umidade")

    if umidade:
        report.umidade_setpoint = umidade["setpoint"]
        report.umidade_media = umidade["media"]

    peso_seco = parse_scanner(texto, "Peso Seco")

    if peso_seco:
        report.peso_seco_setpoint = peso_seco["setpoint"]
        report.peso_seco_media = peso_seco["media"]

    temperatura = parse_scanner(texto, "Temperatura")

    if temperatura:
        report.temperatura_setpoint = temperatura["setpoint"]
        report.temperatura_media = temperatura["media"]

    return report