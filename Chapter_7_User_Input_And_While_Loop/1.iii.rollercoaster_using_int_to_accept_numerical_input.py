#print "Using int() to accept numerical input"
# when you use the input function , python interprets everything the
# user enters as a string.

#age=input("How old are you? ")
#age=int(age)
#print age>=18
#print age
#If all you want to do is print the input, this works well.
#But if you try to use the input as a number, youll get an error:
#age>=18
#TypeError: unorderable types: str() >= int()
#if age>=18:
#    print "You are old enough to vote."
# BUT IN MY TERMINAL IT IS WORKING PERFECTLY.
#rollercoaster.py
#We can resolve this issue by using the int() function, which tells Python to treat
# the input as a numerical value. The int() function converts a string representation
#of a number to a numerical representation, as shown here:
#PROBLEM --> NO DIFFERENCE BETWEEN WITH OT WITHOUT age=int(age)
# WITH age=int(age):
# Rishabhs-MacBook-Pro:Chapter_7_User_Input_And_While_Loop rishabhchopra$ python rollercoaster_using_int_to_accept_numerical_input.py
# Using int() to accept numerical input
# How old are you? 21
# True
# WITHOUT age=int(age)
# Rishabhs-MacBook-Pro:Chapter_7_User_Input_And_While_Loop rishabhchopra$ python rollercoaster_using_int_to_accept_numerical_input.py
# Using int() to accept numerical input
# How old are you? 21
# True
# Rishabhs-MacBook-Pro:Chapter_7_User_Input_And_While_Loop rishabhchopra$
"""There is no difference in the above cases as with the first time, when we use the int function:
We get True, cause yes the integer 21 is >= 18. But the second time when we compare the two and it returns True.
How is it comparing a string with a integer? Well, python is forced to ant str>int in Python. That is why you got True both times.
The first time 21 was actually >=18, the second time , a string is > the integer 18."""
print ("How to use int() function in an actual program?")
# Consider a prgram that determines weather someone is tall enough to ride a roller coaster.

height=input("How tall are you, in inches? ")
#height=int(height)

if height >= 36:
    print ("\nYou're tall enough to ride!")
else:
    print ("\nYou'll be able to ride when you're a little older")
# WORKS!
#Rishabhs-MacBook-Pro:Chapter_7_User_Input_And_While_Loop rishabhchopra$ python rollercoaster_using_int_to_accept_numerical_input.py
# How to use int() function in an actual program?
# How tall are you, in inches? 68

# You're tall enough to ride!
# Rishabhs-MacBook-Pro:Chapter_7_User_Input_And_While_Loop rishabhchopra$ python rollercoaster_using_int_to_accept_numerical_input.py
# How to use int() function in an actual program?
# How tall are you, in inches? 24

# You'll be able to ride when you're a little older
# Rishabhs-MacBook-Pro:Chapter_7_User_Input_And_While_Loop rishabhchopra$

# SEEING NO CHANGE EVEN IF I REMOVE height=int(height):==>
# Rishabhs-MacBook-Pro:Desktop rishabhchopra$ python age.py
# How tall are you, in inches? 68

# You're tall enough to ride!
# Rishabhs-MacBook-Pro:Desktop rishabhchopra$ python age.py
# How tall are you, in inches? 24

# You'll be able to ride when you're a little older
# Rishabhs-MacBook-Pro:Desktop rishabhchopra$

#when you use the input function , python interprets everything the
# user enters as a string.
"""Lesson: If the user input is going to be an integer:
make sure before you write what the program has to do, following the input function:
you write ==> variable=int(variable)
and then continue the rest of the program."""

