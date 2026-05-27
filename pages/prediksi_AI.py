import streamlit as st
import pandas as pd
from utils.helper import load_data, train_model

st.set_page_config(page_title="Prediksi AI", page_icon="📈", layout="wide")
df = load_data()
model, features, r2, mae, rmse, cv_mean = train_model(df)

st.markdown("<h2 style='color: #1E3A8A;'>📈 Simulator Prediksi Nilai Akademik</h2>", unsafe_allow_html=True)
st.markdown("Sesuaikan slider parameter kebiasaan di bawah ini untuk mengestimasi akumulasi skor ujian secara real-time.")
st.markdown("---")

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("##### 📚 Komponen Akademis")
    p_study = st.slider("Jam Belajar (Harian)", 0.0, 10.0, 4.0)
    p_attend = st.slider("Tingkat Kehadiran Kelas (%)", 50.0, 100.0, 90.0)
    p_part_time = st.selectbox("Status Kerja Part-Time?", [0, 1], format_func=lambda x: "Ya" if x == 1 else "Tidak")
with c2:
    st.markdown("##### 🎮 Komponen Hiburan & Fisik")
    p_screen = st.slider("Total Screen Time (Jam)", 0.0, 15.0, 4.0)
    p_exercise = st.slider("Frekuensi Olahraga (Kali/Minggu)", 0, 6, 2)
    p_eskul = st.selectbox("Aktif Kegiatan Ekstrakurikuler?", [0, 1], format_func=lambda x: "Ya" if x == 1 else "Tidak")
with c3:
    st.markdown("##### 🧠 Komponen Kesehatan")
    p_sleep = st.slider("Durasi Tidur Harian (Jam)", 3.0, 12.0, 7.0)
    p_mental = st.slider("Kondisi Kesehatan Mental (1-10)", 1, 10, 8)

input_df = pd.DataFrame([[p_study, p_screen, p_attend, p_sleep, p_mental, p_exercise, p_part_time, p_eskul]], columns=features)
pred = float(model.predict(input_df)[0])

st.markdown("---")
st.markdown("<h3 style='text-align: center; color: #1E3A8A;'>🎯 Hasil Proyeksi Kecerdasan Buatan</h3>", unsafe_allow_html=True)

if pred >= 85:
    bar_color = "#10B981"
    status_text = "🏆 **Kategori: Sangat Memuaskan (A).** Kombinasi aktivitas harian dan kehadiran kelas berada dalam rentang ideal untuk mencapai prestasi puncak."
    st_msg = st.success
elif pred >= 65:
    bar_color = "#F59E0B"
    status_text = "⚠️ **Kategori: Cukup (B/C).** Akumulasi skor aman, namun disarankan mengoptimalkan fokus dengan mereduksi durasi screen time harian."
    st_msg = st.warning
else:
    bar_color = "#EF4444"
    status_text = "🚨 **Kategori: Risiko Tinggi (D/E).** Konfigurasi kebiasaan harian ini sangat riskan dan berpotensi memicu kegagalan akademis."
    st_msg = st.error

res_col1, res_col2 = st.columns([1, 1])

with res_col1:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align: center;'><h1 style='color: {bar_color}; font-size: 3.5rem; margin-bottom: 10px;'>{pred:.1f} <span style='font-size: 1.5rem; color: #9CA3AF;'>/ 100</span></h1></div>", unsafe_allow_html=True)

    st.markdown(f"""
    <div style="width: 100%; background-color: white; border: 1px solid #CBD5E1; border-radius: 12px; height: 32px; overflow: hidden; margin-top: 5px;">
        <div style="width: {pred}%; background-color: {bar_color}; height: 100%; transition: width 0.5s ease-in-out;"></div>
    </div>
    """, unsafe_allow_html=True)

with res_col2:
    st.markdown("<br><br>", unsafe_allow_html=True)
    st_msg(status_text)
