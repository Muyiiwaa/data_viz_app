import streamlit as st
import pandas as pd
import plotly.express as px
from chart_insight import chart_dict,test_dict
from chart_insight import generate_plotly_chart
from hero import hero_section, feedback
from  scipy import stats
from stat_test import display_test


# Function to load CSV file
def load_data(file):
    df = pd.read_csv(file)
    df.columns = df.columns.str.replace(' ', '_')
    return df

# Function to select columns
def select_columns(df):
    #columns = st.multiselect('Select Columns', df.columns)
    x = st.multiselect('Choose X column(s)', df.columns)
    y = st.multiselect('Select Y column', df.columns)
    x.extend(y)
    columns = x
    return columns

# Function to display DataFrame
def display_dataframe(df):
    st.write("### DataFrame")
    st.dataframe(df)
    
def display_charts2(df, cols, chart):
    fig = generate_plotly_chart(chart_type=chart, data=df, cols= cols)
    st.plotly_chart(fig)
    st.divider()
# Function to display charts
def display_charts(df, columns):
    for col in columns:
        fig = px.histogram(df, x=col, title=f'{col} Distribution')
        st.plotly_chart(fig)

# Main function
def main():
    #st.title('THE SIMPLE ANALYST')
    hero_section()
    # Upload CSV file
    uploaded_file = st.sidebar.file_uploader("Upload CSV file", type=['csv'])
    st.sidebar.divider()
    if uploaded_file is not None:
        # Load CSV file
        df = load_data(uploaded_file)

        # Select columns
        selected_columns = select_columns(df)
        # Display DataFrame
        show_data = st.sidebar.toggle(label='show dataset')
        if show_data:
            display_dataframe(df)
        # select chart types.
        show_charts = st.sidebar.toggle(label='show charts')
        if show_charts:
            chart_type = st.sidebar.radio(label='Choose the chart type:',
                                      options= list(chart_dict.keys()))
            if chart_type:
                st.success(f'''{chart_type} chart {chart_dict[chart_type].lower()}''')
                if st.button(label=f"Show {chart_type}", type= 'primary'):
                    if selected_columns:
                        # Display charts
                        #display_charts(df, selected_columns)
                        display_charts2(df, cols = selected_columns,chart=chart_type)
        show_tests = st.sidebar.toggle(label='show tests')
        if show_tests:
            test_type = st.sidebar.radio(label='Choose the test type:',
                                      options= list(test_dict.keys()))
            st.success(f'''{test_type} analysis {test_dict[test_type].lower()}''')
            if st.button(label=f"Perform {test_type} analysis", type= 'primary'):
                if select_columns:
                    display_test(df, columns=selected_columns, test=test_type)
                    #st.text_input(label='What does this mean?')
                    if st.button(label='Clear Result', key='clear_btn'):
                        pass
        st.sidebar.divider()
        feedback()
        

if __name__ == "__main__":
    main()
