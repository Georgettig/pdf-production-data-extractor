from pydantic import BaseModel
from typing import Optional

class PdfRequest(BaseModel):
    filename: str
    content: str

class RoloReport(BaseModel):
    
    # Visão Geral da Produção
    numero_rolo: Optional[str] = None
    produto_id: Optional[int] = None

    data: Optional[str] = None

    producao_total: Optional[float] = None

    tempo_total_maquina: Optional[str] = None
    tempo_quebra: Optional[str] = None
    tempo_producao: Optional[str] = None

    comprimento_total: Optional[float] = None

    numero_quebras: Optional[int] = None
    velocidade_enroladeira: Optional[float] = None
    largura_rolo: Optional[float] = None
    taxa_producao: Optional[float] = None

    # Scanner Enroladeira
    gramatura_setpoint: Optional[float] = None
    gramatura_media: Optional[float] = None

    umidade_setpoint: Optional[float] = None
    umidade_media: Optional[float] = None

    peso_seco_setpoint: Optional[float] = None
    peso_seco_media: Optional[float] = None

    temperatura_setpoint: Optional[float] = None
    temperatura_media: Optional[float] = None

    # Rastreabilidade
    arquivo_origem: Optional[str] = None
    data_processamento: Optional[str] = None