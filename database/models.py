from sqlalchemy import Column, Integer, String, Float

from .database import Base

class RoloReport(Base):
    
    __tablename__ = "relatorios"
    
    id = Column(Integer, primary_key=True)
    
    numero_rolo = Column(String, unique=True)
    
    produto_id = Column(Integer)
    
    data = Column(String)

    producao_total = Column(Float)
    
    tempo_total_maquina = Column(String)
    
    tempo_quebra = Column(String)
    
    tempo_producao = Column(String)
    
    tempo_perdido = Column(String)
    
    comprimento_total = Column(Float)
    
    numero_quebras = Column(Integer)

    velocidade_enroladeira = Column(Float)
    
    largura_rolo = Column(Float)
    
    taxa_producao = Column(Float)
    
    gramatura_setpoint = Column(Float)
    gramatura_media = Column(Float)
    
    umidade_setpoint = Column(Float)
    umidade_media = Column(Float)
    
    peso_seco_setpoint = Column(Float)
    peso_seco_media = Column(Float)
    
    temperatura_setpoint = Column(Float)
    temperatura_media = Column(Float)

    maquina = Column(String)
    
    arquivo_origem = Column(String)