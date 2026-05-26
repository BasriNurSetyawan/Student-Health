import streamlit as st
import pandas as pd
from utils.helper import load_data

st.set_page_config(page_title="Beranda", page_icon="🏠", layout="wide")

df = load_data()

if df is None:
    st.error("❌ File dataset 'student_habits_performance.csv' tidak ditemukan!")
    st.stop()

st.title("🎓 Analisis Kebiasaan & Performa Akademik Mahasiswa")
st.markdown("Aplikasi ini mendeteksi bagaimana gaya hidup dan kebiasaan mahasiswa berdampak pada **Nilai Ujian (Exam Score)** menggunakan Machine Learning.")

st.markdown("### 📌 Ringkasan Basis Data (Setelah Preprocessing)")
k1, k2, k3, k4 = st.columns(4)
k1.metric("Total Sampel Aktif", f"{len(df)} Baris")
k2.metric("Rerata Skor Ujian", f"{df['exam_score'].mean():.1f} / 100")
k3.metric("Rerata Kehadiran", f"{df['attendance_percentage'].mean():.1f}%")
k4.metric("Rerata Waktu Layar", f"{df['total_screen_time'].mean():.1f} Jam")

st.markdown("---")
st.subheader("📂 Cuplikan Dataset Bersih")
st.dataframe(df.head(10), use_container_width=True)
