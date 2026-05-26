import streamlit as st
import pandas as pd
from utils.helper import load_data

st.set_page_config(page_title="Beranda - Burnout Analytics", page_icon="🏠", layout="wide")

df = load_data()

if df is None:
    st.error("❌ Dataset 'student_mental_health_burnout.csv' tidak ditemukan di folder!")
    st.stop()

st.title("🎓 Sistem Analisis Mental Health & Burnout")
st.markdown("Selamat datang! Dashboard ini dirancang khusus untuk memonitor tingkat kelelahan mental (Burnout) pada mahasiswa menggunakan data gaya hidup dan asesmen psikologis.")

st.info("👈 Buka icon hamburger (☰) di pojok kiri atas untuk melihat visualisasi data dan mencoba Prediksi AI.")

st.markdown("### 📌 Metrik Mahasiswa Saat Ini")
kpi1, kpi2, kpi3, kpi4 = st.columns(4)
kpi1.metric("Total Sampel", f"{len(df)} Data")
kpi2.metric("Rerata Screen Time", f"{df['screen_time_hours'].mean():.1f} Jam")
kpi3.metric("Rerata Kecemasan", f"{df['anxiety_score'].mean():.1f} / 10")
kpi4.metric("Rerata Depresi", f"{df['depression_score'].mean():.1f} / 10")

st.markdown("---")
st.markdown("### 📂 Preview Dataset Mentah")
st.dataframe(df.head(15), use_container_width=True)
