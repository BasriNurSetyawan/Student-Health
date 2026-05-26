import streamlit as st
import plotly.express as px
from utils.helper import load_data

st.set_page_config(page_title="Visualisasi Data", page_icon="📊", layout="wide")

df = load_data()

with st.sidebar:
    st.markdown("### 🎛️ Filter Data")
    selected_gender = st.multiselect(
        "Pilih Gender:", 
        options=df['gender'].unique(), 
        default=df['gender'].unique()
    )
    
    selected_olahraga = st.multiselect(
        "Kualitas Olahraga:", 
        options=df['kualitas_olahraga'].unique(), 
        default=df['kualitas_olahraga'].unique()
    )

df_filtered = df[
    (df['gender'].isin(selected_gender)) & 
    (df['kualitas_olahraga'].isin(selected_olahraga))
]

st.title("📊 Exploratory Data Analysis (EDA)")
st.markdown("Menganalisis faktor-faktor kebiasaan yang paling mempengaruhi skor ujian.")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Jam Belajar vs Nilai Ujian")
    fig_study = px.scatter(
        df_filtered, x="study_hours_per_day", y="exam_score", 
        color="mental_health_rating", size="attendance_percentage",
        template="plotly_white", color_continuous_scale="Viridis",
        labels={"study_hours_per_day": "Jam Belajar/Hari", "exam_score": "Nilai Ujian"}
    )
    st.plotly_chart(fig_study, use_container_width=True)

with col2:
    st.markdown("#### Nonton Netflix vs Nilai Ujian")
    fig_netflix = px.scatter(
        df_filtered, x="netflix_hours", y="exam_score", 
        color="kualitas_olahraga", 
        template="plotly_white",
        labels={"netflix_hours": "Jam Netflix/Hari", "exam_score": "Nilai Ujian"},
        color_discrete_map={"Buruk": "red", "Cukup": "orange", "Baik": "green"}
    )
    st.plotly_chart(fig_netflix, use_container_width=True)

st.markdown("---")
st.markdown("#### Distribusi Nilai Ujian Berdasarkan Kualitas Olahraga")
fig_box = px.box(
    df_filtered, x="kualitas_olahraga", y="exam_score", color="kualitas_olahraga",
    title="Apakah Mahasiswa yang Sering Olahraga Punya Nilai Lebih Baik?",
    category_orders={"kualitas_olahraga": ["Buruk", "Cukup", "Baik"]},
    color_discrete_map={"Buruk": "red", "Cukup": "orange", "Baik": "green"}
)
st.plotly_chart(fig_box, use_container_width=True)
