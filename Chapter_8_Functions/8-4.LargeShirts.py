def make_shirt(size,printed_text):
    print("So let me confirm this, You want a:\n\t"+size+" size T-shirt with\n\t"+printed_text+" written on it.")
#postional argument :
make_shirt('L','"Sorry Ladies, I am in the Nights Watch"')
#keyword argument
quote="Sorry Ladies, I'm in the Night's Watch"
make_shirt(size='Snow',printed_text='"'+quote+'"')
#Notice how keyword's value in a list can not only be another variable but also can be operated on to make it
# a sum of strings.

def make_shirt(size='Large',printed_text='"'+'I love Python'+'"'):
        print("So let me confirm this, You want a:\n\t"+size+" size T-shirt with\n\t"+printed_text+" written on it.")

#Large shirt and Medium shirt with default message:
make_shirt() #No input required for large.
make_shirt('Medium') #Only size input , first parameter required according to positional arguments.
#Shirt of any size(small) with a diffferent message:
make_shirt('Small','"'+'I know HTML: HowToMeetLadies'+'"')

