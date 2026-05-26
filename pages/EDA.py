import streamlit as st
import plotly.express as px
from utils.helper import load_data

st.set_page_config(page_title="Visualisasi Data", page_icon="📊", layout="wide")
df = load_data()

with st.sidebar:
    st.markdown("### 🎛️ Filter Kontrol")
    selected_gender = st.multiselect("Pilih Gender:", options=df['gender'].unique(), default=df['gender'].unique())
    selected_olahraga = st.multiselect("Kualitas Olahraga:", options=df['kualitas_olahraga'].unique(), default=df['kualitas_olahraga'].unique())

df_filtered = df[(df['gender'].isin(selected_gender)) & (df['kualitas_olahraga'].isin(selected_olahraga))]

st.title("📊 Exploratory Data Analysis (EDA)")
st.markdown("Eksplorasi korelasi gaya hidup terhadap capaian akademis.")

col1, col2 = st.columns(2)
with col1:
    st.markdown("Jam Belajar vs Nilai Ujian")
    fig1 = px.scatter(df_filtered, x="study_hours_per_day", y="exam_score", color="mental_health_rating", 
                      size="attendance_percentage", template="plotly_white")
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.markdown("Total Screen Time vs Nilai Ujian")
    fig2 = px.scatter(df_filtered, x="total_screen_time", y="exam_score", color="kualitas_olahraga", 
                      template="plotly_white", color_discrete_map={"Buruk": "red", "Cukup": "orange", "Baik": "green"})
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("Distribusi Skor Ujian Berdasarkan Olahraga")
fig3 = px.box(df_filtered, x="kualitas_olahraga", y="exam_score", color="kualitas_olahraga",
              category_orders={"kualitas_olahraga": ["Buruk", "Cukup", "Baik"]},
              color_discrete_map={"Buruk": "red", "Cukup": "orange", "Baik": "green"})
st.plotly_chart(fig3, use_container_width=True)
