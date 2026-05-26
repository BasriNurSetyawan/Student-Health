import streamlit as st
from utils.helper import load_data, train_model

st.set_page_config(page_title="Evaluasi", page_icon="📉", layout="wide")
df = load_data()
model, features, r2, mae, rmse, cv_mean = train_model(df)

st.title("📉 Laporan Metrik Akurasi & Loss Data")

m1, m2 = st.columns(2)
m1.metric("R-Squared (Akurasi Model)", f"{r2*100:.2f}%")
m2.metric("5-Fold Cross Validation Score", f"{cv_mean*100:.2f}%")

st.markdown("---")
st.subheader("📉 Analisis Loss Model (Tingkat Error)")
l1, l2 = st.columns(2)
with l1:
    st.error(f"#### Mean Absolute Error (MAE): {mae:.2f}")
    st.markdown(f"Rata-rata kesalahan model hanya meleset sebesar **{mae:.1f} poin** dari nilai asli mahasiswa. Nilai yang kecil membuktikan AI sangat akurat.")
with l2:
    st.warning(f"#### Root Mean Squared Error (RMSE): {rmse:.2f}")
    st.markdown("Fungsi kerugian untuk menghukum kesalahan ekstrem. Angka RMSE yang rendah menandakan algoritma stabil.")
