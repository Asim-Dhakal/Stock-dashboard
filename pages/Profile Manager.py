import streamlit as st
import pandas as pd
import json as js
from Config_functions import Config_Of_page

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

_ ='''
This funtion displays all the profiles that we have made using Makeprofile.
It then displays all the profiles as button and if you press it it deletes the profile. 
'''
def display_Profile(Profile_list):
    reg_profile_name = st.form('These are the Profiles you have created: ')
    st.write('These are the Profiles you have created: ')
    # start value for the loop 
    i=0
    # This is columns to make the buttons next to each other
    profile_slot_1, profile_slot_2 = st.columns([1,1])

    #Goes thru all the profiles and displays them. 
    for i in range (0,len(Profile_list),2):
        # these are the two buttons in these columns. They both have a unique key which is vlaue of array + array 
        with profile_slot_1:
            first_button = st.button(Profile_list[i], key=f"{Profile_list[i]}_{i}",on_click=None, use_container_width= True )
            # when the button is pressed the profile is removed and new profile without dumped is added to json file 
            if first_button:
                st.success(f'You have removed profile {Profile_list[i]}' )
                Profile_list.pop(i)
                json_dump(Profile_list)
                st.rerun()

        with profile_slot_2:
            if i+1 < len(Profile_list):
                second_button = st.button(Profile_list[i+1], key=f"{Profile_list[i+1]}_{i+1}", on_click=None, use_container_width=True)
                if second_button:
                    st.success(f'You have removed profile {Profile_list[i+1]}' )
                    Profile_list.pop(i+1)
                    json_dump(Profile_list)
                    st.rerun()

def Max_Profiles():
    st.write('YOU HAVE REACHED THE MAX AMOUNT OF PROFILES PLEASE DELETE SOME TO MAKE MORE SPACE')


def Main():
    Config_Of_page('Profile',':bust_in_silhouette:','centered','All Of Your Profiles')
    Profile_list = json_load()
    if len(Profile_list) < 20:
        Profile_name = Makeprofile(remove_whitespace(Profile_list))
        if Profile_name != None:
            Profile_list.append(Profile_name)
        json_dump(Profile_list)
    else: 
        Max_Profiles()
    display_Profile(remove_whitespace(Profile_list))

Main()

