import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

st.set_page_config(page_title="Dân số thế giới", page_icon="🌍")

# Sidebar navigation using buttons
# st.sidebar.title("Navigation")
# if st.sidebar.button("Home"):
#     st.switch_page("web")

# if st.sidebar.button("Chart"):
#     st.switch_page("app")

# if st.sidebar.button("Predictions"):
#     st.switch_page("predict")

# Main content
st.title('🌍 Top 10 quốc gia có dân số cao nhất')

# Load the CSV file
data = pd.read_csv('./data/world.csv')

# Sort data by Rank
sorted_data = data.sort_values(by='Rank')

# Bar chart for top 10 countries by population
st.bar_chart(sorted_data.set_index('Country/Territory')['2022 Population'].iloc[:10])

# Create dataframe for visualization
ef = pd.DataFrame(data)
ef = ef.sort_values(by='Rank')

# Area chart for top 10 countries
st.area_chart(ef.set_index('Country/Territory')['2022 Population'].iloc[:10])

# Population influencing factors
st.title('📊 Các yếu tố ảnh hưởng đến dân số')
st.write('1. Tốc độ tăng trưởng')
st.write('2. Diện tích')
st.write('3. Mật độ dân số (per km²)')
st.write('4. Tỷ lệ dân số thế giới')

st.title('📈 Các biểu đồ về các yếu tố ảnh hưởng đến dân số')

# Dropdown selection for factors
a = st.selectbox('Chọn yếu tố', ['Growth Rate','Area (km²)','Density (per km²)','World Population Percentage'])
st.write(f'📊 Biểu đồ về top 10 quốc gia có {a} cao nhất năm 2022')

# Bar & Line chart for selected factor
st.bar_chart(ef.set_index('Country/Territory')[a].iloc[:10])
st.line_chart(ef.set_index('Country/Territory')[a].iloc[:10])

# Correlation matrix
st.title('📌 Chi tiết tương quan giữa các yếu tố')
correlation_matrix = ef[['Growth Rate', 'Area (km²)', 'Density (per km²)', 'World Population Percentage']].corr()

# Display correlation matrix
st.write(correlation_matrix)

# Draw a bar chart for correlation matrix
st.bar_chart(correlation_matrix)
