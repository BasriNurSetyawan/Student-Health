import streamlit as st
import plotly.express as px
from utils.helper import load_data

st.set_page_config(page_title="Visualisasi Data", page_icon="📊", layout="wide")

df = load_data()

with st.sidebar:
    st.markdown("### 🎛️ Filter Data")
    selected_gender = st.multiselect("Pilih Gender:", options=df['gender'].unique(), default=df['gender'].unique())
    selected_diet = st.multiselect("Kualitas Diet:", options=df['diet_quality'].unique(), default=df['diet_quality'].unique())

df_filtered = df[(df['gender'].isin(selected_gender)) & (df['diet_quality'].isin(selected_diet))]

st.title("📊 Exploratory Data Analysis (EDA)")
st.markdown("Menganalisis faktor-faktor yang paling mempengaruhi skor ujian.")

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
        color="extracurricular_participation", 
        template="plotly_white",
        labels={"netflix_hours": "Jam Netflix/Hari", "exam_score": "Nilai Ujian"}
    )
    st.plotly_chart(fig_netflix, use_container_width=True)

st.markdown("---")
st.markdown("#### Distribusi Nilai Ujian Berdasarkan Diet & Olahraga")
fig_box = px.box(
    df_filtered, x="diet_quality", y="exam_score", color="part_time_job",
    title="Pengaruh Pola Makan dan Kerja Part-Time Terhadap Nilai Ujian"
)
st.plotly_chart(fig_box, use_container_width=True)
