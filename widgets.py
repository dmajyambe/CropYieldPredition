import streamlit as st
import pandas as pd
import numpy as np

st.title("WIDGETS")
if st.button("Subscribe"):
    st.write("Thanks for subscribing")
name= st.text_input("Name")
st.write(name)
address=st.text_area("Enter your address")
st.write(address)
st.date_input("Enter date")
st.time_input("Enter the time input")
if st.checkbox("You accept TC",value=False):
    st.write("Thank you")
st.selectbox("Colors",['r','g','b'],index=0)
st.multiselect("Colors",['r','g','r'])
st.slider("age",min_value=10,max_value=100,step=4)
st.number_input("numbers")