import streamlit as st
import numpy as np
import joblib
import warnings
warnings.filterwarnings('ignore')

#Uploading the model
model =joblib.load("Random_Search (3).pkl")

#Uploading the pickle file
st.title("House Price Prediction")
st.markdown("---")

bedroom = st.number_input("Enter the number of bedroom",min_value=0,value=0)
bathroom = st.number_input("Enter the number of bathroom",min_value=0,value=0)

living_area=st.number_input("Living area",min_value=0,value=2000)
condition_of_house=st.number_input("Condition of house",min_value=1 , value=1)
school=st.number_input("Number of School",min_value=0,value=0)
x=[[bedroom,bathroom,living_area,condition_of_house,school]]

pred = st.button("Predict")

if pred ==True:
    arr=np.array(x)
    price =int(model.predict(arr)[0])
    st.write(f"The Price of the house is {price}")
else:
     st.write("Please click on the button")


