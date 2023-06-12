import pickle
import streamlit as st

# membaca model
heart_model = pickle.load(open('heart_model.sav', 'rb'))

#judul web
st.title('Prediksi Serangan Jantung')

#membagi kolom
col1, col2 = st.columns(2)

with col1 :
    sex = st.number_input('Jenis Kelamin pasien (F = 0 & M = 1)')
    age = st.number_input('Umur pasien')
    cp = st.number_input('Jenis nyeri dada ~ 0 = Angina Khas, 1 = Angina Atipikal, 2 = Nyeri Non-angina, 3 = Tanpa gejala')
    trtbps = st.number_input('tekanan darah istirahat (dalam mmHg)')
    chol = st.number_input('kolestrol dalam mg/dl yang diambil melalui sensor BMI')
    fbs = st.number_input('gula darah puasa > 120 mg/dl (1 = benar; 0 = salah)')

with col2 :
    restecg = st.number_input('Hasil elektrokardiografi istirahat ~ 0 = Normal, 1 = Normalitas gelombang ST-T, 2 = Hipertrofi ventrikel kiri')
    thalachh = st.number_input('Denyut jantung maksimum yang dicapai')
    exng = st.number_input('angina yang diinduksi oleh olahraga (1 = ya; 0 = tidak)')
    caa = st.number_input('jumlah pembuluh darah utama (0-3)')
    thall = st.number_input('Hasil Tes Stres Thalium ~ (0,3)')

heart_diagnosis = ''

# membuat tombol untuk prediksi
if st.button('Diagnosis'):
    heart_prediction = heart_model.predict([[age, sex, cp, trtbps, chol, fbs, restecg, thalachh,
                                                   exng, caa, thall]])

    if heart_prediction[0] == 0:
        heart_diagnosis = 'kemungkinan serangan jantung lebih kecil'
    else:
        heart_diagnosis = 'kemungkinan serangan jantung lebih besar'
    st.success(heart_diagnosis)
