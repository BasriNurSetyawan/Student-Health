import pandas as pd
import streamlit as st
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

@st.cache_data
def load_data():
    try:
        df = pd.read_csv('student_habits_performance.csv')
        return df.dropna().drop_duplicates()
    except FileNotFoundError:
        return None

@st.cache_resource
def train_model(df):
    features = ['study_hours_per_day', 'social_media_hours', 'netflix_hours', 
                'attendance_percentage', 'sleep_hours', 'mental_health_rating']
    
    X = df[features].copy()
    y = df['exam_score'].copy()
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestRegressor(n_estimators=100, random_state=42, max_depth=5)
    model.fit(X_train, y_train)

    akurasi = model.score(X_test, y_test)
    
    return model, features, akurasi
