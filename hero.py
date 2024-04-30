import streamlit as st

def hero_section():
    #st.title('SIMPLE INTERFACE FOR YOUR QUICK ANALYTICS NEEDS')
    st.set_page_config(
    page_title="SMART ANALYTICS BUDDY!",
    page_icon=":brain:",  # Favicon emoji
    layout="centered",)  # Page layout option
    
    st.title("🤖 WELCOME TO VIZAPP.")
    st.markdown('### YOUR QUICK DATA ANALYTICS AND VISUALISATON BUDDY')
    st.divider()
    #st.button(label='Get Started', type= 'primary')
    column1, column2 = st.columns(2)
    with column1:
        container1 = st.container(border=True, height=230)
        container1.subheader('Quick Data Viz', divider=True)
        container1.markdown(body= "Generate quick chart and unlock diverse information from your dataset")
        get_visual = container1.button(label= 'Get Visuals', type='secondary', key='viz')
    with column2:
        container2 = st.container(border=True, height=230)
        container2.subheader('Statistical Test', divider=True)
        container2.markdown(body= "Run quick statistical test, unlock diverse insight from your data")
        get_test = container2.button(label= 'Check it out', type='secondary')
   
    if get_test:
        st.success('Upload dataset to get started. Are you On Mobile? Open side panel')
    elif get_visual:
        st.success('Upload dataset to get started.Are you On Mobile? Open side panel')
    st.divider()

def feedback():
    comment = st.sidebar.text_area(label='Feedback', label_visibility= 'visible')
    if st.sidebar.button(label='Send', type='primary'):
        if comment == '':
            st.sidebar.error('Please add a feedback or ignore')
        else:
            st.sidebar.success('Feedback recieved!')
        
        