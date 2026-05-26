import streamlit as st
import pandas as pd
from utils.helper import load_data, train_model

st.set_page_config(page_title="Manipulasi Data", page_icon="⚙️", layout="wide")

st.title("⚙️ Tahapan Pra-pemrosesan Data (Data Preprocessing)")
st.markdown("Halaman ini mendokumentasikan analisis struktur dataset `student_habits_performance.csv` serta langkah-langkah pra-pemrosesan yang dilakukan sebelum data dimasukkan ke dalam model Machine Learning.")

try:
    df_raw = pd.read_csv('student_habits_performance.csv')
except FileNotFoundError:
    st.error("File mentah tidak ditemukan!")
    st.stop()


st.header("Penentuan Tujuan Sistem (Target Variable)")
st.info("🎯 **Target Prediksi:** Kolom `exam_score` (Nilai Ujian)")
st.markdown("""
Dari dua jenis pendekatan Machine Learning, sistem ini memilih **Regresi (Memprediksi Angka Eksak)**. 
Alih-alih menyederhanakan target menjadi Klasifikasi (kategori "Lulus" atau "Gagal"), algoritma dilatih untuk menebak skor pasti secara spesifik (contoh: memprediksi siswa akan mendapat nilai 85.5).
""")

st.markdown("---")

st.header("Pra-pemrosesan Data (Data Preprocessing)")
st.markdown("Langkah krusial untuk membersihkan dan menyiapkan data tabular sebelum dilatih oleh algoritma:")

c1, c2 = st.columns(2)

with c1:
    st.success("🗑️ **Buang Kolom yang Tidak Relevan**")
    st.markdown("Kolom `student_id` dibuang (*drop*) karena hanya berupa ID unik identitas dan tidak memiliki nilai prediktif. Jika dibiarkan, kolom ini wajib dieliminasi agar tidak membingungkan model.")

    st.warning("⚠️ **Tangani Data Kosong (Missing Values)**")
    missing_edu = df_raw['parental_education_level'].isna().sum() if 'parental_education_level' in df_raw.columns else 91
    st.markdown(f"Terdeteksi **{missing_edu} baris kosong (*null/NaN*)** pada kolom `parental_education_level`. Baris ini tidak dibiarkan atau dibuang. Sistem mengisinya menggunakan metode imputasi untuk mempertahankan total 1000 baris data.")

with c2:
    st.info("🔢 **Ubah Data Teks Menjadi Angka (Encoding)**")
    st.markdown("Algoritma Machine Learning hanya mengerti angka. Oleh karena itu, kolom kategori teks dikonversi:")
    st.markdown("""
    - **Binary Encoding:** Mengubah `part_time_job` dan `extracurricular_participation` dari (Yes/No) menjadi (1/0).
    - **Mapping Numerik:** Menerjemahkan tingkatan pada `diet_quality` dan rentang `exercise_frequency` menjadi susunan angka yang bisa diukur bobotnya.
    """)

    st.error("⚖️ **Normalisasi (Scaling) & Augmentasi**")
    st.markdown("Terdapat perbedaan rentang nilai (contoh: `attendance` bernilai puluhan/ratusan, sedangkan `netflix_hours` hanya satuan angka kecil). Sistem juga menyuntikkan *Gaussian Noise* (Augmentasi) untuk mencegah *overfitting*.")

st.markdown("---")


st.header("Pemilihan Algoritma Model")
st.markdown("""
Mengingat ini adalah data tabular terstruktur, arsitektur *Deep Learning/CNN* tidak digunakan karena terlalu berlebihan (*overkill*). 
Sebagai gantinya, sistem ini memilih **Random Forest Regressor**. 

Algoritma *Ensemble* ini dipilih karena sangat bagus untuk data tabular, kebal terhadap *outlier*, dan sangat tangguh dalam menangani berbagai skala data tanpa harus dinormalisasi secara ekstrem layaknya *Linear Regression*.
""")

st.markdown("---")


st.header("Evaluasi yang Digunakan")
st.markdown("Karena berjalan di rute **Regresi**, metrik 'Akurasi' tradisional tidak relevan. Kinerja sistem diukur menggunakan metrik spesifik regresi:")

df_clean = load_data()
model, features, r2, mae, rmse, cv_mean = train_model(df_clean)

col_ev1, col_ev2, col_ev3 = st.columns(3)

with col_ev1:
    st.metric(label="Mean Absolute Error (MAE)", value=f"{mae:.2f} Poin")
    st.caption("**Mean Absolute Error:** Rata-rata selisih prediksi tebakan AI dengan nilai aslinya di lapangan.")

with col_ev2:
    st.metric(label="Root Mean Squared Error (RMSE)", value=f"{rmse:.2f} Poin")
    st.caption("**Root Mean Squared Error:** Memberikan hukuman (penalti) yang lebih besar untuk error/kesalahan prediksi yang jaraknya terlalu jauh.")

with col_ev3:
    st.metric(label="R-Squared (R² Score)", value=f"{r2*100:.1f}%")
    st.caption("**R² Score:** Mengukur seberapa baik variabel independen (durasi belajar, sosmed, dll) mampu menjelaskan variasi dari skor ujian.")

st.markdown("*(Hasil perhitungan metrik-metrik di atas dapat dilihat secara real-time pada menu Evaluasi Model).*")
