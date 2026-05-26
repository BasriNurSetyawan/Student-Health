import pandas as pd
import numpy as np
import streamlit as st
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

@st.cache_data
def load_data():
    try:
        df = pd.read_csv('student_habits_performance.csv')
        
        df = df.ffill()
        
        df_augmented = df.sample(n=100, replace=True, random_state=42).copy()
        df_augmented['study_hours_per_day'] = df_augmented['study_hours_per_day'] + np.random.uniform(-0.1, 0.1, size=100)
        df_augmented['study_hours_per_day'] = df_augmented['study_hours_per_day'].clip(lower=0)
        df = pd.concat([df, df_augmented], ignore_index=True)
        
        df['total_screen_time'] = df['social_media_hours'] + df['netflix_hours']

        kamus_yes_no = {'Yes': 1, 'No': 0}
        df['is_part_time'] = df['part_time_job'].map(kamus_yes_no)
        df['is_extracurricular'] = df['extracurricular_participation'].map(kamus_yes_no)
        
        def kategori_olahraga(x):
            if x <= 1: return 'Buruk'
            elif x <= 3: return 'Cukup'
            else: return 'Baik'
        df['kualitas_olahraga'] = df['exercise_frequency'].apply(kategori_olahraga)
        
        return df
    except FileNotFoundError:
        return None

@st.cache_resource
def train_model(df):
    features = ['study_hours_per_day', 'total_screen_time', 'attendance_percentage', 
                'sleep_hours', 'mental_health_rating', 'exercise_frequency',
                'is_part_time', 'is_extracurricular']
    
    X = df[features].copy()
    y = df['exam_score'].copy() 
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestRegressor(n_estimators=150, random_state=42, max_depth=10, min_samples_split=4)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    
    cv_scores = cross_val_score(model, X, y, cv=5, scoring='r2')
    cv_mean = cv_scores.mean()
    
    return model, features, r2, mae, rmse, cv_mean
