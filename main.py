# importing the libraries 


import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
import time

options= ['bar-chart','line chart', 'scatter chart']
# set up file upload

"""
# VIZZ-APP
### Learn a lot and quickly form your dataset with just one click. Making data visualisation fun again
"""
st.sidebar.title("VIZZ-APP")


uploaded_data = st.sidebar.file_uploader(label="xyz", label_visibility='hidden')
try:
    if st.sidebar.button(label='Upload', type= 'secondary'):
        with st.spinner("uploading loading file.."):
            time.sleep(3)
        st.sidebar.success(body="Done!")
except ValueError:
    st.write("You Must upload a dataset")    


if st.button(label= 'Try it Out', type='primary'):
    st.divider()
    st.sidebar.divider()
    st.sidebar.title("Now Choose your charts")

df = pd.read_csv(uploaded_data)
st.write(df.head(5))

chart = st.sidebar.radio(label= "Charts",
                         options= ['bar_chart','line chart','scatter chart'],
                         index=None)

if chart:
    st.success(f"You chose {chart}")
    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        x = st.text_input(label= "X")
    with col2:
        y = st.text_input(label= "Y")
    if chart == 'bar_chart':
        fig = px.histogram(data_frame=df, x = df[x], y = df[y],
                           color= df[x],
                           title= f"Bar Chart of {x} and {y}")
        st.plotly_chart(fig)  
else:
    st.error(f'Choose a Chart')
