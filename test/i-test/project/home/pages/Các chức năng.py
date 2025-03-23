import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(page_title="Các chức năng", page_icon="🌍", layout="wide")

# Title and header
st.title('🌍 Dự đoán dân số của các quốc gia')
st.markdown("---")

# Sidebar
st.sidebar.header("📋 Menu")
st.sidebar.write("1. Vẽ biểu đồ cột")
st.sidebar.write("2. Phân tích dữ liệu")
st.sidebar.write("3. Dự đoán dân số")

# Main content
st.subheader('📊 Bảng dữ liệu dân số thế giới')
try:
	data = pd.read_csv('./data/world.csv')
	ef = pd.DataFrame(data)
	ef = ef.sort_values(by='Rank')
	st.dataframe(ef, use_container_width=True)
except FileNotFoundError:
	st.error("❌ The file './data/world.csv' was not found. Please check the file path.")

# Features section
st.markdown("---")
st.subheader('⚙️ Các chức năng')
col1, col2 = st.columns(2)

with col1:
	st.write('1️⃣ **Vẽ biểu đồ cột của 10 quốc gia có dân số cao nhất năm 2022**')
	st.write('2️⃣ **Xem phân tích tập dữ liệu dân số thế giới**')

with col2:
	st.write('3️⃣ **Dự đoán dân số của các quốc gia bằng AI**')

# Footer
