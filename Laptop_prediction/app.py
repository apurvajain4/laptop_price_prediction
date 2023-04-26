import streamlit as st
import os
from PIL import Image


st.title("Laptop Prediction :rainbow:")

image = Image.open('a.jpg')

st.header("EM Laptops")
st.text('Want to predict price of laptop?')


st.subheader("Let's Connect:-")
st.text("LinkedIn:- ")
if st.button(' Click Here to Connect with me:point_down:'):
    st.write('https://www.linkedin.com/in/apurva-jain04')
    st.success('Get connected!', icon="✅")

st.text("GitHub:- ")
if st.button(' Click Here to Connect::point_down:'):
    st.write('https://github.com/apurvajain4')
    st.success('Visit!', icon="✅")
