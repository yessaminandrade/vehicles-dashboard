# Vehicles Dashboard

Aplicación web desarrollada con Streamlit para analizar anuncios de vehículos en EE.UU.

## Funcionalidad

La aplicación permite visualizar:

- Distribución del kilometraje (`odometer`) mediante un histograma
- Relación entre kilometraje y precio (`price`) con un gráfico de dispersión

## Análisis

Se observa una relación negativa entre el kilometraje y el precio: a mayor kilometraje, menor precio.  
Sin embargo, existe una alta dispersión, lo que indica que otros factores (modelo, año, condición) también influyen en el precio.

Se realizó una limpieza básica de datos:
- Eliminación de valores nulos en `odometer` y `price`
- Eliminación de valores extremos para mejorar la visualización

## Dataset

El dataset utilizado es `vehicles_us.csv`, que contiene información sobre anuncios de vehículos, incluyendo precio, kilometraje, modelo, tipo, entre otros.

## Tecnologías

- Python
- Pandas
- Plotly Express
- Streamlit