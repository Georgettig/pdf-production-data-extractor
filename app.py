import streamlit as st
import pandas as pd 

from extractor import extrair_texto
from parsers.parser import parse_report
from machines.factory import MachineFactory

from database.database import engine
from database.database import Base
from database.repository import ReportRepository
from database.models import RoloReport

Base.metadata.create_all(bind=engine)

st.set_page_config(page_title="PDF Data Extractor", layout="wide")

st.title("PDF Data Extractor")

uploaded_files = st.file_uploader("Envie o(s) PDF(s)", type=["pdf"], accept_multiple_files=True)

if uploaded_files:

    resultados = []

    progress = st.progress(0)

    for i, pdf in enumerate(uploaded_files):
        try:
            texto = extrair_texto(pdf.read())

            machine = MachineFactory.create(pdf.name)

            report = parse_report(texto, pdf.name, machine)

            dados = report.model_dump(exclude_none=True)

            dados["maquina"] = machine.nome

            resultados.append(dados)

        except Exception as e:
            resultados.append({
                "arquivo_origem": pdf.name, 
                "erro": str(e)
            })

        progress.progress((i + 1) / len(uploaded_files))

    df = pd.DataFrame(resultados)

    if "numero_rolo" in df.columns:
        df = df.drop_duplicates(subset=["numero_rolo"])

    st.success(f"{len(resultados)} arquivo(s) processado(s)!")

    col1, col2, col3 = st.columns(3)

    col1.metric("Rolos Processados", len(df))
    
    col2.metric("Produção Total (t)", round(df["producao_total"].sum(), 2) if "producao_total" in df.columns else 0)
    
    col3.metric("Quebras", int(df["numero_quebras"].sum()) if "numero_quebras" in df.columns else 0)
    
    if "nome_produto" in df.columns:
    
        produtos = df["nome_produto"].dropna().unique()

        if len(produtos) > 0:
    
            produto = st.selectbox("Produto", ["Todos"] + list(produtos))

            if produto != "Todos":

                df = df[df["nome_produto"] == produto]

    if "data_inicio" in df.columns:

        try:
    
            df["data_inicio"] = pd.to_datetime(df["data_inicio"], errors="coerce")

            df = df.sort_values(by="data_inicio", ascending=False)

        except:
            
            pass

    st.dataframe(df, use_container_width=True)

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        if st.button("Salvar Dados"):

            repository = ReportRepository()

            salvos = 0

            for registro in resultados:

                if "erro" in registro:
                    continue

                repository.salvar(registro)

                salvos += 1

            st.success(f"{salvos} registro(s) salvo(s) com sucesso!")

    with col2:

        if st.button("Visualizar Banco de Dados"):

            repository = ReportRepository()

            registros = repository.listar()

            if registros:

                df_db = pd.DataFrame(
                    [
                        {
                            coluna: valor 
                            for coluna, valor in vars(registro).items()
                            if not coluna.startswith("_") 
                        }
                        for registro in registros
                    ]
                )
                st.dataframe(df_db, use_container_width=True)

            else:
                st.info("Banco de Dados vazio!")
