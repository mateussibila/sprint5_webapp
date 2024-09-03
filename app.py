import streamlit as st
import pandas as pd
import plotly_express as px

car_data = pd.read_csv('vehicles.csv')

model_counts = car_data['model'].value_counts()
models_limit = 500
models_to_keep = model_counts[model_counts > models_limit].index
car_data_filtered = car_data[car_data['model'].isin(models_to_keep)]

st.header('Data viewer')
filter_dataset = st.checkbox(f'Include models with less than {models_limit} ads')


if filter_dataset:
    st.write(car_data_filtered)    
else:
    st.write(car_data)

st.header('Vehicle types by manufacturer')
st.write("INSERIR gráfico de barras interativo")

st.header('Histogram of condition vs model_year')
hist_button = st.button('Create histogram')  # criar um botão

if hist_button:  # se o botão for clicado
    # escrever uma mensagem
    st.write('Creating a histogram for the car sale adds dataset')

    # criar um histograma
    fig = px.histogram(car_data, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)


st.header('Compare price distribution between manufacturers')
scatter_plot_button = st.button('Creat scatter plot')

if scatter_plot_button:
    # escrever uma mensagem
    st.write('Creating a scatter plot for the car sale adds dataset')

    fig = px.scatter(car_data, x='odometer', y='price')

    st.plotly_chart(fig, use_container_width=True)

# select box
# https://docs.streamlit.io/develop/api-reference/widgets/st.selectbox