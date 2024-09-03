import streamlit as st
import pandas as pd
import plotly_express as px

# reading the dataset
car_data = pd.read_csv('vehicles.csv')

# Section 1 - Data view
st.header('Data viewer')  # Showing header
# Building a filter
model_counts = car_data['model'].value_counts()
models_limit = 500
models_to_keep = model_counts[model_counts > models_limit].index
car_data_filtered = car_data[car_data['model'].isin(models_to_keep)]
# Checkbox to turn on and off the filter
filter_num_ads = st.checkbox(
    f'Exclude models with less than {models_limit} ads')
# Defining what to show based on the checkbox state
if filter_num_ads:
    st.write(car_data_filtered)  # if on, show filtered dataset
else:
    st.write(car_data)  # if off, show unfiltered

# Section 2 - Histogram
st.header('Histogram of `model_year`')  # Showing header
# Showing a button to create an histogram
hist_button = st.button('Create histogram')
# If the button is clicked
if hist_button:
    # Write a message
    st.write('Creating a histogram by `model_year`')
    # Create a histogram by 'model_year'
    fig = px.histogram(car_data, x="model_year")
    # Show the histogram
    st.plotly_chart(fig, use_container_width=True)

# Section 3 - Scatter plot - price and odometer
# showing a header
st.header('Compare `price` distribution per `odometer` mesurements')
# Showing a button to create the plot
scatter_plot_button = st.button('Create scatter plot')
# If the button is clicked
if scatter_plot_button:
    # Write a message
    st.write('Creating a scatter plot')
    # Create a scatter plot of price distribution per odometer mesurements
    fig = px.scatter(car_data, x='odometer', y='price')
    # Show the scatter plot
    st.plotly_chart(fig, use_container_width=True)
