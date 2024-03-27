# importing the libraries 


import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

# set up file upload

"""
# DATAVIZ APP
"""

st.sidebar.title("DATAVIZ")
st.sidebar.divider()
uploaded_data = st.sidebar.file_uploader(label='Upload dataset')
x = st.text_input(label="X VARIABLE")
y = st.text_input(label= "Y VARIABLE")



def main(data, col):
    
    fig = px.histogram(data_frame= data, 
                    x =  data[col[0]],y= data[col[1]] )
    show = st.plotly_chart(fig, use_container_width=True)
    
    return show


if st.sidebar.button(label= 'Upload', type= 'primary'):
    data = pd.read_csv(uploaded_data)
    uploaded_cols = list(data.columns)
    st.write(f'You have columns {list(data.columns)}')
    main(data= data, col=[x,y])
    