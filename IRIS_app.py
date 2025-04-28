import streamlit as st
import numpy as np
import pickle

# Load the model
with open('IRIS_KNN_Model.pkl', 'rb') as f:
    model = pickle.load(f)

# Streamlit UI
st.title("Predict IRIS Flower Species")
st.write("🔍 This app uses a K-NN model to predict the type of flower.")

# Collect user input
SepalLengthCm = st.number_input("Sepal Length (cm)", min_value=0.0, value=5.8)
SepalWidthCm = st.number_input("Sepal Width (cm)", min_value=0.0, value=3.0)
PetalLengthCm = st.number_input("Petal Length (cm)", min_value=0.0, value=3.75)
PetalWidthCm = st.number_input("Petal Width (cm)", min_value=0.0, value=1.2)

# Button to predict
if st.button("Predict IRIS Flower Species"):
    input_data = np.array([[SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm]])
    
    # Prediction
    prediction = model.predict(input_data)[0]

    if prediction == 0:
        st.success("🌸 Iris-setosa !!!")
    elif prediction == 1:
        st.success("🌼 Iris-versicolor !!!")
    elif prediction == 2:
        st.success("🌺 Iris-virginica !!!")
    else:
        st.error("❗ No Match Found !!!")
