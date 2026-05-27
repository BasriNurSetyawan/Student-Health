import streamlit as st
import plotly.graph_objects as go
from utils.helper import load_data, train_model

st.set_page_config(page_title="Evaluasi Model", page_icon="📉", layout="wide")
df = load_data()
model, features, r2, mae, rmse, cv_mean = train_model(df)

st.markdown("<h2 style='color: #1E3A8A;'>📉 Laporan Akurasi & Tingkat Galat Model</h2>", unsafe_allow_html=True)
st.markdown("Evaluasi performa statistik dari model Random Forest Regressor menggunakan data uji dan validasi silang.")
st.markdown("---")

r2_pct = float(r2 * 100)
cv_pct = float(cv_mean * 100)

def get_metric_color(val):
    if val >= 80: return "#10B981"
    elif val >= 60: return "#F59E0B"
    return "#EF4444"

c1, c2 = st.columns(2)

with c1:
    st.markdown("<h4 style='text-align: center; color: #1E3A8A;'>R-Squared Accuracy (Data Uji)</h4>", unsafe_allow_html=True)
    color_r2 = get_metric_color(r2_pct)
    fig_r2 = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = r2_pct,
        number = {'suffix': "%", 'font': {'size': 36, 'color': color_r2}},
        gauge = {
            'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "#CBD5E1"},
            'bar': {'color': color_r2},
            'bgcolor': "white",
            'borderwidth': 1,
            'bordercolor': "#E5E7EB",
            'steps': [{'range': [0, 100], 'color': "white"}]
        }
    ))
    fig_r2.update_layout(height=240, margin=dict(l=30, r=30, t=10, b=10))
    st.plotly_chart(fig_r2, use_container_width=True)

with c2:
    st.markdown("<h4 style='text-align: center; color: #1E3A8A;'>5-Fold Cross Validation Mean</h4>", unsafe_allow_html=True)
    color_cv = get_metric_color(cv_pct)
    fig_cv = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = cv_pct,
        number = {'suffix': "%", 'font': {'size': 36, 'color': color_cv}},
        gauge = {
            'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "#CBD5E1"},
            'bar': {'color': color_cv},
            'bgcolor': "white",
            'borderwidth': 1,
            'bordercolor': "#E5E7EB",
            'steps': [{'range': [0, 100], 'color': "white"}]
        }
    ))
    fig_cv.update_layout(height=240, margin=dict(l=30, r=30, t=10, b=10))
    st.plotly_chart(fig_cv, use_container_width=True)

st.markdown("---")
st.markdown("### 📉 Parameter Loss & Nilai Galat (Error)")

col_l1, col_l2 = st.columns(2)
with col_l1:
    st.markdown("<div style='background-color: #FEF2F2; padding: 15px; border-radius: 8px; border-left: 5px solid #EF4444;'> <h5 style='color: #991B1B; margin:0;'>Mean Absolute Error (MAE): " + f"{mae:.3f}</h5> </div>", unsafe_allow_html=True)
    st.write("Mengukur selisih linear rata-rata hasil prediksi AI dengan poin riil. Nilai galat yang kecil mengonfirmasi kedekatan akurasi model.")

with col_l2:
    st.markdown("<div style='background-color: #FFF7ED; padding: 15px; border-radius: 8px; border-left: 5px solid #F97316;'> <h5 style='color: #C2410C; margin:0;'>Root Mean Squared Error (RMSE): " + f"{rmse:.3f}</h5> </div>", unsafe_allow_html=True)
    st.write("Menerapkan bobot kuadrat kesalahan prediksi untuk mendeteksi varians deviasi ekstrem. Nilai RMSE yang stabil menjamin keandalan prediksi.")
