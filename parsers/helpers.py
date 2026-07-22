import re
from datetime import datetime
from models import RoloReport

def extract(pattern, text):
    match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)

    if match:
        return match.group(1).strip()

    return None
    

def to_float(valor):
    if valor is None:
        return None

    valor = valor.strip()

    valor = valor.replace(".", "")
    valor = valor.replace(",", ".")

    try:
        return float(valor)

    except:
        return None


def to_int(valor):
    if valor is None:
        return None

    try:
        return int(float(valor.replace(",", ".")))
    except:
        return None


def extrair_metrica(texto, nomes):
    
    if isinstance(nomes, str):
        nomes = [nomes]

    for nome in nomes:

        pattern = rf"{re.escape(nome)}\s+[^\n]+\s+([\d,]+)"

        match = re.search(pattern, texto, re.IGNORECASE)

        if match:
            return to_float(match.group(1))

    return None


def extrair_porcentagem(texto, nome):
    pattern = rf"{re.escape(nome)}\s+%\s+([\d,]+)"

    match = re.search(pattern, texto, re.IGNORECASE)

    if match:
        return to_float(match.group(1))

    return None


def extrair_tempo(texto, nomes):

    if isinstance(nomes, str):
        nomes = [nomes]

    for nome in nomes:

        pattern = (
            rf"{re.escape(nome)}"
            rf"\s+[^\n]+"
            rf"\s+([0-9:]+)"
        )

        match = re.search(pattern, texto, re.IGNORECASE)

        if match:
            return match.group(1)

    return None


def formatar_data(data):
    if not data:
        return None

    formatos = [
        "%d.%m.%Y %H:%M:%S",
        "%Y-%m-%d %H:%M:%S",
        "%d/%m/%Y %H:%M:%S"
    ]

    for formato in formatos:
        try:
            return datetime.strptime(
                data.strip(),
                formato
            ).strftime("%Y-%m-%d %H:%M:%S")
        except:
            pass

    return data