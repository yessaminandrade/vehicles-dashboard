import pandas as pd
import plotly.express as px
import streamlit as st

import os
import streamlit as st

st.set_page_config(layout="wide")

df = pd.read_csv('vehicles_us.csv')

# limpiar datos extremos
df = df[df['odometer'] < 300000]
df = df[df['price'] < 100000]

st.header('Dashboard de vehículos')

if st.button('Construir histograma'):
    fig = px.histogram(df, x='odometer')
    st.plotly_chart(fig)

if st.button('Construir dispersión'):
    fig = px.scatter(df, x='odometer', y='price')
    st.plotly_chart(fig)