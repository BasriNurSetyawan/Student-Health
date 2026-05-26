import streamlit as st
import pandas as pd
from utils.helper import load_data, train_model

st.set_page_config(page_title="Prediksi Skor", page_icon="📈", layout="wide")
df = load_data()
model, features, r2, mae, rmse, cv_mean = train_model(df)

st.title("📈 AI Prediktor Nilai Ujian")
st.markdown("Atur kebiasaan mahasiswa di bawah ini. AI Regresi akan mengevaluasi angka ujiannya secara instan.")

c1, c2, c3 = st.columns(3)
with c1:
    p_study = st.slider("Jam Belajar (Harian)", 0.0, 10.0, 4.0)
    p_attend = st.slider("Persentase Kehadiran (%)", 50.0, 100.0, 90.0)
    p_part_time = st.selectbox("Kerja Part-Time?", [0, 1], format_func=lambda x: "Ya" if x == 1 else "Tidak")
with c2:
    p_screen = st.slider("Total Screen Time (Jam)", 0.0, 15.0, 4.0)
    p_exercise = st.slider("Olahraga (Kali/Minggu)", 0, 6, 3)
    p_eskul = st.selectbox("Ikut Ekstrakurikuler?", [0, 1], format_func=lambda x: "Ya" if x == 1 else "Tidak")
with c3:
    p_sleep = st.slider("Jam Tidur Harian", 3.0, 12.0, 8.0)
    p_mental = st.slider("Kesehatan Mental (1-10)", 1, 10, 7)

input_df = pd.DataFrame([[p_study, p_screen, p_attend, p_sleep, p_mental, p_exercise, p_part_time, p_eskul]], columns=features)
pred = model.predict(input_df)[0]

st.subheader("🎯 Hasil Estimasi Nilai Ujian:")
st.metric("Prediksi Skor Akhir:", f"{pred:.1f} / 100")
if pred >= 85: st.success("✅ **Sangat Memuaskan.** Pola ini berpotensi mencetak nilai A.")
elif pred >= 65: st.warning("🟡 **Cukup.** Kurangi waktu layar untuk meningkatkan fokus.")
else: st.error("🔴 **Kritis.** Kebiasaan pola HIDUP SEPERTI LARRY")
