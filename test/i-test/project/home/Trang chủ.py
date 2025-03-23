import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

st.set_page_config(page_title="Dân số thế giới", page_icon="🌍", layout="wide")

# Sidebar navigation
st.sidebar.title("🌍 Navigation")
page = st.sidebar.radio("Đi đến", ["Trang chủ", "Biểu đồ cột", "Dự đoán"])

# Main content
if page == "Trang chủ":
    st.title('🌍 Top 10 quốc gia có dân số cao nhất')
    st.markdown("### Khám phá dữ liệu dân số thế giới và các yếu tố ảnh hưởng đến dân số.")

    # Load the CSV file
    data = pd.read_csv('./data/world.csv')

    # Sort data by Rank
    sorted_data = data.sort_values(by='Rank')

    # Display top 10 countries by population
    st.markdown("#### Biểu đồ thanh: Top 10 quốc gia có dân số cao nhất")
    st.bar_chart(sorted_data.set_index('Country/Territory')['2022 Population'].iloc[:10])

    # Area chart for top 10 countries
    st.markdown("#### Biểu đồ diện tích: Top 10 quốc gia có dân số cao nhất")
    st.area_chart(sorted_data.set_index('Country/Territory')['2022 Population'].iloc[:10])

elif page == "Biểu đồ cột":
    st.title('📊 Các yếu tố ảnh hưởng đến dân số')
    st.markdown("### Phân tích các yếu tố ảnh hưởng đến dân số qua các biểu đồ.")

    # Load the CSV file
    data = pd.read_csv('./data/world.csv')
    ef = pd.DataFrame(data).sort_values(by='Rank')

    # Dropdown selection for factors
    factor = st.selectbox('Chọn yếu tố', ['Growth Rate', 'Area (km²)', 'Density (per km²)', 'World Population Percentage'])
    st.markdown(f"#### 📊 Biểu đồ về top 10 quốc gia có {factor} cao nhất năm 2022")

    # Bar & Line chart for selected factor
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("##### Biểu đồ thanh")
        st.bar_chart(ef.set_index('Country/Territory')[factor].iloc[:10])
    with col2:
        st.markdown("##### Biểu đồ đường")
        st.line_chart(ef.set_index('Country/Territory')[factor].iloc[:10])

elif page == "Dự đoán":
    st.title('📈 Dự đoán dân số')
    st.markdown("### Phân tích và dự đoán dân số dựa trên các yếu tố.")

    # Load the CSV file
    data = pd.read_csv('./data/world.csv')
    ef = pd.DataFrame(data)

    # Correlation matrix
    st.markdown("#### Ma trận tương quan giữa các yếu tố")
    correlation_matrix = ef[['Growth Rate', 'Area (km²)', 'Density (per km²)', 'World Population Percentage']].corr()
    st.write(correlation_matrix)

    # Display correlation matrix as a heatmap
    st.markdown("#### Biểu đồ nhiệt (Heatmap) của ma trận tương quan")
    fig, ax = plt.subplots()
    cax = ax.matshow(correlation_matrix, cmap='coolwarm')
    fig.colorbar(cax)
    st.pyplot(fig)

# Footer
