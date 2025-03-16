import streamlit as st
import pandas as pd
st.set_page_config(page_title="Các chức năng", page_icon="🌍")
st.title('Dự đoán dân số của các quốc gia')

# st.sidebar.title('Home')
# st.sidebar.title('Some chart','app1.py')
# st.sidebar.title('Predictions')


st.write('Bảng dữ liệu dân số thế giới')
try:
	data = pd.read_csv('./data/world.csv')
	ef = pd.DataFrame(data)
	ef = ef.sort_values(by='Rank')
	st.write(ef)
except FileNotFoundError:
	st.error("The file './data/world.csv' was not found. Please check the file path.")
st.title('Chưc năng')
st.write('01.Vẽ biểu đồ cột của 10 quốc gia có dân số cao nhất năm 2022')
st.write('02.Xem Xem phân tích tập dữ liệu dân số thế giới')
st.write('03.Dự đoán dân số của các quốc gia bằng AI')