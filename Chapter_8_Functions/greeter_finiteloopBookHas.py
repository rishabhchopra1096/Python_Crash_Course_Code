def get_formatted_name(first_name,last_name):
    full_name=first_name+' '+last_name
    return full_name.title()
while True:
    print("\nPlease tell me your name:")
    print("enter 'quit' at any time to end program.")
    f_name=input("First name: ")
    if f_name=='quit':
        break
    l_name=input("Last name: ")
    if l_name=='quit':
        break
    formatted_name=get_formatted_name(f_name,l_name)
    print ("Hello, "+formatted_name+"!")

