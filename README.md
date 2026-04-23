# Vehicles Dashboard

Aplicación interactiva para explorar cómo el kilometraje y otras variables influyen en el precio de vehículos en EE.UU.

🔗 App desplegada:  
https://vehicles-dashboard-exp4djv582rfcxubqjlouc.streamlit.app/

---

## Funcionalidad

La aplicación permite:

- Filtrar por tipo de vehículo
- Visualizar la distribución del kilometraje mediante un histograma
- Analizar la relación entre kilometraje y precio con un gráfico de dispersión
- Explorar cómo la condición del vehículo impacta el precio

---

## Análisis

Se observa una relación inversa entre kilometraje y precio: en general, los vehículos con mayor kilometraje tienden a tener menor valor.

Sin embargo, la dispersión de los datos indica que el kilometraje no es el único factor relevante. La condición del vehículo muestra diferencias claras en el precio, lo que sugiere que múltiples variables influyen en la valoración final.

Además, al filtrar por tipo de vehículo, es posible identificar patrones distintos entre categorías, lo que permite un análisis más detallado del comportamiento del mercado.

---

## Procesamiento de datos

Se realizó una limpieza básica de los datos para mejorar la calidad del análisis:

- Eliminación de valores nulos en `odometer` y `price`
- Filtrado de valores extremos para evitar distorsiones en la visualización

---

## Dataset

El dataset utilizado es `vehicles_us.csv`, que contiene información sobre anuncios de vehículos en EE.UU., incluyendo variables como precio, kilometraje, modelo, condición, tipo, entre otras.

---

## Tecnologías

- Python  
- Pandas  
- Plotly Express  
- Streamlit  