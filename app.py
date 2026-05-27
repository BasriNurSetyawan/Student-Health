import streamlit as st
import pandas as pd
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
        
    st.markdown(f"<div style='text-align: center;'><h1 style='color: {g_color}; font-size: 3rem; margin-bottom: 10px;'>{mean_score:.1f} <span style='font-size: 1.5rem; color: #9CA3AF;'>/ 100</span></h1></div>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style="width: 100%; background-color: white; border: 1px solid #CBD5E1; border-radius: 12px; height: 28px; overflow: hidden; margin-top: 5px;">
        <div style="width: {mean_score}%; background-color: {g_color}; height: 100%; transition: width 0.5s ease-in-out;"></div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
with st.expander("🔍 Preview Dataset Bersih"):
    st.dataframe(df.head(15), use_container_width=True)
