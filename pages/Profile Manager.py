import streamlit as st
import pandas as pd
import json as js

# Gets list from json file thats under the key 'Profiles' in the dict 
def json_load():
    with open('Profile manager.json', 'r') as file:
        Profile_list = js.load(file)
        Profiles = Profile_list['Profiles']
        List_to_return = remove_whitespace(Profiles)
        return List_to_return

# Removes all '' values from the list to return only valid profile names 
def remove_whitespace(List_to_return):
    cleaned_list = [item for item in List_to_return if (item != '') or (item == None)]
    return cleaned_list

# Writes to the json file and stores all our profile 
def json_dump(Profile_list):
    with open('Profile manager.json', 'w') as file:
        js.dump({'Profiles' : Profile_list}, file)

# This configs out Porfile managter page. It does the heading, the icon and layout 
def Config_Of_pagge():
    st.set_page_config(
        page_title='Profile', 
        page_icon=':bust_in_silhouette:', 
        layout='centered'
    )
    # This is the head to the page 
    st.title('All Of Your Profiles')

#This sets to true making buttons or inputs disable. 
def disable():
    st.session_state.disabled = True
        
# This is the funtion that loads up the profile maker 
def Makeprofile(list_names):
    if "disabled" not in st.session_state:
        st.session_state.disabled = False
    #This asks for name of the profile 
    reg_profile_name = st.form('Profile creator')
    profile_name = reg_profile_name.text_input(
    'Profile Name: ',
    max_chars= 30,
    key=None
                                               ) #The input bubble 
    submit_button = reg_profile_name.form_submit_button('Make Profile') # The submit button 
    
    # This is whats printed if its submited 
    if submit_button:
        if profile_name.strip() == "":
            st.warning("Profile name cannot be empty.")
            st.session_state.disabled = False
        elif profile_name in list_names:
            st.error("This profile name already exists. Please enter another name.")
            st.session_state.disabled = False
        else: 
            st.success(f'You have created a profile called {profile_name}' )
            return profile_name
    return None

# Displays all the different profiles   
def display_Profile(Profile_list):
    reg_profile_name = st.form('These are the Profiles you have created: ')
    st.write('These are the Profiles you have created: ')

    profile_slot_1, profile_slot_2 = st.columns([1,1])
    list_of_profile = len(Profile_list)
    for i in range(0,list_of_profile,2):
        with profile_slot_1:
            st.button(Profile_list[i], key=[i])
        with profile_slot_2:
            if i+1 < list_of_profile:
                st.button(Profile_list[i+1], key=[i+1])
  
def Main():
    Config_Of_pagge()
    Profile_list = json_load()
    if len(Profile_list) < 20:
        Profile_name = Makeprofile(remove_whitespace(Profile_list))
        if Profile_name != None:
            Profile_list.append(Profile_name)
        json_dump(Profile_list)
    display_Profile(remove_whitespace(Profile_list))

Main()

