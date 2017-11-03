def get_formatted_name(first_name,last_name,middle_name=""):
    """Return a full name , neatly formatted."""
    # Make sure the middle name is the last argument
    # entered when function is called.
    if middle_name:
        full_name = first_name + ' '  + middle_name + ' ' + last_name
        return full_name.title()
    else:
        full_name = first_name + ' ' + last_name
        return full_name.title()

while True: # Infinite loop
    print("Please tell me your name.")
    f_n = raw_input("First Name: \nEnter 'quit' to quit program. ")
    if f_n != 'quit':
        l_n = raw_input("Last Name: \nEnter 'quit' to quit program. ")
        if l_n != 'quit':
            question = raw_input('Do you have a middle name?(yes/no) ')
            if question == 'yes':
                m_n = raw_input("Middle name: \nEnter 'quit' to quit program. ")
                if m_n != 'quit':
                    formatted_name = get_formatted_name(f_n,l_n,m_n)
                    print("\nHello " + formatted_name + "!")
                else:
                    break
            elif question == 'no':
                formatted_name = get_formatted_name(f_n,l_n)
                print("\nHello " + formatted_name + "!")
        else:
            break
    else:
        break


