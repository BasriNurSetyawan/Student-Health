import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Manipulasi Data", page_icon="⚙️", layout="wide")

st.title("⚙️ Transparansi Manipulasi & Pengolahan Data")
st.markdown("Dokumentasi detail mengenai *Preprocessing*, *Feature Engineering*, *Selection*, dan *Augmentation*.")

try:
    df_raw = pd.read_csv('student_habits_performance.csv')
except FileNotFoundError:
    st.error("File mentah tidak ditemukan!")
    st.stop()


st.header("Imputasi Missing Values")
col_na1, col_na2 = st.columns([1, 2])

missing_data = df_raw.isna().sum()
missing_cols = missing_data[missing_data > 0]

with col_na1:
    st.error(f"**Data Mentah Awal:** {len(df_raw)} Baris")
    if not missing_cols.empty:
        st.write("🚨 Terdeteksi Kolom Kosong:")
        for col, count in missing_cols.items():
            st.write(f"- `{col}`: Hilang {count} data")

with col_na2:
    st.success("**Metode: Forward Fill (ffill)**")
    st.markdown("""
    Sistem **tidak menghapus (drop)** baris yang kosong agar jumlah data tidak menyusut. Sistem mengisi data yang bolong dengan menduplikasi nilai dari baris sebelumnya secara berurutan. Hasilnya data kembali utuh 1.000 sampel.
    """)

st.markdown("---")


st.header("Feature Engineering & Encoding")
c_fe1, c_fe2, c_fe3 = st.columns(3)

with c_fe1:
    st.info("💻 **Penggabungan Fitur (Screen Time)**")
    st.markdown("Kolom `social_media_hours` + `netflix_hours` digabung jadi **`total_screen_time`** agar AI lebih fokus pada total durasi layar.")

with c_fe2:
    st.warning("🔢 **Label Encoding**")
    st.markdown("Kolom `part_time_job` dan `extracurricular` yang berisi Yes/No dikonversi menjadi angka **1 dan 0** agar bisa dibaca algoritma.")

with c_fe3:
    st.success("🏃 **Binning (Olahraga)**")
    st.markdown("Angka frekuensi olahraga dikelompokkan menjadi kategori ordinal: **Buruk (0-1), Cukup (2-3), Baik (4-6)**.")

st.markdown("---")

st.header("Feature Selection (Penyaringan Kolom)")
st.markdown("Dari total 16 kolom mentah, hanya **8 fitur inti** yang diteruskan ke dalam arsitektur AI. Sisa kolom lainnya dieliminasi dengan alasan ilmiah berikut:")

st.markdown("""
- 🗑️ **`student_id`**: Memiliki kardinalitas terlalu tinggi (semua unik) dan tidak memiliki pola relasional.
- 🗑️ **`age`, `gender`, `parental_education_level`**: Adalah faktor demografis bawaan. AI ini difokuskan pada analisis **Actionable Habits** (kebiasaan yang bisa diubah/diperbaiki oleh mahasiswa).
- 🗑️ **`diet_quality`, `internet_quality`**: Di-drop untuk melakukan *Dimensionality Reduction* (mengurangi beban model) guna mencegah terjadinya *Overfitting* akibat terlalu banyak variabel yang kurang berkorelasi tajam dengan nilai akhir.
""")

st.markdown("---")


st.header("Data Augmentation & Noise Injection")

col_aug1, col_aug2 = st.columns(2)

with col_aug1:
    st.markdown("Proses:")
    st.code("""
# 1. Re-sampling 100 data
df_augmented = df.sample(n=100, replace=True)

# 2. Injeksi Gaussian Noise ke Jam Belajar
noise = np.random.uniform(-0.1, 0.1, size=100)
df_augmented['study_hours_per_day'] += noise

# 3. Gabungkan
df_final = pd.concat([df, df_augmented])
    """, language='python')

with col_aug2:
    st.markdown("Hasil Akhir")
    st.metric("Data Mentah", "1.000 Sampel")
    st.metric("Data Sintetis", "+ 100 Sampel")
    st.metric("Dataset Final AI", "1.100 Sampel ✅")
    st.caption("Penambahan noise secara sengaja memaksa algoritma untuk melakukan generalisasi pola, bukan sekadar menghafal angka repetitif.")
