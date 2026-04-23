import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(layout="wide")

df = pd.read_csv("vehicles_us.csv")
df = df[df["odometer"] < 300000]
df = df[df["price"] < 100000]

st.header("Dashboard de vehículos")

tipo = st.selectbox("Tipo de vehículo", df["type"].dropna().unique())
df_filtrado = df[df["type"] == tipo]

fig = px.scatter(df_filtrado, x="odometer", y="price", color="condition")
st.plotly_chart(fig)

if st.button("Construir histograma"):
    fig = px.histogram(df, x="odometer")
    st.plotly_chart(fig)

if st.button("Construir dispersión"):
    fig = px.scatter(df, x="odometer", y="price")
    st.plotly_chart(fig)