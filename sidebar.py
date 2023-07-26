import streamlit as st
import pandas as pd
import time
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')
data={
    'num':[x for x in range(1,11)],
    "square":[x**2 for x in range(1,11)],
    "twice":[x*2 for x in range(1,11)],
    "thrice": [x*3 for x in range(1,11)]

}
rad=st.sidebar.radio('Navigation',['Home',"About us"])
if rad=="Home":

    df=pd.DataFrame(data=data)
    fig, ax = plt.subplots()
    st.sidebar.selectbox("Select a number",[1,2,3,4,5])
    col=st.sidebar.multiselect("Select a column",df.columns)
    ax.plot(df['num'],df[col])
    st.pyplot(fig)
if rad=='About us':
    progress= st.progress(0)
    for i in range(100):
        time.sleep(0.1)
        progress.progress(i+1)
    st.balloons()
    st.write('You are on about us page')
    
    st.error('Error')
    st.success("Show success")
    st.info("Information")
    st.exception(RuntimeError("This is an error"))
