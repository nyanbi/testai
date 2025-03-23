import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title="Huấn luyện dữ liệu", page_icon="🌍", layout="wide")

# Load and preprocess data
data = pd.read_csv('./data/world.csv')
df = pd.DataFrame(data)
data = df.sort_values(by='Rank')

X = data[['Growth Rate', 'Area (km²)', 'Density (per km²)', 'World Population Percentage']]
y = data['2020 Population']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Streamlit UI
st.title('🌍 Huấn luyện mô hình dự đoán dân số')
st.markdown("""
### Mô tả
Ứng dụng này sử dụng **hồi quy tuyến tính** để dự đoán dân số dựa trên các thông số như:
- Tốc độ tăng trưởng
- Diện tích
- Mật độ dân số
- Tỷ lệ dân số thế giới
""")

st.sidebar.header("Cấu hình")
st.sidebar.write("Dữ liệu được chia thành:")
st.sidebar.write("- **80%** để huấn luyện")
st.sidebar.write("- **20%** để kiểm tra")

if st.sidebar.button('Huấn luyện mô hình'):
    st.success('✅ Mô hình đã được huấn luyện thành công!')
    st.write('### Kết quả:')
    st.metric(label="Mean Squared Error (MSE)", value=f"{mse:.2f}")
    st.metric(label="R-squared (R²)", value=f"{r2:.2f}")

    # Visualize results
    st.write('### Biểu đồ so sánh giữa giá trị thực tế và dự đoán:')
    fig, ax = plt.subplots()
    ax.scatter(y_test, y_pred, alpha=0.7, color='blue')
    ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2, color='red')
    ax.set_xlabel("Giá trị thực tế")
    ax.set_ylabel("Giá trị dự đoán")
    ax.set_title("Thực tế vs Dự đoán")
    st.pyplot(fig)

    st.write('### Dữ liệu mẫu:')
    st.dataframe(data.head(10))
else:
    st.info('Ấn nút **Huấn luyện mô hình** ở thanh bên để bắt đầu.')