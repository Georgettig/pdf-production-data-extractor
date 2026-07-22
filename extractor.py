import pymupdf

def extrair_texto(pdf_bytes: bytes) -> str:
    
    pdf = pymupdf.open(stream=pdf_bytes, filetype="pdf")

    texto = ""

    for pagina in pdf:
        texto += pagina.get_text("text")
        texto += "\n"

    return texto