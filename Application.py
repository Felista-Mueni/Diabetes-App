import pickle
import numpy as np
import streamlit as st

# Load the trained model
loaded_model = pickle.load(open("trained_model.sav", 'rb'))

# Function to predict if the person is diabetic or not
def diabetic_prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = loaded_model.predict(input_data_reshaped)

    if prediction[0] == 0:
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'

# Streamlit UI setup
def main():
    st.title('Diabetes Prediction Web App')

    # User inputs for prediction
    Pregnancies = st.text_input('Number of Pregnancies', key='pregnancies')
    Glucose = st.text_input('Glucose Level', key='glucose')
    BloodPressure = st.text_input('Blood Pressure Value', key='blood_pressure')
    SkinThickness = st.text_input('Skin Thickness Value', key='skin_thickness')
    Insulin = st.text_input('Insulin Level', key='insulin')
    BMI = st.text_input('BMI Value', key='bmi')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function', key='diabetes_pedigree')
    Age = st.text_input('Age', key='age')

    diagnosis = ''

    if st.button('Diabetes Test Result'):
        diagnosis = diabetic_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])

    st.success(diagnosis)

if __name__ == '__main__':
    main()


