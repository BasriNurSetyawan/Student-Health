import streamlit as st
import pandas as pd
from utils.helper import load_data, train_model

st.set_page_config(page_title="Prediksi Skor Ujian", page_icon="📈", layout="wide")

df = load_data()
model, features, accuracy = train_model(df)

st.title("📈 AI Prediktor Nilai Ujian")
st.markdown("Atur kebiasaan mahasiswa di bawah ini. AI Random Forest Regressor akan menebak berapa **Skor Ujian** yang akan didapat!")

st.info(f"🤖 Model AI Aktif (R2 Score / Akurasi Prediksi: {accuracy*100:.1f}%)")

c_in1, c_in2, c_in3 = st.columns(3)

with c_in1:
    p_study = st.slider("Jam Belajar (Harian)", 0.0, 10.0, 3.5)
    p_attend = st.slider("Persentase Kehadiran (%)", 50.0, 100.0, 85.0)

with c_in2:
    p_sosmed = st.slider("Main Sosmed (Harian)", 0.0, 10.0, 2.5)
    p_netflix = st.slider("Nonton Netflix (Harian)", 0.0, 8.0, 1.5)
    
with c_in3:
    p_sleep = st.slider("Jam Tidur", 3.0, 12.0, 7.0)
    p_mental = st.slider("Rating Mental Health (1-10)", 1, 10, 5)

# EKSEKUSI AI
input_df = pd.DataFrame([[p_study, p_sosmed, p_netflix, p_attend, p_sleep, p_mental]], columns=features)
pred_score = model.predict(input_df)[0]

st.markdown("---")
st.subheader("🎯 Hasil Prediksi AI:")

col_hasil, _ = st.columns([1, 1])

with col_hasil:
    st.metric("Estimasi Skor Ujian:", f"{pred_score:.1f} / 100")
    
    #feedback logic berdasarkan nilai
    if pred_score >= 80:
        st.success("✅ **Sangat Baik!** Gaya hidup ini berpotensi menghasilkan skor yang tinggi.")
    elif pred_score >= 60:
        st.warning("🟡 **Cukup.** Masih bisa ditingkatkan dengan mengurangi sosmed/netflix atau menambah jam belajar.")
    else:
        st.error("🔴 **Berbahaya.** Dengan pola ini, risiko gagal ujian sangat besar.")
