import streamlit as st
import pandas as pd
import plotly.express as px

# bazowałem na winequality.csv

st.set_page_config(layout = "wide")

st.header("PAD -> Streamlit")

firstPage = 'Ankieta'
secondPage = 'Stats'

page = st.sidebar.selectbox('Select page',[firstPage,secondPage]) 

if page == firstPage:
    
    with st.form(key='form'):
        firstName = st.text_input("First Name","", placeholder ="Type in your first name")
        name = st.text_input("Name","", placeholder ="Type in your name")
        submit_button = st.form_submit_button(label='Submit',type="primary")
    
    if submit_button:
        if not firstName or not name:
            st.write(f"{firstName} {name}")
            st.error("Form is not valid")
        else:
            st.success("Form has been successfully saved")

else:
    ## secondPage
	
    st.write(secondPage)

    ## uploading data
    data = st.file_uploader("Upload your dataset", type=['csv'])
    if data is not None:
        with st.spinner('Wait for it...'):
            df = pd.read_csv(data)
            st.dataframe(df)
        st.success('Done!')
        
        wineColorlist = df['target'].unique()
        wineColor = st.selectbox("Select a target wine color:",wineColorlist)
        
        col1,col2 = st.columns(2)

        fig = px.scatter(df[df['target'] == wineColor],
        x = "quality", y = "fixed acidity",
        trendline='ols')
        col1.plotly_chart(fig)
        
        fig = px.scatter(df[df['target'] == wineColor],
        x = "quality", y = "residual sugar",
        trendline='ols')
        col2.plotly_chart(fig)