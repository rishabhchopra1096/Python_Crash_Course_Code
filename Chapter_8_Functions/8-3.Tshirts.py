def make_shirt(size,printed_text):
    print("So let me confirm this, You want a:\n\t"+size+" size T-shirt with\n\t"+printed_text+" written on it.")
#postional argument :
make_shirt('L','"Sorry Ladies, I am in the Nights Watch"')
#keyword argument
quote="Sorry Ladies, I'm in the Night's Watch"
make_shirt(size='Snow',printed_text='"'+quote+'"')
#Notice how keyword's value in a list can not only be another variable but also can be operated on to make it
# a sum of strings.
