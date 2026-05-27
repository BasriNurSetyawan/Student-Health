import streamlit as st
import pandas as pd
from utils.helper import load_data

st.set_page_config(page_title="Dashboard Utama", page_icon="🎓", layout="wide")

df = load_data()
if df is None:
    st.error("❌ File dataset 'student_habits_performance.csv' tidak ditemukan!")
    st.stop()

st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>🏛️ Sistem Analisis Akademik & Pola Hidup Mahasiswa</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 16px; color: #4B5563;'>Platform analitik cerdas berbasis Machine Learning untuk mendeteksi pengaruh gaya hidup terhadap pencapaian nilai ujian.</p>", unsafe_allow_html=True)
st.markdown("---")

with st.container():
    k1, k2, k3, k4 = st.columns(4)
    with k1:
        st.markdown("<div style='background-color: #F3F4F6; padding: 20px; border-radius: 10px; border-left: 5px solid #1E3A8A;'>", unsafe_allow_html=True)
        st.metric("Total Sampel Aktif", f"{len(df)} Baris")
        st.markdown("</div>", unsafe_allow_html=True)
    with k2:
        st.markdown("<div style='background-color: #F3F4F6; padding: 20px; border-radius: 10px; border-left: 5px solid #10B981;'>", unsafe_allow_html=True)
        st.metric("Rerata Skor Ujian", f"{df['exam_score'].mean():.1f} / 100")
        st.markdown("</div>", unsafe_allow_html=True)
    with k3:
        st.markdown("<div style='background-color: #F3F4F6; padding: 20px; border-radius: 10px; border-left: 5px solid #F59E0B;'>", unsafe_allow_html=True)
        st.metric("Rerata Kehadiran Kelas", f"{df['attendance_percentage'].mean():.1f}%")
        st.markdown("</div>", unsafe_allow_html=True)
    with k4:
        st.markdown("<div style='background-color: #F3F4F6; padding: 20px; border-radius: 10px; border-left: 5px solid #EF4444;'>", unsafe_allow_html=True)
        st.metric("Rerata Waktu Layar", f"{df['total_screen_time'].mean():.1f} Jam")
        st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("---")
with st.expander("🔍 Buka Peninjau Dataset Bersih (Cleaned Data Preview)"):
    st.dataframe(df.head(25), use_container_width=True)
