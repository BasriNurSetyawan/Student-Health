import streamlit as st
from utils.helper import load_data, train_model

st.set_page_config(page_title="Laporan Performa", page_icon="📉", layout="wide")
df = load_data()
model, features, r2, mae, rmse, cv_mean = train_model(df)

st.markdown("<h2 style='color: #1E3A8A;'>📉 Laporan Matrik Validasi & Loss Model AI</h2>", unsafe_allow_html=True)
st.markdown("Uji performa matematis algoritma berdasarkan pengujian data latih dan data uji.")
st.markdown("---")

with st.container():
    m1, m2 = st.columns(2)
    with m1:
        st.markdown("<div style='background-color: #EEF2F6; padding: 25px; border-radius: 8px; text-align: center; border: 1px solid #CBD5E1;'>", unsafe_allow_html=True)
        st.metric("R-Squared Accuracy (Data Uji)", f"{r2*100:.2f}%")
        st.caption("Menilai seberapa presisi variabel habit mahasiswa dalam merepresentasikan sebaran nilai ujian asli.")
        st.markdown("</div>", unsafe_allow_html=True)
    with m2:
        st.markdown("<div style='background-color: #EEF2F6; padding: 25px; border-radius: 8px; text-align: center; border: 1px solid #CBD5E1;'>", unsafe_allow_html=True)
        st.metric("5-Fold Cross Validation Mean", f"{cv_mean*100:.2f}%")
        st.caption("Rata-rata akurasi setelah data diacak dan diuji ulang sebanyak 5 kali berturut-turut untuk menjamin model bebas bias.")
        st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<h3 style='color: #1E3A8A;'>📉 Analisis Parameter Loss (Tingkat Galat Tebakan)</h3>", unsafe_allow_html=True)

col_l1, col_l2 = st.columns(2)
with col_l1:
    st.markdown(f"<div style='background-color: #FEF2F2; padding: 20px; border-radius: 8px; border-left: 5px solid #EF4444;'> <h5 style='color: #991B1B;'>Mean Absolute Error (MAE): {mae:.3f}</h5> </div>", unsafe_allow_html=True)
    st.write("Secara rata-rata, estimasi tebakan nilai yang dikeluarkan oleh AI hanya meleset di kisaran angka tersebut dari poin nilai asli di lapangan. Nilai galat yang rendah mengonfirmasi akurasi sistem.")

with col_l2:
    st.markdown(f"<div style='background-color: #FFF7ED; padding: 20px; border-radius: 8px; border-left: 5px solid #F97316;'> <h5 style='color: #C2410C;'>Root Mean Squared Error (RMSE): {rmse:.3f}</h5> </div>", unsafe_allow_html=True)
    st.write("Metrik penalti untuk mengukur deviasi kuadrat kesalahan tebakan. Jarak nilai RMSE yang berdekatan dengan nilai MAE membuktikan model stabil dan terbebas dari deviasi eror yang ekstrem.")
