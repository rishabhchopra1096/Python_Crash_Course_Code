#The function build_profile() takes in the the first and the last
#name, BUT it accepts an arbitrary number of keyword
#arguments as well.
#As above discussed , we will first write the positional #parameters ,
# then keyword arguments if any, then aribatary parameter.

def build_profile(first,last,**user_info):
    """Build a dictionary to contain everything we know about a user"""
    profile={}
    profile['First name']=first
    profile['Last name']=last
    for key, value in user_info.items():
        profile[key]=value
    return profile
user_profile=build_profile('albert','einstein',location='princeton',field='physics')
print (user_profile)



