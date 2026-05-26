import streamlit as st
import pandas as pd
from utils.helper import load_data

st.set_page_config(page_title="Beranda - Student Habits", page_icon="🏠", layout="wide")

df = load_data()

if df is None:
    st.error("❌ Dataset 'student_habits_performance.csv' tidak ditemukan!")
    st.stop()

st.title("🎓 Analisis Kebiasaan & Performa Akademik Mahasiswa")
st.markdown("Dashboard ini menganalisis bagaimana kebiasaan harian (tidur, sosmed, nonton Netflix) dan tingkat kehadiran berdampak pada **Nilai Ujian (Exam Score)** mahasiswa.")


st.markdown("### 📌 Ringkasan Data Saat Ini")
kpi1, kpi2, kpi3, kpi4 = st.columns(4)
kpi1.metric("Total Sampel Tersedia", f"{len(df)} Mahasiswa")
kpi2.metric("Rerata Nilai Ujian", f"{df['exam_score'].mean():.1f} / 100")
kpi3.metric("Rerata Kehadiran", f"{df['attendance_percentage'].mean():.1f}%")
kpi4.metric("Rerata Main Sosmed", f"{df['social_media_hours'].mean():.1f} Jam/Hari")

st.markdown("---")
st.markdown("### 📂 Preview Dataset Mentah")
st.dataframe(df.head(15), use_container_width=True)
