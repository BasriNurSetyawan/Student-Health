import streamlit as st
import pandas as pd
from utils.helper import load_data, train_model

st.set_page_config(page_title="Simulator AI", page_icon="📈", layout="wide")
df = load_data()
model, features, r2, mae, rmse, cv_mean = train_model(df)

st.markdown("<h2 style='color: #1E3A8A;'>📈 Aplikasi Simulator Prediksi Nilai Cerdas</h2>", unsafe_allow_html=True)
st.markdown("Gunakan panel di bawah untuk mensimulasikan kebiasaan harian seorang mahasiswa. AI akan memberikan estimasi nilai secara *real-time*.")
st.markdown("---")

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("##### 📚 Komponen Akademis")
    p_study = st.slider("Jam Belajar (Harian)", 0.0, 10.0, 4.0)
    p_attend = st.slider("Tingkat Kehadiran Kelas (%)", 50.0, 100.0, 90.0)
    p_part_time = st.selectbox("Status Kerja Part-Time?", [0, 1], format_func=lambda x: "Ya" if x == 1 else "Tidak")
with c2:
    st.markdown("##### 🎮 Komponen Hiburan & Fisik")
    p_screen = st.slider("Total Screen Time (Sosmed + Netflix / Jam)", 0.0, 15.0, 4.0)
    p_exercise = st.slider("Frekuensi Olahraga (Kali/Minggu)", 0, 6, 2)
    p_eskul = st.selectbox("Aktif Kegiatan Ekstrakurikuler?", [0, 1], format_func=lambda x: "Ya" if x == 1 else "Tidak")
with c3:
    st.markdown("##### 🧠 Komponen Kesehatan")
    p_sleep = st.slider("Durasi Istirahat/Tidur Harian", 3.0, 12.0, 7.0)
    p_mental = st.slider("Kondisi Kesehatan Mental (1-10)", 1, 10, 8)

input_df = pd.DataFrame([[p_study, p_screen, p_attend, p_sleep, p_mental, p_exercise, p_part_time, p_eskul]], columns=features)
pred = model.predict(input_df)[0]

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>🎯 Output Evaluasi Kecerdasan Buatan:</h3>", unsafe_allow_html=True)

res_col1, res_col2 = st.columns([1, 1])
with res_col1:
    st.markdown("<div style='text-align: center; background-color: #F3F4F6; padding: 15px; border-radius: 8px;'>", unsafe_allow_html=True)
    st.metric("Estimasi Skor Akhir Ujian:", f"{pred:.1f} / 100")
    st.markdown("</div>", unsafe_allow_html=True)

with res_col2:
    if pred >= 85:
        st.success("🏆 **Kategori: Sangat Memuaskan (A).** Kombinasi gaya hidup dan komitmen akademis mahasiswa ini berada di zona ideal untuk meraih performa tertinggi.")
    elif pred >= 65:
        st.warning("⚠️ **Kategori: Cukup (B/C).** Mahasiswa diprediksi aman, namun disarankan untuk menekan durasi *waktu layar* guna mengoptimalkan jam belajar.")
    else:
        st.error("🚨 **Kategori: Risiko Tinggi (D/E).** Pola kebiasaan ini sangat riskan. Diperlukan intervensi segera untuk memulihkan stabilitas akademik mahasiswa.")
