import json as js


# Gets list from json file thats under the key 'Profiles' in the dict 
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

# Writes to the json file and stores all our profile 

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
def json_manager():

    all_profiles= json_load()
    saved_profiles = json_load('Profile_with_stocks.json',None)
    
    keys_to_remove = [key for key in saved_profiles if key not in all_profiles]
    for key in keys_to_remove:
        saved_profiles.pop(key for key in keys_to_remove)    
    for profile in all_profiles:
        if profile not in saved_profiles:
            saved_profiles[profile] = {}
    json_dump(None,None,'Profile_with_stocks.json',saved_profiles)
    
    return saved_profiles

def stocks():
    print()



json_manager()