import streamlit as st
import pandas as pd
import plotly.express as px
from utils.helper import load_data, train_model

st.set_page_config(page_title="Metodologi Sistem", page_icon="🔬", layout="wide")
df = load_data()
model, features, r2, mae, rmse, cv_mean = train_model(df)

st.markdown("<h2 style='color: #1E3A8A;'>🔬 Kerangka Kerja Teoretis & Feature Importance</h2>", unsafe_allow_html=True)
st.markdown("Landasan ilmiah pemilihan arsitektur model komputasi cerdas.")
st.markdown("---")

col_m1, col_m2 = st.columns([1, 1.3])

with col_m1:
    st.markdown("<h4 style='color: #1E3A8A;'>🌲 Arsitektur Model: Random Forest</h4>", unsafe_allow_html=True)
    st.markdown("""
    Sistem menggunakan **Random Forest Regressor** dengan optimasi struktur (`n_estimators=150`, `max_depth=10`). 
    Algoritma ini bekerja dengan membangun 150 pohon keputusan independen (*Ensemble Learning*) melalui mekanisme pembagian sampel acak (*Bagging*).
    
    **Alasan Bebas Epoch:** Karena berbasis struktur pohon (*tree-based split*), algoritma membagi hierarki percabangan data secara matematis lewat kalkulasi indeks, sehingga **tidak memerlukan iterasi berbasis Epoch** layaknya arsitektur *Neural Network/Deep Learning*.
    """)

with col_m2:
    st.markdown("<h4 style='text-align: center;'>Arsitektur Pengaruh Variabel (Feature Importance)</h4>", unsafe_allow_html=True)
    importances = model.feature_importances_

    kamus_fitur = {
        'study_hours_per_day': 'Jam Belajar',
        'total_screen_time': 'Total Screen Time',
        'attendance_percentage': 'Persentase Kehadiran',
        'sleep_hours': 'Durasi Tidur',
        'mental_health_rating': 'Rating Mental',
        'exercise_frequency': 'Frekuensi Olahraga',
        'is_part_time': 'Status Kerja Part-Time',
        'is_extracurricular': 'Keaktifan Eskul'
    }
    
    df_imp = pd.DataFrame({'Faktor': features, 'Tingkat Pengaruh': importances})
    df_imp['Faktor'] = df_imp['Faktor'].map(kamus_fitur)
    df_imp = df_imp.sort_values(by='Tingkat Pengaruh', ascending=True)
    
    fig = px.bar(df_imp, x='Tingkat Pengaruh', y='Faktor', orientation='h', 
                 color='Tingkat Pengaruh', color_continuous_scale="Blues", template="plotly_white")
    st.plotly_chart(fig, use_container_width=True)
