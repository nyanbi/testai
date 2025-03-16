import pandas as pd
import pandas as pd
from sklearn.model_selection import train_test_split # chia tập train và test
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import streamlit as st
st.set_page_config(page_title="Huấn luyện dữ liệu", page_icon="🌍")

data = pd.read_csv('./data/world.csv')
df = pd.DataFrame(data)
df.head(9)
data = df.sort_values(by='Rank')

X = data[['Growth Rate', 'Area (km²)', 'Density (per km²)', 'World Population Percentage']]
y = data['2020 Population']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(y_pred)# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

# Visualize the results
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Values")
plt.ylabel("Predicted Values")
plt.title("Actual vs Predicted Values")
plt.show()

st.title('Huấn luyện mô hình')
st.write('Dữ liệu được chia thành 2 phần: 80% dùng để huấn luyện và 20% dùng để kiểm tra')
st.write('Mô hình hồi quy tuyến tính được huấn luyện với dữ liệu')
a = st.button('Ấn để huấn luyện')
if a:
    st.write('Dữ liệu đã được huấn luyện')
    st.write('Mean Squared Error: ', mse)
    st.write('R^2: ', r2)
    st.write('Biểu đồ so sánh giữa dự đoán và thực tế')
