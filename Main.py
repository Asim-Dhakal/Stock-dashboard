import streamlit as st 
import pandas as pd
import numpy as np 
import plotly.express as px 
import warnings 
from Config_functions import Config_Of_page
warnings.filterwarnings('ignore')

def Main_page():
    Config_Of_page('Home',':bar_chart:','centered','Main page')
Main_page()