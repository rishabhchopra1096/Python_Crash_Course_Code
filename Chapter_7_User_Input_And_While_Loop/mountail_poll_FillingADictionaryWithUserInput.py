# You can prompt for as much input as you need in each pass
# through a while loop.
#Lets make a polling program in which each pass through the loop
#prompts for the participants name and response.
 # Well store the data we gather in a dictionary, because we want to
 # connect each response with a particular user:
#print ("THIS IS WHAT I DID:")
# responses={}
# prompt="What is your name? "
# prompt2="\nWhich mountain would you like to climb someday? "
# prompt+="\nEnter 'quit' to end program."
# prompt2+="\nEnter 'quit' to end program."
# name=''
# mountain=''

# while name!='quit':
#     name=input(prompt)
#     if name!='quit':
#         mountain=input(prompt2)
#     elif name=='quit':
#         break
#     elif mountain!='quit':
#         responses[name] = mountain
#         print (responses)
#         print (name)
#         print (mountain)
#     elif mountain =='quit':
#         break

#print ("this is how the book does it:")
responses={}

#setting a flag too indicate polling is active.
polling_active=True

while polling_active:
    #prompt for person's name and response.
    name=input("\nWhat is your name? ")
    response=input("Which mountain would you like to climb someday? ")
    #Storing the response in the dictionary.
    responses[name.title()]=response.title()
    #Find out if anyone else is going to take the poll.
    repeat=input("Would you like to let another person respond?(yes/no) ")
    if repeat=='no':
        polling_active=False
    else:
        polling_active=True #This line is not included but i added it for clarity.

print("\nPolling Results:")
for name, response in responses.items():
    print(name.title()+" would like to climb "+response.title()+".")
print (responses)


# Ok, so the problem between my method and their method is that
# I was not aware that questions will automatically come one by one if i keep them in different
# variables representing different inputs.







