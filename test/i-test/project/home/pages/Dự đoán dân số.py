import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import streamlit as st

# Set page configuration
st.set_page_config(page_title="Dự đoán dân số", page_icon="🌍", layout="wide")

# Load and preprocess data
data = pd.read_csv('./data/world.csv')
data = data.sort_values(by='Rank')

# Train the model
def train(data):
    X = data[['Growth Rate', 'Area (km²)', 'Density (per km²)', 'World Population Percentage']]
    y = data['2020 Population']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    return model, y_test, y_pred

model, y_test, y_pred = train(data)

# Header section
st.title("🌍 Dự đoán dân số")
st.markdown("### Một ứng dụng dự đoán dân số dựa trên các thông số quốc gia.")

# Comparison chart section
st.header("📊 Biểu đồ so sánh giữa dự đoán và thực tế")
chart_data = pd.DataFrame({
    'Index': range(len(y_pred)),
    'Predicted': y_pred
})

col1, col2 = st.columns(2)

with col1:
    st.subheader("Scatter Chart")
    st.scatter_chart(chart_data.set_index('Index'))

with col2:
    st.subheader("Vega Lite Chart")
    st.vega_lite_chart({
        'width': 700,
        'height': 400,
        'mark': {'type': 'point', 'tooltip': True},
        'encoding': {
            'x': {'field': 'Index', 'type': 'quantitative', 'title': 'Index'},
            'y': {'field': 'Predicted', 'type': 'quantitative', 'title': 'Predicted'}
        },
        'data': {'values': chart_data.to_dict(orient='records')}
    })

# Actual vs Predicted plot
st.subheader("📈 Actual vs Predicted")
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.7, label="Predictions")
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linewidth=2, label="Ideal Line")
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Actual vs Predicted')
plt.legend()
st.pyplot(plt)

# Prediction section
st.header("🔮 Dự đoán dân số của một quốc gia")
st.write("### Chọn quốc gia để dự đoán dân số:")
st.dataframe(data[['Rank', 'Country/Territory']])

aff = st.number_input('Chọn thứ hạng quốc gia (Rank)', min_value=1, max_value=len(data), value=1)

test = pd.DataFrame({
    'Growth Rate': [data['Growth Rate'].iloc[int(aff)-1]],
    'Area (km²)': [data['Area (km²)'].iloc[int(aff)-1]],
    'Density (per km²)': [data['Density (per km²)'].iloc[int(aff)-1]],
    'World Population Percentage': [data['World Population Percentage'].iloc[int(aff)-1]]
})

predicted_population = model.predict(test)
predicted_population = np.float32(predicted_population[0])

st.success(f"🌟 Dự đoán dân số của **{data['Country/Territory'].iloc[int(aff)-1]}** là: **{predicted_population:,.0f}**")