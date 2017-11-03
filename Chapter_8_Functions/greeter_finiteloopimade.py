# I made it finite by adding an if statement and a flag.
active=True
while active:
    intro=input("\nTo tell me your name, enter anything in quotes or\nIf you want to end the program, enter 'quit'.")
    if intro!='quit':
        f_name=input("First name(in quotes):")
        l_name=input("Last name(in quotes): ")
        formatted_name=get_formatted_name(f_name,l_name)
        print("\nHello, "+formatted_name+"!")
    else:
        active=False