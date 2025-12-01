
import streamlit as st
import joblib 
import numpy as np

model = None
model_load_error = None
try:
    model = joblib.load('model.pkl')
except Exception as e:
    model_load_error = str(e)

st.title('House Price Prediction App')

st.divider()

st.write("This app uses machine learning for predicting house prices with given features of the house. For using this app you can enter the inputs from this UI and then use predict button.")

st.divider()

bedrooms = st.number_input('Number of Bedrooms', min_value=0, value=0)
bathrooms = st.number_input('Number of Bathrooms', min_value=0, value=0)
living_area = st.number_input('Living Area', min_value=0, value=2000)
condition = st.number_input('Condition', min_value=1, value=3)
number_of_schools = st.number_input('Number of Schools Nearby', min_value=0, value=0)

st.divider()


x = [[bedrooms, bathrooms, living_area, condition, number_of_schools]]


predictbutton = st.button("Predict!")

if predictbutton:
    if model is None:
        st.error("Model file `model.pkl` is missing or couldn't be loaded.")
        if model_load_error:
            st.write(f"Load error: {model_load_error}")
    else:
        with st.spinner("Predicting..."):
            x_array = np.array(x)
            try:
                prediction = model.predict(x_array)
            except Exception as e:
                st.error(f"Prediction failed: {e}")
            else:
                try:
                    pred_val = float(prediction[0]) if hasattr(prediction, '__len__') else float(prediction)
                    st.success(f"The predicted price of the house is: {pred_val}")
                except Exception:
                    st.success(f"The predicted price of the house is: {prediction}")

else:
    st.write("Please use predict button after entering values.")
    










# order of x ['number of bedrooms', 'number of bathrooms', 'living area',
       #'condition of the house', 'Number of schools nearby']