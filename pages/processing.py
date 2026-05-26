import streamlit as st
import pandas as pd
from utils.helper import load_data

st.set_page_config(page_title="Preprocessing", page_icon="⚙️", layout="wide")

st.title("⚙️ Analisis Missing Values & Preprocessing")
st.markdown("Laporan komprehensif penanganan *missing values* (data kosong) dan penambahan data secara sintesis.")

try:
    df_raw = pd.read_csv('student_habits_performance.csv')
    total_raw = len(df_raw)
    missing_data = df_raw.isna().sum()
    missing_cols = missing_data[missing_data > 0]
except FileNotFoundError:
    st.error("File mentah tidak ditemukan!")
    st.stop()

col1, col2 = st.columns(2)

with col1:
    st.error(f"### 🛑 Laporan Data Mentah (Raw Data)")
    st.markdown(f"- **Total Data Awal:** {total_raw} Baris")
    if not missing_cols.empty:
        st.markdown("**🚨 Terdeteksi Data Kosong (Missing Values):**")
        for col, count in missing_cols.items():
            st.markdown(f"- Kolom `{col}`: **Hilang {count} data**")
    
    st.markdown("""
    *Jika menggunakan perintah biasa (`dropna`), 91 baris ini akan terhapus dan jumlah data akan menyusut menjadi 909 sampel, yang mengurangi tingkat validitas eksperimen.*
    """)

with col2:
    st.success("### 🛠️ Solusi: Imputasi & Augmentasi")
    st.markdown("""
    Untuk mempertahankan integritas dataset, sistem melakukan metode berikut:
    1. **Forward Fill Imputation:** Mengisi 91 data kosong di atas berdasarkan nilai observasi yang berdekatan. Data kembali utuh 1.000 sampel.
    2. **Data Augmentation:** Untuk membuat model AI kebal (*robust*), 100 sampel di-duplikasi secara acak dan ditambahkan *Gaussian Noise*.
    """)

# Load data bersih
df_clean = load_data()
st.info(f"✅ **Total Dataset Siap Latih (Setelah Preprocessing): {len(df_clean)} Sampel**")

st.markdown("---")
st.subheader("Data Mentah yang Terdeteksi Kosong (NaN)")
st.dataframe(df_raw[df_raw.isna().any(axis=1)].head(10), use_container_width=True)
