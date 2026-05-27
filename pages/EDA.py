import streamlit as st
import plotly.express as px
from utils.helper import load_data

st.set_page_config(page_title="Analisis Tren", page_icon="📊", layout="wide")
df = load_data()

with st.sidebar:
    st.markdown("<h3 style='color: #1E3A8A;'>🎛️ Panel Kontrol</h3>", unsafe_allow_html=True)
    selected_gender = st.multiselect("Pilih Komponen Gender:", options=df['gender'].unique(), default=df['gender'].unique())
    selected_olahraga = st.multiselect("Filter Kualitas Olahraga:", options=df['kualitas_olahraga'].unique(), default=df['kualitas_olahraga'].unique())

df_filtered = df[(df['gender'].isin(selected_gender)) & (df['kualitas_olahraga'].isin(selected_olahraga))]

st.markdown("<h2 style='color: #1E3A8A;'>📊 Exploratory Data Analysis (EDA) Interaktif</h2>", unsafe_allow_html=True)
st.markdown("Halaman ini menyajikan pola korelasi antara aktivitas harian mahasiswa dengan distribusi nilai akhir mereka.")
st.markdown("---")

col1, col2 = st.columns(2)
with col1:
    st.markdown("<h4 style='text-align: center;'>Hubungan Jam Belajar vs Nilai Ujian</h4>", unsafe_allow_html=True)
    fig1 = px.scatter(df_filtered, x="study_hours_per_day", y="exam_score", color="mental_health_rating", 
                      size="attendance_percentage", template="plotly_white", color_continuous_scale="Blugrn",
                      labels={"study_hours_per_day": "Jam Belajar/Hari", "exam_score": "Skor Ujian", "mental_health_rating": "Rating Mental"})
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.markdown("<h4 style='text-align: center;'>Dampak Waktu Layar (Screen Time) vs Nilai Ujian</h4>", unsafe_allow_html=True)
    fig2 = px.scatter(df_filtered, x="total_screen_time", y="exam_score", color="kualitas_olahraga", 
                      template="plotly_white", color_discrete_map={"Buruk": "#EF4444", "Cukup": "#F59E0B", "Baik": "#10B981"},
                      labels={"total_screen_time": "Total Screen Time (Jam)", "exam_score": "Skor Ujian"})
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")
st.markdown("<h4 style='text-align: center;'>Komparasi Skor Ujian Berdasarkan Tingkat Keaktifan Olahraga</h4>", unsafe_allow_html=True)
fig3 = px.box(df_filtered, x="kualitas_olahraga", y="exam_score", color="kualitas_olahraga",
              category_orders={"kualitas_olahraga": ["Buruk", "Cukup", "Baik"]},
              color_discrete_map={"Buruk": "#EF4444", "Cukup": "#F59E0B", "Baik": "#10B981"},
              labels={"kualitas_olahraga": "Kategori Olahraga", "exam_score": "Skor Ujian"})
st.plotly_chart(fig3, use_container_width=True)
