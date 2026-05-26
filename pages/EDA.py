import streamlit as st
import plotly.express as px
from utils.helper import load_data

st.set_page_config(page_title="Visualisasi Data", page_icon="📊", layout="wide")

df = load_data()

# Filter Interaktif di Sidebar
with st.sidebar:
    st.markdown("### 🎛️ Filter Data")
    
    selected_gender = st.multiselect(
        "Pilih Gender:", 
        options=df['gender'].unique(), 
        default=df['gender'].unique()
    )
    
    selected_sleep = st.multiselect(
        "Kualitas Tidur:",
        options=df['sleep_quality'].unique(),
        default=df['sleep_quality'].unique()
    )

df_filtered = df[
    (df['gender'].isin(selected_gender)) & 
    (df['sleep_quality'].isin(selected_sleep))
]

st.title("📊 Exploratory Data Analysis (EDA)")
st.markdown("Analisis korelasi antara kebiasaan harian dengan tingkat Burnout mahasiswa.")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Screen Time vs Kecemasan")
    fig_scatter = px.scatter(
        df_filtered, 
        x="screen_time_hours", y="anxiety_score", 
        color="burnout_level", size="academic_pressure_score",
        template="plotly_white",
        labels={"screen_time_hours": "Jam Natap Layar", "anxiety_score": "Skor Kecemasan"},
        color_discrete_map={"Low": "green", "Medium": "orange", "High": "red"}
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

with col2:
    st.markdown("#### Distribusi Jam Tidur per Level Burnout")
    fig_box = px.box(
        df_filtered, 
        x="burnout_level", y="daily_sleep_hours", color="burnout_level",
        category_orders={"burnout_level": ["Low", "Medium", "High"]},
        color_discrete_map={"Low": "green", "Medium": "orange", "High": "red"}
    )
    st.plotly_chart(fig_box, use_container_width=True)

st.markdown("---")
st.markdown("#### Proporsi Tingkat Burnout Keseluruhan")
risk_counts = df_filtered["burnout_level"].value_counts().reset_index()
risk_counts.columns = ["burnout_level", "Count"]
fig_pie = px.pie(risk_counts, values="Count", names="burnout_level", hole=0.4, 
                 color="burnout_level", color_discrete_map={"Low": "green", "Medium": "orange", "High": "red"})
st.plotly_chart(fig_pie, use_container_width=True)
