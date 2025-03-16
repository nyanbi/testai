import os
import streamlit as st

from config import Config


def menu():
    st.sidebar.page_link("app.py", label="Home Page")
    st.sidebar.page_link("pages/1_Data_Analysis.py", label="Phân tích tập dữ liệu")
    st.sidebar.page_link("pages/2_Input_Record.py", label="Thêm dữ liệu dự đoán")
    st.sidebar.page_link("pages/3_Prediction.py", label="Phân tích dự đoán")

if __name__ == "__main__": 
    st.set_page_config(
        page_title="Lettuce Multipage Tracker",
        layout="centered",
        page_icon="👋",
    )

    st.title("Lettuce Growth Tracker")
    st.header("Chức năng")
    st.markdown("""
    1. Xem phân tích tập dữ liệu trồng Xà Lách
    2. Thêm dữ liệu mới và cập nhật các biểu đồ
    3. Sử dụng AI để dự đoán ngày trưởng thành của cây
    """)
    
    st.subheader("Credits")
    st.markdown(

        """
        Ứng dựng được xây dựng với [streamlit](https://streamlit.io) và [Plotly](https://plotly.com/).
        
        Bản quyền thuộc về CTCP Trường học MindX
        """
    )
    img_path = os.path.join(Config.IMG_DIR, 'mindx_light_small.png')
    st.image(img_path)

    menu()