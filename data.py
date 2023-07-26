import streamlit as st
import pandas as pd
import numpy as np
import time

a= [1,2,3,4,5,6,7,8]
m=np.array(a)
md=m.reshape((2,4))

dic ={
    "name":"dan",
    "age":25,
    "city":"Kigali"
}
st.dataframe(dic)
st.table(dic)
st.json(dic)
st.write(dic)
@st.cache
def ret_time(t):
    time.sleep(5)
    return time.time()
if st.checkbox("1"):
    st.write(ret_time(2))
if st.checkbox("2"):
    st.write(ret_time(1))
