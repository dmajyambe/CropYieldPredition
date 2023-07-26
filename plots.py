import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt



data=pd.DataFrame(np.random.randn(100,3),
                  columns=['a','b','c'])
#plt.scatter(data['a'],data['b'])
chart=alt.Chart(data).mark_circle().encode(x='a',y='b',tooltip=['a','b'])
# st.graphviz_chart() #flowchart 
# st.plotly_chart()# plot plotly chart
#st.altair_chart(chart)
data = {
    'city': ['kigali'],
    'lat': [1.9441],
    'lon': [30.0619]
}

city = pd.DataFrame(data)
st.map(city)
#fig, ax = plt.subplots()
#ax.scatter(data['a'],data['b'])
#st.table(city)
#st.line_chart(data)
# st.area_chart(data)
# st.bar_chart(data)

