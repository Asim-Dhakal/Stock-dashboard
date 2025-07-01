import streamlit as st 
from Config_functions import Config_Of_page
from funtions import json_dump, json_load, json_manager,Top_50

if __name__ == "__main__":
    # Initialize session state variable
    if 'submitted' not in st.session_state:
        st.session_state.submitted = False

def main():
    Config_Of_page('Stock allocation',':bank:','centered','Allocate stocks')
    show_stocks()

_ ='''
This displays all the profile 
then it lets user select the stock 
then it lets use add ticker and also amount of share 
then it will write it to the json file : ) 

'''
def show_stocks():
    profile_list = json_load()
    st.write('These are the Profiles you have created:')

    profile_slot_1, profile_slot_2 = st.columns([1, 1])

    # Track selected profile
    if "selected_profile" not in st.session_state:
        st.session_state.selected_profile = None

    for i in range(0, len(profile_list), 2):
        with profile_slot_1:
            if st.button(profile_list[i], key=f"profile_{i}",use_container_width=True):
                st.session_state.selected_profile = profile_list[i]

        if i + 1 < len(profile_list):
            with profile_slot_2:
                if st.button(profile_list[i+1], key=f"profile_{i+1}",use_container_width=True):
                    st.session_state.selected_profile = profile_list[i+1]
    # Show form if a profile is selected
    if st.session_state.selected_profile:
        Temp_pop_up = placeholder = st.empty()
        with Temp_pop_up.form("Add Stock Form"):
            ticker = st.selectbox(f'Select which stock you want to add to profile {st.session_state.selected_profile} ', Top_50())
            stock = st.number_input('How many stocks do you want to add? (Value over 100000000 will be 0)', 0, 100000000)
            submitted = st.form_submit_button('Add stock')
            if submitted:
                json_manager(ticker,st.session_state.selected_profile, stock)
                Temp_pop_up.empty()
main()


