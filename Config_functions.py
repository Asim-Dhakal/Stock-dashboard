import streamlit as st

'''
This is the page configirator it makes the page in streamlit 
Then it calls it later on when needed in different pahes 
configs the pages. 

'''
def Config_Of_page(config_title,config_icon,config_layout,title):
    st.set_page_config(
        page_title= config_title, 
        page_icon= config_icon, 
        layout= config_layout
        # This is the head to the page 
    )
    st.title(title)

# page_title='Profile'
# page_icon=':bust_in_silhouette:'
# layout='centered'