import streamlit as st
import pandas as pd
import plotly.express as px
from utils.helper import load_data, train_model

st.set_page_config(page_title="Metodologi", page_icon="🔬", layout="wide")
df = load_data()
model, features, r2, mae, rmse, cv_mean = train_model(df)

st.title("🔬 Metodologi AI & Feature Importance")

col1, col2 = st.columns([1, 1.5])

with col1:
    st.info("### 🌲 Algoritma: Random Forest")
    st.markdown("""
    AI menggunakan algoritma **Random Forest Regressor** dengan teknik *Hyperparameter Tuning* (`max_depth=10`, `min_samples_split=4`) untuk menebak angka kontinu tanpa terjebak dalam *overfitting*.
    Model menggabungkan tebakan dari 150 pohon keputusan independen.
    """)

with col2:
    st.subheader("📊 Fitur Paling Berpengaruh Terhadap Nilai")
    importances = model.feature_importances_
    df_imp = pd.DataFrame({'Faktor': features, 'Pengaruh': importances}).sort_values(by='Pengaruh', ascending=True)
    fig = px.bar(df_imp, x='Pengaruh', y='Faktor', orientation='h', color='Pengaruh', color_continuous_scale='Blues')
    st.plotly_chart(fig, use_container_width=True)
