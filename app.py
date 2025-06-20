import streamlit as st
from fipeapy import get_marcas, get_modelos, get_anos, get_detalhes

st.set_page_config(page_title="Comparador de Carros", layout="wide")
st.title("🚗 Comparador de Carros - Tabela FIPE")

def selecionar_carro(col, prefixo):
    with col:
        marcas = get_marcas()
        marca = st.selectbox("Marca", marcas, format_func=lambda x: x["nome"], key=f"{prefixo}_marca")
        modelos = get_modelos(marca["codigo"])["modelos"]
        modelo = st.selectbox("Modelo", modelos, format_func=lambda x: x["nome"], key=f"{prefixo}_modelo")
        anos = get_anos(marca["codigo"], modelo["codigo"])
        ano = st.selectbox("Ano", anos, format_func=lambda x: x["nome"], key=f"{prefixo}_ano")
        detalhes = get_detalhes(marca["codigo"], modelo["codigo"], ano["codigo"])
        return detalhes

st.markdown("### Escolha os carros a comparar")

col1, col2 = st.columns(2)
carro1 = selecionar_carro(col1, "carro1")
carro2 = selecionar_carro(col2, "carro2")

if carro1 is None or carro2 is None:
    st.error("Por favor, selecione dois carros para comparar.")
    st.stop()

if carro1 and carro2:
    st.markdown("---")
    st.subheader("🔍 Comparação")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"**{carro1['Marca']} {carro1['Modelo']} ({carro1['AnoModelo']})**")
        st.text(f"Preço: {carro1['Valor']}")
        st.text(f"Combustível: {carro1['Combustivel']}")
        st.text(f"Tipo: {carro1['TipoVeiculo']}")
        st.text(f"FIPE: {carro1['CodigoFipe']}")

    with col2:
        st.markdown(f"**{carro2['Marca']} {carro2['Modelo']} ({carro2['AnoModelo']})**")
        st.text(f"Preço: {carro2['Valor']}")
        st.text(f"Combustível: {carro2['Combustivel']}")
        st.text(f"Tipo: {carro2['TipoVeiculo']}")
        st.text(f"FIPE: {carro2['CodigoFipe']}")

import pandas as pd
import streamlit as st

# Exemplo de DataFrame
df = pd.DataFrame({
    "carro": ["Fiat", "Ford", "Chevrolet"],
    "preco": [30000, 40000, 35000]
})

# Gerar CSV em formato string
data_csv = df.to_csv(index=False).encode('utf-8')

# Botão para baixar
st.download_button("Baixar Comparação", data_csv, file_name="comparacao.csv", mime="text/csv")
