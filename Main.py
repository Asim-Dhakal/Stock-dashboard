import streamlit as st 
import pandas as pd
import numpy as np 
import plotly.express as px 
import warnings 
warnings.filterwarnings('ignore')

def Main_page():
    st.set_page_config(
        page_title='Home', 
        page_icon=':bar_chart:', 
        layout='centered'
    )

    st.title('Main page')
    #st.button('Profile Manager', key=None, help=None, on_click=profile(),type='primary')
    #st.button('Portfolio Manager', key=None, help=None, on_click=p,type='primary')

Main_page()