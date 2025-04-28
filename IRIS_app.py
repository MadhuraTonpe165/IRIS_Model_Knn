{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ed3932f6-70d5-44ff-8b91-c32b8f5808c6",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import numpy as np\n",
    "import pickle\n",
    "\n",
    "# Load the model\n",
    "with open('IRIS_KNN_Model.pkl', 'rb') as f:\n",
    "    model = pickle.load(f)\n",
    "\n",
    "# Streamlit UI\n",
    "st.title(\"Predict IRIS Flower Species\")\n",
    "st.write(\"🔍 This app uses a K-NN to predict type of flower.\")\n",
    "\n",
    "# Collect user input\n",
    "SepalLengthCm = st.number_input(\"SepalLengthCm (in cm)\", min_value=0.0, value=5.8)\n",
    "SepalWidthCm = st.number_input(\"SepalWidthCm (in cm)\", min_value=0.0, value=3.0)\n",
    "PetalLengthCm = st.number_input(\"PetalLengthCm (in cm)\", min_value=0.0, value=3.75)\n",
    "PetalWidthCm = st.number_input(\"PetalWidthCm (in cm)\", min_value=0.0, value=1.2)\n",
    "\n",
    "# Button to predict\n",
    "if st.button(\"Predict IRIS Flower Species\"):\n",
    "    input_data = np.array([[\n",
    "        SepalLengthCm,\n",
    "        SepalWidthCm,\n",
    "        PetalLengthCm,\n",
    "        PetalWidthCm        \n",
    "    ]])\n",
    "\n",
    "    # Prediction\n",
    "    prediction = model.predict(input_data)[0]\n",
    "\n",
    "    if prediction == 0:\n",
    "        st.success(\"Iris-setosa !!!\")\n",
    "    elif prediction == 1:\n",
    "        st.success(\"Iris-versicolor !!!\")\n",
    "    elif prediction == 2:\n",
    "        st.success(\"Iris-virginica !!!\")\n",
    "    else:\n",
    "        st.error(\"No Match !!!\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
