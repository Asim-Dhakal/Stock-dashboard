import json as js
import pandas as pd
import streamlit as st
''' 
So this fine gets all the profiles by defult 
It opens the profile manager file and then within the dict in it gets the values in the profiles key 
if the key is set to none then it doesnt get the profiles by defult instead it loads up the filename you get everything in a file as a dict 
'''
def json_load(filename ='Profile manager.json', key='Profiles' ):
    with open(filename, 'r') as file:
        if key == 'Profiles':
            Profile_list = js.load(file)
            Profiles = Profile_list[key]
            List_to_return = remove_whitespace(Profiles)
        else: 
            List_to_return = js.load(file)
        return List_to_return
    
# Removes all '' values from the list to return only valid profile names
def remove_whitespace(List_to_return):
    cleaned_list = [item for item in List_to_return if (item != '') or (item == None)]
    return cleaned_list
'''
Writes to the json file and stores all our profile. The what we are saving is profiles then profile ma nager is the 
file and it gets saved as profile as a key and then the list as the value 
'''
def json_dump(Profile_list = 0, defult_profile = 'Profiles',file_name = 'Profile manager.json',finished_dict = {}):
    with open(file_name, 'w') as file:
        if defult_profile == 'Profiles':
            js.dump({defult_profile : Profile_list}, file)
        else:
            js.dump(finished_dict,file)


''' This gets all the profiles and makes sure all of them are in our profile with stock list. 
    First it loads the amount of profiles we have 
    Then it runs the saved profiles 
    if the profile is not in the saved stock profiles we have it removes it
    if the profile is in the saved stock profiles then it does nothing 
    if its not in it then it makes it a key and then gives it a dict value where we will have {'ticker' : amount of stock }

'''
def json_manager(Ticker = None,Profile_name = None, share = 0):

    all_profiles= json_load()
    saved_profiles = json_load('Profile_with_stocks.json',None)
    
    keys_to_remove = [key for key in saved_profiles if key not in all_profiles]
    for key in keys_to_remove:
        saved_profiles.pop(key)   
    for profile in all_profiles:
        if profile not in saved_profiles:
            saved_profiles[profile] = {}
    json_dump(None,None,'Profile_with_stocks.json',saved_profiles)
    if Profile_name != None:
        saved_profiles[Profile_name].update({Ticker:share})
        json_dump(None,None,'Profile_with_stocks.json',saved_profiles)     
    saved_profiles = json_load('Profile_with_stocks.json',None)
    
    return saved_profiles

'''
Has the top 50 trickers on USA companies 

'''
def Top_50():
    top_50_tech_tickers = [
    "AAPL", "MSFT", "NVDA", "AVGO", "GOOGL", "GOOG", "AMZN", "META", "TSLA", "ADBE",
    "AMD", "ORCL", "CRM", "CSCO", "INTC", "QCOM", "TXN", "AMAT", "ADI", "TEAM",
    "ADSK", "NOW", "PLTR", "ZS", "FTNT", "SHOP", "NFLX", "SNPS", "CDNS", "CDW",
    "ARM", "ASML", "MU", "LRCX", "SNOW", "ZM", "INTU", "ANSS", "ANET", "CTXS",
    "DXCM", "EA", "MCHP", "STX", "COUP", "EVBG", "MDB", "DOCU"
    ]
    return top_50_tech_tickers

