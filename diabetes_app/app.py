# app.py
import streamlit as st
import pandas as pd
import joblib
import numpy as np
import matplotlib.pyplot as plt

# Load model dan scaler
model = joblib.load("model/random_forest_model.pkl")
scaler = joblib.load("model/scaler.pkl")

st.set_page_config(page_title="Prediksi Diabetes", layout="wide")
st.title("🧠 Aplikasi Prediksi Diabetes - Random Forest")

# TAB UI
tab1, tab2 = st.tabs(["🔍 Prediksi Manual", "📁 Prediksi dari File CSV"])

with tab1:
    st.subheader("Masukkan Data Pasien")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        preg = st.number_input("Pregnancies", 0)
    with col2:
        gluc = st.number_input("Glucose", 0)
    with col3:
        bp = st.number_input("Blood Pressure", 0)
    with col4:
        skin = st.number_input("Skin Thickness", 0)
    with col1:
        insulin = st.number_input("Insulin", 0)
    with col2:
        bmi = st.number_input("BMI", 0.0)
    with col3:
        dpf = st.number_input("Diabetes Pedigree Function", 0.0)
    with col4:
        age = st.number_input("Age", 0)

    if st.button("🔮 Prediksi"):
        data = np.array([[preg, gluc, bp, skin, insulin, bmi, dpf, age]])
        scaled = scaler.transform(data)
        pred = model.predict(scaled)[0]
        prob = model.predict_proba(scaled)[0][1]
        st.write("---")
        if pred == 1:
            st.error(f"Hasil: Positif Diabetes (Probabilitas: {prob:.2f})")
        else:
            st.success(f"Hasil: Negatif Diabetes (Probabilitas: {prob:.2f})")

with tab2:
    st.subheader("📄 Upload CSV")

    file = st.file_uploader("Unggah file CSV", type=["csv"])
    if file:
        df = pd.read_csv(file)
        st.write("📋 Data Awal:", df.head())

        try:
            scaled = scaler.transform(df)
            predictions = model.predict(scaled)
            df['Prediksi'] = predictions
            df['Probabilitas Diabetes'] = model.predict_proba(scaled)[:,1]
            st.success("✅ Prediksi selesai!")
            st.write(df)

            # Grafik ringkasan
            st.subheader("📊 Distribusi Hasil Prediksi")
            fig1, ax1 = plt.subplots()
            df['Prediksi'].value_counts().plot.pie(autopct="%1.1f%%", labels=["Negatif", "Positif"], colors=["green", "red"], ax=ax1)
            ax1.set_ylabel("")
            st.pyplot(fig1)

            # Download hasil
            csv_download = df.to_csv(index=False).encode('utf-8')
            st.download_button("⬇️ Download Hasil", csv_download, "hasil_prediksi.csv", "text/csv")
        except Exception as e:
            st.error(f"Terjadi kesalahan: {e}")
