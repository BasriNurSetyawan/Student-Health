import pandas as pd
import streamlit as st
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

@st.cache_data
def load_data():
    try:
        df = pd.read_csv('student_mental_health_burnout.csv')
        return df.dropna().drop_duplicates()
    except FileNotFoundError:
        return None

@st.cache_resource
def train_model(df):
    features = ['age', 'daily_study_hours', 'daily_sleep_hours', 
                'screen_time_hours', 'anxiety_score', 'depression_score', 
                'academic_pressure_score', 'financial_stress_score']
    
    X = df[features].copy()
    y = df['burnout_level'].copy()
    
    le = LabelEncoder()
    y_encoded = le.fit_transform(y)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier(n_estimators=50, random_state=42, max_depth=5)
    model.fit(X_train, y_train)
    
    akurasi = model.score(X_test, y_test)
    
    return model, le, features, akurasi
