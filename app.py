import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from utils.helper import load_data

st.set_page_config(page_title="Beranda", page_icon="🏠", layout="wide")

df = load_data()

if df is None:
    st.error("❌ File dataset 'student_habits_performance.csv' tidak ditemukan!")
    st.stop()

st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>🎓 Analisis Kebiasaan & Performa Akademik</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 16px; color: #4B5563;'>Monitoring pengaruh gaya hidup harian terhadap capaian hasil ujian mahasiswa.</p>", unsafe_allow_html=True)
st.markdown("---")

col_metric, col_gauge = st.columns([1, 1])

mean_score = float(df['exam_score'].mean())

with col_metric:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 📌 Ringkasan Parameter Basis Data")
    k1, k2 = st.columns(2)
    k1.metric("Total Sampel Aktif", f"{len(df)} Baris")
    k2.metric("Rerata Kehadiran Kelas", f"{df['attendance_percentage'].mean():.1f}%")
    
    k3, k4 = st.columns(2)
    k3.metric("Rerata Waktu Layar", f"{df['total_screen_time'].mean():.1f} Jam")
    k4.metric("Rerata Jam Tidur", f"{df['sleep_hours'].mean():.1f} Jam")

with col_gauge:
    st.markdown("<h4 style='text-align: center; color: #1E3A8A;'>Rerata Skor Ujian Keseluruhan</h4>", unsafe_allow_html=True)

    if mean_score >= 85:
        g_color = "#10B981"  
    elif mean_score >= 65:
        g_color = "#F59E0B"  
    else:
        g_color = "#EF4444"  
        
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = mean_score,
        number = {'suffix': " / 100", 'font': {'size': 36, 'color': g_color}},
        gauge = {
            'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "#CBD5E1"},
            'bar': {'color': g_color},
            'bgcolor': "white", 
            'borderwidth': 1,
            'bordercolor': "#E5E7EB",
            'steps': [{'range': [0, 100], 'color': "white"}] 
        }
    ))
    fig.update_layout(height=260, margin=dict(l=30, r=30, t=10, b=10))
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
with st.expander("🔍 Preview Dataset Bersih"):
    st.dataframe(df.head(15), use_container_width=True)
