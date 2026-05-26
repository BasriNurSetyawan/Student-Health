import streamlit as st
import pandas as pd
from utils.helper import load_data, train_model

st.set_page_config(page_title="Prediksi AI", page_icon="🔥", layout="wide")

df = load_data()
model, le, features, accuracy = train_model(df)

st.title("🔥 AI Prediktor Burnout (Real-Time)")
st.markdown("Ubah slider parameter di bawah ini. AI Random Forest akan langsung menganalisis tingkat Burnout mahasiswa.")

st.info(f"🤖 Model Machine Learning Aktif (Akurasi: {accuracy*100:.1f}%)")

c_in1, c_in2, c_in3 = st.columns(3)

with c_in1:
    p_age = st.number_input("Usia (Tahun)", 17, 30, 21)
    p_study = st.slider("Jam Belajar Harian", 0.0, 15.0, 5.0)
    p_sleep = st.slider("Jam Tidur Harian", 0.0, 15.0, 6.0)

with c_in2:
    p_screen = st.slider("Screen Time Harian", 0.0, 18.0, 8.0)
    p_anxiety = st.slider("Skor Kecemasan (1-10)", 1.0, 10.0, 6.0)
    
with c_in3:
    p_depress = st.slider("Skor Depresi (1-10)", 1.0, 10.0, 5.0)
    p_acad = st.slider("Tekanan Akademik (1-10)", 1.0, 10.0, 7.0)
    p_fin = st.slider("Stres Finansial (1-10)", 1.0, 10.0, 4.0)

#Prediksi AI
input_df = pd.DataFrame([[p_age, p_study, p_sleep, p_screen, p_anxiety, p_depress, p_acad, p_fin]], columns=features)
pred_idx = model.predict(input_df)[0]
pred_label = le.inverse_transform([pred_idx])[0]
probs = model.predict_proba(input_df)[0] 

st.markdown("---")
st.subheader("🎯 Hasil Analisis AI:")

col_hasil, col_prob = st.columns([1, 2])

with col_hasil:
    if pred_label == 'Low': 
        st.success(f"### Level Burnout:\n### {pred_label} 🟢")
    elif pred_label == 'Medium': 
        st.warning(f"### Level Burnout:\n### {pred_label} 🟡")
    else: 
        st.error(f"### Level Burnout:\n### {pred_label} 🔴")
        
with col_prob:
    st.markdown("**Confidence Score (Tingkat Keyakinan Model):**")
    for cls, prb in zip(le.classes_, probs):
        if prb > 0: 
            st.progress(float(prb), text=f"{cls} Burnout ({prb*100:.1f}%)")
